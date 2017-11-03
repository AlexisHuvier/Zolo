import os

LML={}
GLOBALS, LOCALS = globals(), locals()
_exec = lambda c: exec(c, GLOBALS, LOCALS)
include = lambda m: _exec("{module} = __import__('{module}')".format(module=m))
__create_fake_module = lambda m: _exec("class {module}: pass".format(module=m))
__add_module_to_fake_module = lambda ms, m: _exec("class {ms}: pass\n{module}.{ms} = {ms}".format(ms=ms, module=m))
exists = lambda m: _exec("""try:
    if {last}: __m = True
    else: __m = True
except: __m = False
""".format(last=m))

def include_all_modules(directory):
    files = os.listdir("{}/".format(directory)) if os.path.exists("{}/".format(directory)) else [os.mkdir(directory), []][1]
    ext_libs = ["{}.{}".format(directory, os.path.basename(f).split('.')[0]) for f in files if os.path.basename(f).split('.')[0] != '__pycache__']
    imported = []
    for module in ext_libs:
        try:
            if '.' in module:
                prefix, *m = module.split('.'); prefixs = [prefix]
                if len(m) > 1: prefixs = [p for p in m[:-1]] + [prefix]
                last = prefixs.pop(0); __create_fake_module(last) if not [exists(last), __m][1] else 0
                for p in prefixs:
                    __add_module_to_fake_module(p, last); last = p
            include(module); imported.append(module)
        except ImportError: pass
    return ext_libs, imported

def assistant():
    libs, imported = include_all_modules("modules")
    unimported = set(imported) ^ set(libs)
    if unimported:
        print("Could not import {}".format(", ".join(list(unimported))))
    for m in imported:
        last = m.split('.')[-1]
        _exec("LML[{mod}.{last}.prefix] = {mod}.{last}.moduleInstance".format(mod=m, last=last))

    a=0
    while a!=1:
        print("Que puis-je faire pour vous ?")
        rep=input()
        print("")
        test=rep.split(" ")
        if len(test)==1:
            rep+=" help"
        prefix,args=rep.split(" ",1)
        if prefix in LML:
            a=LML.get(prefix).handle(LML.get(prefix),args)
            print("")
        else:
            print("Je n'ai pas compris votre demande")
            print("")
    
