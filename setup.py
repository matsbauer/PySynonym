from setuptools import setup

setup(
    name = "PySynonym",
    version = "0.0.3",
    author = "Mats Bauer",
    author_email = "mats.bauer@icloud.com",
    description = ("PySynonym is a plugin that returns a list of synonyms for the given word. This is very useful when programming bots and digital assistants, to increase their understanding. "),
    license = "BSD",
    keywords = "python synonym plugin",
    url = "https://github.com/matsbauer/PySynonym",
    packages=['PySynonym'],
    long_description=open('README.md').read(),
    install_requires=['bs4']
)