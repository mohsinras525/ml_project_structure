from setuptools import find_packages,setup
from typing import List


'''
this function is taken input a file path containing name of all pakages used by this project and step by step install it
'''
HYPHEN_E_DOT = "-e ."
def get_requirements(file_path :str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 's.m.m.r',
    author_email = 'mohsinrashid20@gmail.com',
    packages = find_packages(),
    install_requires =  get_requirements('requirements.txt')
)