from setuptools import setup

setup(
    name="Verify",
    description="Szyfrowanie hasła",
    version="v1.0",
    author="Albert Szadziński",
    author_email="",
    licence="MIT",
    install_requires=["Click"],
    packages=['Verify'],
    entry_points={
        'console_scripts' : ['verify = Verify.main:main']
    }
)

