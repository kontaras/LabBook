# gzip
## Open tar-ed and gzipped file
`tar zxvf <file.tgz>`

## Extract a single file out of a zipped tarball
1. Find file path using `tar -tzf <tarball.tgz> | grep <file>`
2. Extract file `tar -xzf <tarball.tgz> <path to file>`

# ls flags
`-l` long output

`-h` human readable file sizes

`-A` display all files other than `.` and `..`

`-t` sort by modification timestamp

# less
## Line numbers
`-N`

# ps
## See how log a process has been running
`ps -o etime= -p <PID>`

# systemctl
## Get the status logs for a service
`sudo systemctl status -l <SERVICE NAME>`

## More logs
`sudo journalctl -u <SERVICE NAME>.service`

# chmod
`u` user  
`g` goup  
`o` other  
`a` all

# vi
## delete all lines
`:1,$d` where `1` is the starting line number and `$` is the ending line number (EOF)  
`:%d` because `%` is all the lines in the file  
`Vggx` Delete from the current line to the start of file
`VGx` Delete from current line to end of file

## go to line
`1G` Go to line 1  
`$G` Go to last line

## copy-paste
`yy` Yank current line  
`p` put

## find
`/<word>`

# screen
## Connecting
`screen` start a new screen  
`screen -r` reconnect to your screen  
`screen -S <SESSION NAME>` start a new session

## Scrollback mode
`Ctrl+A, Esc` Enter scrollback  
`Up Down PageUp PageDown` Navigate  
`Esc` Exit

# firewalld
`sudo firewall-cmd --get-active-zones` Get configured zones  
`sudo firewall-cmd --zone=<ZONE> --add-port=<PORT>/tcp` Add a port, `--permanent ` to make it permanent
