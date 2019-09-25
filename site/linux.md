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
