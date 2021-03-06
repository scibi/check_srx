# -*- coding: utf8 -*-
import setuptools

setuptools.setup(
    name="check-srx",
    version="0.1.0",
    url="https://github.com/scibi/check_srx",

    author="Patryk Ściborek",
    author_email="patryk@sciborek.com",

    description="Icinga/Nagios plugin for Juniper SRX firewalls",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        'junos-eznc',
        'nagiosplugin',
    ],
    package_data={
        'check_srx.tables': ['*.yml'],
    },

    entry_points={
        'console_scripts': [
            'check_srx = check_srx.main:main',
        ],
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
