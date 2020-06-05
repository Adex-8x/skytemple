import os

from setuptools import setup, find_packages

# README read-in
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
# END README read-in


def recursive_pkg_files(file_ext):
    directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'skytemple')
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith(file_ext):
                paths.append(os.path.relpath(os.path.join('..', path, filename), directory))
    return paths


setup(
    name='skytemple',
    version='0.0.2a1',
    packages=find_packages(),
    description='GUI Application to edit the ROM of Pokémon Mystery Dungeon Explorers of Sky (EU/US)',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/SkyTemple/skytemple/',
    install_requires=[
        'ndspy >= 3.0.0',
        'skytemple-files >= 0.0.2a1',
        'pygobject >= 3.26.0',
        'pycairo >= 1.16.0',
        'natsort >= 7.0.0',
        'tilequant >= 0.0.1',
        'skytemple-ssb-debugger >= 0.0.2a1'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    package_data={'skytemple': ['*.css', 'data/*/*/*/*/*'] + recursive_pkg_files('.glade')},
    entry_points='''
        [skytemple.module]
        rom=          skytemple.module.rom.module:RomModule
        bgp=          skytemple.module.bgp.module:BgpModule
        map_bg=       skytemple.module.map_bg.module:MapBgModule
        script=       skytemple.module.script.module:ScriptModule
        monster=      skytemple.module.monster.module:MonsterModule
        portrait=     skytemple.module.portrait.module:PortraitModule
        [console_scripts]
        skytemple=skytemple.main:main
    ''',
    #dungeon=      skytemple.module.dungeon.module:DungeonModule
    #item=         skytemple.module.item.module:ItemModule
    #music=        skytemple.module.music.module:MusicModule
    #sprite=       skytemple.module.sprite.module:SpriteModule
    #stats=        skytemple.module.stats.module:StatsModule
)
