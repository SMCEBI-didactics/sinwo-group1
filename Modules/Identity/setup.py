from setuptools import setup

setup(
    name="Identity",
    description="Generuje losowe dane osobowe",
    version="v1.0",
    author="Adrian Lewandowski",
    author_email="",
    licence="",
    packages=['Identity'],
    entry_points={
        'console_scripts' : ['identity = Identity.main:main']
    }
)

