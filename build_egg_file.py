from setuptools import setup, find_packages


setup(
    name = "MyFirstEggPackage",
    version = "0.1",
    packages = find_packages()
    )

#To build the .egg package
#Run: python build_egg_file.py bdist_egg
