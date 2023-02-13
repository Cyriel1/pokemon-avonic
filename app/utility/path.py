from os import path
import sys


def resource_path(relative):
    application_path = path.abspath(".")
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    return path.join(application_path, relative)
