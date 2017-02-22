#!/usr/bin/env python3
from setuptools import setup, find_packages
setup(
name = 'HSModule',
version = '0.1.0',
description = 'Hearthstone classes',
long_description = 'Contains all classes needed for Hearthstone related programs',
keywords = 'Hearhtstone',
license = 'GPLv3',
author = 'Gregor Möller',
author_email = 'gregor_moeller@live.de',
url = 'https://github.com/GroovyGregor/Hearthstone',
classifiers = 
	['License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
	'Programming Language :: Python :: 3.5',
	'Operating System :: OS Independent',
	'Topic :: Games/Entertainment :: Turn Based Strategy',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'Topic :: Utilities'],
	
packages = find_packages(),
install_requires = 
	[]

)

