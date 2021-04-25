# BootsOff  
### O. KAUFMANN, 2021.  
  
BootsOff brings together tools for the preparation and processing of geophysical data.

[![Documentation](https://readthedocs.org/projects/bootsoff/badge/?version=latest)](https://bootsoff.readthedocs.io/en/latest/?badge=latest
)
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


## Table of Contents
1. [Description of the project](#Description-of-the-project)
2. [Prerequisites](#Prerequisites)
3. [Installation](#Installation)
4. [Contributing](#Contributing)
5. [License](#License)
6. [Citation](#Citation)
7. [Contact](#Contact)

## Description of the project <a name="Description-of-the-project"></a>

BootsOff brings together tools for the preparation and processing of geophysical data. These tools rely on classes that 
describe common acquisition patterns. 

## Prerequisites <a name="Prerequisites"></a>

The project is developed in a virtual environment using pipenv. It is therefore necessary to install pyenv and pipenv before starting the installation of the program.  

Pyenv will setup the virtual environment with the correct version of Python. Pipenv will add the required python dependencies automatically during installation.  

Refer to this [link](https://github.com/pyenv/pyenv-installer) to install Pyenv and this [link](https://pipenv.pypa.io/en/latest/install/) to install Pipenv, the prerequisites.  
## Installation <a name="Installation"></a>
To clone the repository and setup the environment for using this project :

.. code-block:: bash 

   $  git clone git@github.com:kaufmanno/BootsOff.git  
   $  cd BootsOff/  
   $  pipenv shell  
   $  pipenv install   

To view installed dependencies, see the [Pipfile](https://github.com/kaufmanno/BootsOff/blob/master/Pipfile). Be aware that using *pipfile install* actually installs from the Pipfile.lock file. Use the --skip-lock option if you want to use the Pipfile instead.  
  

## Contributing <a name="Contributing"></a>

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Also have a look at this note about [contributing](https://github.com/kaufmanno/BootsOff/blob/master/CONTRIBUTING.md).  

Please note we have a [code of conduct](https://github.com/kaufmanno/BootsOff/blob/master/CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.  


## License <a name="License"></a>

The license of the project is avalaible on the [license](https://github.com/kaufmanno/BootsOff/blob/master/LICENSE) file.  

## Citation <a name="Citation"></a>

@@@ Please provide a citation here!  

## Contact <a name="Contact"></a>

We are interested in your feedback. Please create issues for bug reports, suggestions, PR and questions.  
