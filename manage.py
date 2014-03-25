#!/usr/bin/env python
import logging
import os
import sys
from packages.libtool import include_file_sibling_folder
from packages.libtool.filetools import get_folder


def initialize_settings():
    include_file_sibling_folder(__file__, "packages")
    include_file_sibling_folder(__file__, "libs")
    from djangoautoconf import DjangoAutoConf
    #Added keys folder to path so DjangoAutoConf can find keys in it
    include_file_sibling_folder(__file__, "keys")
    c = DjangoAutoConf()
    c.set_default_settings("default.settings")
    c.set_root_dir(get_folder(__file__))
    c.add_extra_settings(["extra_settings.settings"])
    c.configure(['sae_settings', ])


if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "default.settings")
    #logging.basicConfig(level=logging.DEBUG)
    initialize_settings()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
