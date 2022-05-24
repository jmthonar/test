import os
import sys
import glob
import logging
import importlib
from pathlib import Path
from telethon import TelegramClient, events
from jmthon import jmthon, LOGGER
from jmthon.plugins import *

def load_plugins(plugin_name):
    path = Path(f"jmthon/plugins/{plugin_name}.py")
    name = "jmthon.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["jmthon.plugins." + plugin_name] = load

path = "jmthon/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

jmthon.start()

print("- تم بنجاح تنصيب سورس جمثون  @jmthon")

jmthon.run_until_disconnected()
