# gzip
## Open tar-ed and gzipped file
`tar zxvf <file.tgz>`

## Extract a single file out of a zipped tarball
1. Find file path using `tar -tzf <tarball.tgz> | grep <file>`
2. Extract file `tar -xzf <tarball.tgz> <path to file>`
