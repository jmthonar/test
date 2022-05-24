import os
import sys
import glob
import logging
import importlib
from pathlib import Path
from telethon import TelegramClient, events
from jmthon import jmthon, LOGGER
from jmthon.plugins import *
from jmthon.helpers.extdl import install_pip
from telethon.tl.types import InputMessagesFilterDocument

PLUGIN_CHANNEL = -1001712823896

async def install():
    documentss = await jmthon.get_messages(
        PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument
    )
    total = int(documentss.total)
    for module in range(total):
        plugin_to_install = documentss[module].id
        plugin_name = documentss[module].file.name
        if os.path.exists(f"jmthon/plugins/{plugin_name}"):
            return
        downloaded_file_name = await jmthon.download_media(
            await jmthon.get_messages(PLUGIN_CHANNEL, ids=plugin_to_install),
            "jmthon/plugins/",
        )
        path1 = Path(downloaded_file_name)
        shortname = path1.stem
        type = True
        check = 0
        while type:
            try:
                load_module(shortname.replace(".py", ""))
                break
            except ModuleNotFoundError as e:
                install_pip(e.name)
                check += 1
                if check > 5:
                    break


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
print("- تم بنجاح تنصيب سورس جمثون")
jmthon.loop.create_task(install())
jmthon.run_until_disconnected()
