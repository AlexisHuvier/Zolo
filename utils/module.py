import importlib

class Module:
    def __init__(self, name, author, prefix, version, module):
        self.name = name
        self.author = author
        self.prefix = prefix
        self.version = version
        self.module = module
        self.commands = []

        temp = importlib.import_module(f"modules.{self.name}.module")
        self.moduleImport = eval(f"temp.{self.module}")