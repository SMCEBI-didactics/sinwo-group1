from setuptools import setup

setup(
    name="Tic_tac_toe",
    description="Funkcja obsługująca grę w kółko i krzyżyk",
    version="1.0",
    author="Oskar Kocjan",
    author_email="oskar.kocjan@smcebi.edu.pl",
    licence="MIT",
    packages=['Tic_tac_toe'],
    entry_points={'console_scripts' : ['tic_tac_toe = Tic_tac_toe.main:main']}
)

