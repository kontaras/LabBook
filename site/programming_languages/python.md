# pip
## Update
`pip list --outdated`  
`pip install <PKG> --upgrade`

## Install file
`pip install -r requirements.txt`

## Install into dir
`pip install -t <DIR>`

# PyCharm
## Configure test runner
Go into Settings/Preferences > Tools > Python Integrated Tools  
Change "Default test runner"

# venv
## Create
### Python 2
    python.exe -m pip install virtualenv
    python -m virtualenv <PATH TO VENV>
### Python 3
`python -m venv <PATH TO VENV>`

## Enter
PoweShell: `<PATH TO VENV>\Scripts\Activate.ps1`  
CMD: `<PATH TO VENV>\Scripts\activate.bat`  
bash: `source <PATH TO VENV>/bin/activate`  
