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

# screen
## Connecting
`screen` start a new screen  
`screen -r` reconnect to your screen  

## Scrollback mode
`Ctrl+A, Esc` Enter scrollback  
`Up Down PageUp PageDown` Navigate  
`Esc` Exit
