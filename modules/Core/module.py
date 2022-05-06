class Core:
    def info(zolo, module):
        print(f"[Core] Version {module.version}")

    def stop(zolo, module):
        zolo.stop()