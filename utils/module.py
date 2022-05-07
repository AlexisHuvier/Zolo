import importlib


class Module:
    def __init__(self, name, author, prefix, version, module, reload = False):
        """
        Create module

        Args:
            name (string): Name of module
            author (string): Author of module
            prefix (string): Prefix of module
            version (string): Version of module
            module (string): Name of Class of module
        """
        self.name = name
        self.author = author
        self.prefix = prefix
        self.version = version
        self.module = module
        self.commands = []
        
        temp = importlib.import_module(f"modules.{self.name}.module")
        if reload:
            importlib.reload(temp)
        self.moduleImport = eval(f"temp.{self.module}")
