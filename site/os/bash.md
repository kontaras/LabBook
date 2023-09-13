## Redirect stdout and err to file
`CMD &> FILE` where `CMD` is the command to run and `FILE` is the log for output

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
