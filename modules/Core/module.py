class Core:
    def info(zolo, module, args):
        print(f"[Core] Version {module.version}")

    def stop(zolo, module, args):
        zolo.stop()

