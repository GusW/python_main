from setuptools import setup

setup(
    name='myCompany',
    version='0.1.0',
    packages=['myCompany'],
    entry_points={
        'console_scripts': [
            'myCompany = myCompany.main:main'
        ]
    })
