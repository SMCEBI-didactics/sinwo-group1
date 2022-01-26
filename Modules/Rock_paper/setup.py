from setuptools import setup

setup(
    name="Rock_paper",
    description="Funkcja obsługująca grę w kamień, papier, nożyce",
    version="1.0",
    author="Oskar Kocjan",
    author_email="oskar.kocjan@smcebi.edu.pl",
    licence="MIT",
    packages=['Rock_paper'],
    entry_points={'console_scripts' : ['rock_paper = Rock_paper.main:main']}
)

