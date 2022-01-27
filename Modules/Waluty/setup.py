from setuptools import setup

setup(
    name="Waluty",
    description="Wymiana na inne waluty",
    version="v1.0",
    author="Bartłomiej Kaim",
    author_email="",
    licence="MIT",
    install_requires=["Click"],
    packages=['Waluty'],
    entry_points={
        'console_scripts' : ['waluty = Waluty.main:main']
    }
)

