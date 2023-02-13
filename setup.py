from setuptools import setup, find_packages

with open('requirements.txt') as file:
    requirements = file.readlines()

setup(
    name='pokemon_avonic_package',
    version='1.0',
    description='Coding Challenge Avonic - Pokemon Game',
    author='Cyriel van der Raaf',
    author_email='cyrielvdraaf@hotmail.com',
    url='https://avonic.com/',
    license='LICENSE',
    packages=find_packages(),
    install_requires=requirements,
)
