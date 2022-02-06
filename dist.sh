#!/bin/bash
. utils.sh

# Check if on master
git status
confirm "Are you are on a clean master branch in the virtual environment" "No" READY
if [[ "$READY" == "Yes" ]]; then
    echo -e "OK."
else
    echo -e "make a commit, checkout to master and merge with this branch before calling dist.sh"
    exit 1
fi

# tag
echo -e "Last commit is $(git describe --tags)"
echo -e "Current tag is $(git describe --tags --abbrev=0)" 
read -r -p "What will be the tag of this new version? " NEWTAG
git tag -a $NEWTAG -m "Version $NEWTAG"

# publi
confirm "Publish to Pypi" "No" PUBLISHTOPYPI
if [[ "$PUBLISHTOPYPI" == "Yes" ]]; then  
    echo -e "\nPublishing to PyPI...\n"
    PACKAGEINDEX="pypi"
else
    echo -e "\nPublishing to TestPyPY...\n"
    PACKAGEINDEX="testpypi"
fi

# update the docs ?
confirm "Update the docs" "No" UPDATEDOCS
if [[ "$UPDATEDOCS" == "Yes" ]]; then  
   
    bash build_docs.sh || exit 1
    git tag -d $NEWTAG
else
    # update requirements.txt only
    echo -e "\nUpdating requirements.txt !\n"
    bash update_requirements.sh || exit 1
fi

# set tag
git tag -a $NEWTAG -m "Version $NEWTAG"
git push --tags

# create wheel
python setup.py bdist_wheel || exit 1

# upload wheel to testpypi
twine upload --skip-existing -r "${PACKAGEINDEX}" dist/* || exit 1
