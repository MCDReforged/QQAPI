import os
import shutil
import zipfile

NAME = 'CoolQAPI'
PLUGIN_DIR = 'plugins'
TEMP_DIR = f'{os.path.join(PLUGIN_DIR, NAME)}_temp'
PLUGIN_NAME = f'{NAME}-MCDR.py'


def setup(files: dict):
    zipfile_name = list(files.keys())[0]
    version_name = zipfile_name.rstrip('.zip')
    with zipfile.ZipFile(os.path.join(PLUGIN_DIR, zipfile_name)) as f:
        f.extractall(TEMP_DIR)
    temp_dir = os.path.join(TEMP_DIR, version_name)
    shutil.copytree(os.path.join(temp_dir, NAME), os.path.join(PLUGIN_DIR, NAME))
    shutil.copyfile(os.path.join(temp_dir, PLUGIN_NAME), os.path.join(PLUGIN_DIR, PLUGIN_NAME))
