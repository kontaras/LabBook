# Perforce

## Pulling code
`p4 sync`

## Checking in code

## Moving all open files into a change
Either make a new change  
or  
`p4 reopen -c <CLN> ...`

### Creating changelist
`p4 change`

### Checking in to repo
`p4 submit -c <CLN>`

## Checking local state

#### See what is opened
`p4 opened`

## Shelves

#### Shelving
TBD

### Unshelving
`p4 unshelve -s <Shelf Number> [-c <CLN>]`

## Undo the damage

### Reverting default change list
`p4 revert -c default //...`

### Backout a change
`p4 undo "@<CLN>"`

## Crosporting change
```bash
p4 integrate  //depot/<path>...@CLN,CLN  //depot/<path>...
p4 resolve
```
