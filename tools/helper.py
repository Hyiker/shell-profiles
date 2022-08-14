# coding: utf-8
from __future__ import annotations
from enum import Enum
from typing import Collection


class TargetPlat(Enum):
    POWERSHELL = 1
    BASH = 2


class Exportable:
    def __init__(self, plats: Collection = [TargetPlat.POWERSHELL, TargetPlat.BASH]):
        self.plats = set(plats)

    def export_ps(self) -> str:
        pass

    def export_bash(self) -> str:
        pass


class AliasCommand(Exportable):
    '''
    make an alias $name->$value
    '''

    def __init__(self, name: str, value: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.value = value

    def export_ps(self) -> str:
        return f'Set-Alias -Name {self.name} -Value "{self.value}"'

    def export_bash(self) -> str:
        return f'alias {self.name}="{self.value}"'


class EVCommand(Exportable):
    '''
    export a environment variable $key->$value
    '''

    def __init__(self, key: str, value: str, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.value = value

    def export_ps(self) -> str:
        return f'$env:{self.key}="{self.value}"'

    def export_bash(self) -> str:
        return f'export {self.key}="{self.value}"'


class CustomShellFunction(Exportable):
    '''
    export custom shell function 
    '''

    def __init__(self):
        super().__init__(plats=[])

    def set_ps_func(self, func: str):
        self.ps_func = func
        self.plats.add(TargetPlat.POWERSHELL)

    def set_bash_func(self, func: str):
        self.bash_func = func
        self.plats.add(TargetPlat.BASH)

    def export_ps(self) -> str:
        return self.ps_func

    def export_bash(self) -> str:
        return self.bash_func


class ShellFunctionProxy:
    '''
    proxy for shell function
    '''

    def __init__(self, exportable_collection: ExportableCollection):
        self._csf = CustomShellFunction()
        self._exportable_collection = exportable_collection

    def add_ps_func(self, content: str) -> ShellFunctionProxy:
        self._csf.set_ps_func(content)
        return self

    def add_bash_func(self, content: str) -> ShellFunctionProxy:
        self._csf.set_bash_func(content)
        return self

    def add_ps_func_from_file(self, file: str) -> ShellFunctionProxy:
        with open(file, 'r') as foo:
            self.add_ps_func(foo.read())
        return self

    def add_bash_func_from_file(self, file: str) -> ShellFunctionProxy:
        with open(file, 'r') as foo:
            self.add_bash_func(foo.read())
        return self

    def build(self):
        self._exportable_collection.append(self._csf)


class ExportableCollection(list):
    def _filter_target(self, target: TargetPlat) -> str:
        return [cmd for cmd in self if target in cmd.plats]

    def add_alias(self, *args, **kwargs):
        self.append(AliasCommand(*args, **kwargs))

    def add_ev(self, *args, **kwargs):
        self.append(EVCommand(*args, **kwargs))

    def build_custom_shell_func(self) -> ShellFunctionProxy:
        return ShellFunctionProxy(self)

    def compile_ps(self) -> str:
        return ';\n'.join([cmd.export_ps() for cmd in self._filter_target(TargetPlat.POWERSHELL)])+';'

    def compile_bash(self) -> str:
        return '\n'.join([cmd.export_bash() for cmd in self._filter_target(TargetPlat.BASH)])
