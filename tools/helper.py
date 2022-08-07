# coding: utf-8

class Command:
    def __init__(self):
        pass

    def export_ps(self) -> str:
        raise NotImplementedError('powershell export for {} is not implemented'.format(self.__class__.__name__))

    def export_bash(self) -> str:
        raise NotImplementedError('bash export for {} is not implemented'.format(self.__class__.__name__))


'''
make an alias $name->$value
'''


class AliasCommand(Command):
    def __init__(self, name: str, value: str):
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
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

    def export_ps(self) -> str:
        return f'$env:{self.key}="{self.value}"'

    def export_bash(self) -> str:
        return f'export {self.key}="{self.value}"'


class CommandCollection(list):
    def compile_ps(self) -> str:
        return ';\n'.join([cmd.export_ps() for cmd in self])+';'

    def compile_bash(self) -> str:
        return '\n'.join([cmd.export_bash() for cmd in self])
