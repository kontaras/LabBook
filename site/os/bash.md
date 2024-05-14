## Redirect stdout and err to file
`CMD &> FILE` where `CMD` is the command to run and `FILE` is the log for output


## Redirect stderr into stdout
`2>&1`

## `find`
`find <PATH> <TESTS>` Where:  
`PATH`: Path in which to look  
`TESTS`:  

* `-name <EXP>`: file name matching expression
* `-iname <EXP>`: file name matching expression, case insensitive
* `-path <EXP>`: path name matching expression
* `-ipath <EXP>`: path name matching expression, case insensitive

## Background processes
List: `jobs`  
Connect: `fg %<NUM>`  
Kill: `kill %<NUM>`

## Get absolute path to a file
`realpath <FILE NAME>`  
`realpath -m <FILE NAME>` to allow for non-existent files  

## Get total size of dir
`du -sh <PATH>` Total size of PATH  
`du -h -d 1 <PATH>` Also get the size by sub-dir (larger values of `-d` for sub-sub-dirs)
