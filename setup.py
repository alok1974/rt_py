# -*- coding: utf-8 -*-
from distutils.core import setup
from glob import glob


PACKAGE_NAME = 'rt_py'
PACKAGE_VERSION = '0.1.0'


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='Python port of raytracing in one weekend book',
    author='Alok Gandhi',
    author_email='alok.gandhi2002@gmail.com',
    url=f'https://github.com/alok1974/{PACKAGE_NAME}',
    packages=[f'{PACKAGE_NAME}'],
    package_dir={f'{PACKAGE_NAME}': f'src/{PACKAGE_NAME}'},
    download_url=(f'https://github.com/alok1974/chessly/archive/v{PACKAGE_VERSION}.tar.gz'),
    scripts=glob('src/scripts/*'),
    install_requires=['Pillow >=9.5.0'],
    license='MIT',
)
