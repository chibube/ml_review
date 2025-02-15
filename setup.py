from setuptools import find_packages, setup #this enables the setup.py file find all the packages used in the directory (or application)
#find packages does this by identifying how many directories have "__init__" in them. 
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements, hence the arrow pointing to list
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #if the txt file moves to the next line the readlines method will include \n when reading it, so we 
                                            #remove it
        requirements=[req.replace("\n","") for req in requirements] #replacing \n with blanks

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) #we don't want the -e . when reading the requirements file, it is only for calling up the setup.py
    
    return requirements

setup(
    name='mlreview',
    version='0.0.1',
    author='Chimdi',
    author_email='bubefro@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') 
    )