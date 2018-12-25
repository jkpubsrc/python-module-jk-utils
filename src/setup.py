﻿from setuptools import setup


def readme():
	with open('README.rst') as f:
		return f.read()


setup(name='jk_utils',
	version='0.2018.12.24',
	description='This python module provides various utility functions and classes.',
	author='Jürgen Knauth',
	author_email='pubsrc@binary-overflow.de',
	license='Apache 2.0',
	url='https://github.com/jkpubsrc/python-module-jk-utils',
	download_url='https://github.com/jkpubsrc/python-module-jk-utils/tarball/0.2018.12.24',
	keywords=[
		"utilities"
	],
	packages=[
		"jk_utils",
		"jk_utils.async",
	],
	install_requires=[
		#"netifaces",
		#"jk_simpleexec",
	],
	include_package_data=True,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Programming Language :: Python :: 3.5',
		'License :: OSI Approved :: Apache Software License'
	],
	long_description=readme(),
	zip_safe=False)












