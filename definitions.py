from pathlib import Path

def get_version():
    cmd = ['git', 'describe', '--tags', '--abbrev=0']
    output = check_output(cmd)
    return output.decode('latin1').strip()
    
def get_release():
    cmd = ['git', 'describe', '--tags']
    output = check_output(cmd)
    return output.decode('latin1').strip()

PROJECT = u'BootsOff'
AUTHOR = u'O. KAUFMANN'
VERSION = get_version()
RELEASE = get_release()
LICENSE = u'GPLv3'
SHORT_DESCRIPTION = 'Bootsoff bundles tools for applied geophysics'
ROOT_DIR = str(Path(__file__).parent.absolute())
URL = f'https://github.com/kaufmanno/{PROJECT}'
