# update.sh

`update.sh` is a little shell script that I run periodically to update packages in various package managers.
Some proprietary/environment specific settings are omitted. 

## OSX bash
    #! /bin/bash
    bold=$(tput bold)
    normal=$(tput sgr0)
    
    # Run timestamp
    date
    
    echo
    echo "-----------------------------------------------------------------------------------------"
    echo
    
    # Update various toolchain git repos
    # I always want to use the latest version
    TOOLS_REPOS=($HOME'/tools' $HOME'/more_tools')
    
    for REPO in "${TOOLS_REPOS[@]}"
    do
      echo $REPO
      git -C "$REPO" pull -p
      echo
      echo "-----------------------------------------------------------------------------------------"
      echo
    done
    #nuosetup/bin/init-3rdparty
    
    # Get the latest versions of brew packages, but let me decide to install them
    brew update
    
    echo "Brew outdated: ${bold}brew upgrade${normal}"
    brew outdated --formula --greedy
    
    echo
    
    echo "Brew outdated: ${bold}brew upgrade --cask${normal}"
    brew outdated --cask --greedy
    
    echo
    echo "-----------------------------------------------------------------------------------------"
    echo
    
    # Get the latest versions of python packages in each python installation, but
    # let me decide to install them
    PYTHONS=('python3')
    
    for PY_VERSION in "${PYTHONS[@]}"
    do
      PIP_CMD="$PY_VERSION -m pip"
      echo "Pip outdated: ${bold}$PIP_CMD install -U${normal}"
      $PIP_CMD list --outdated
      echo
      echo "-----------------------------------------------------------------------------------------"
      echo
    done
    
    # Get the latest versions of ports packages, but let me decide to install them.
    # Unfortunately, I need to be sudo to fetch new package versions, so the 
    # selfupdate command needs to be manually run periodically.
    echo "MacPorts outdated: ${bold}sudo port upgrade${normal}"
    port outdated
    echo
    echo "Also periodically run: ${bold}sudo port selfupdate${normal}"
