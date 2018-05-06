import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AutoOps.settings")
    import django
    django.setup()

    from backend import main


    obj = main.HostManager()
    obj.interactive()
