# coding: utf-8
from enum import Enum


class TargetPlat(Enum):
    POWERSHELL = 1
    BASH = 2


class Command:
    def __init__(self, plats: list[TargetPlat] = [TargetPlat.POWERSHELL, TargetPlat.BASH]):
        self.plats = plats

    def export_ps(self) -> str:
        pass

    def export_bash(self) -> str:
        pass


'''
make an alias $name->$value
'''


class AliasCommand(Command):
    def __init__(self, name: str, value: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.value = value

    def export_ps(self) -> str:
        return f'Set-Alias -Name {self.name} -Value "{self.value}"'

    def export_bash(self) -> str:
        return f'alias {self.name}="{self.value}"'


'''
export a environment variable $key->$value
'''


class EVCommand(Command):
    def __init__(self, key: str, value: str, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.value = value

    def export_ps(self) -> str:
        return f'$env:{self.key}="{self.value}"'

    def export_bash(self) -> str:
        return f'export {self.key}="{self.value}"'


class CommandCollection(list):
    def _filter_target(self, target: TargetPlat) -> str:
        return [cmd for cmd in self if target in cmd.plats]

    def add_alias(self, *args, **kwargs):
        self.append(AliasCommand(*args, **kwargs))

    def add_ev(self, *args, **kwargs):
        self.append(EVCommand(*args, **kwargs))

    def compile_ps(self) -> str:
        return ';\n'.join([cmd.export_ps() for cmd in self._filter_target(TargetPlat.POWERSHELL)])+';'

    def compile_bash(self) -> str:
        return '\n'.join([cmd.export_bash() for cmd in self._filter_target(TargetPlat.BASH)])
