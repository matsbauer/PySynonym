from setuptools import setup

setup(
    name = "PySynonym",
    version = "0.0.6",
    author = "Mats Bauer",
    author_email = "mats.bauer@icloud.com",
    description = ("PySynonym is a plugin that returns a list of synonyms for the given word. This is very useful when programming bots and digital assistants, to increase their understanding. "),
    license = "BSD",
    keywords = "python synonym plugin",
    url = "https://github.com/matsbauer/PySynonym",
    packages=['PySynonym'],
    #long_description=open('readme-pypi.rst').read(),
    install_requires=['bs4', 'beautifulsoup4', 'urllib2']
)