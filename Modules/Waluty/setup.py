from setuptools import setup

setup(
    name="Kantor",
    description="Wymiana na inne waluty",
    version="v1.0",
    author="Bartłomiej Kaim",
    author_email="",
    licence="MIT",
    install_requires=["Click"],
    packages=['Waluty'],
    entry_points={
        'console_scripts' : ['Przeliczwaluty = Przeliczwaluty.main:main']
    }
)

