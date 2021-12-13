from setuptools import setup

setup(
    name="Verify-SMCEBI",
    description="",
    version="v0.1",
    author="",
    author_email="",
    licence="",
    packages=['Verify'],
    entry_points={
        'console_scripts' : ['verify = Verify.main:main']
    }
)

