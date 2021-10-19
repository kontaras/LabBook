# brew

## Install

### Package Manager
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

### Lookup package
`brew search <PKG>`

### Package info
`brew info <PKG>`  
`brew cask info <PKG>`

### Install Package
`brew install <PKG>`  
`brew cask install <PKG>`

## Updating

### Brew self update:
`brew update`

### list out of date:
`brew outdated`  
`brew cask outdated`

### update all out of date packages
`brew upgrade`  
`brew cask upgrade`

# Debug
## Find service holding a port
`netstat -vanp tcp | grep <PORT>`  
`lsof -i tcp:<PORT>`

# java_home
## Get installed versions
`/usr/libexec/java_home -V`

## Setting JAVA_HOME
``export JAVA_HOME=`/usr/libexec/java_home -v11<VERSION>` ``
