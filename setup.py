
from setuptools import find_packages,setup
# Importing the find_packages and setup functions from setuptools.
# - find_packages: Automatically detects and lists all Python packages in the source directory.
# - setup: Configures the metadata and options for the Python package distribution, enabling its installation and use.

from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #Reads the requirements.txt file line by line.
        requirements=[req.replace("\n","") for req in requirements] #Strips newline characters (\n) from each requirement.

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) #Removes -e . from the list if it exists, as it is not a library dependency.
    
    return requirements

setup(
name='mlproject',                        # The name of the package being created.
version='0.0.1',                         # The initial version of the package following semantic versioning (major.minor.patch).
author='atharvabhishma',                 # The name of the author or maintainer of the package.
author_email='atharvabhishma@gmail.com', # The email address for the author or maintainer, used for contact or support.
packages=find_packages(),                # Automatically finds and includes all Python packages in the directory using find_packages().
                                            # This avoids manually specifying package directories.
install_requires=get_requirements('requirements.txt')
# Specifies the dependencies required for the package, read from an external requirements.txt file.
    # The get_requirements function is to parse this file and return a list of dependencies.

)
