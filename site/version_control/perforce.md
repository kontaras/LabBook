# Perforce

## Pulling code
`p4 sync "[file][@1,CLN]"`

## Checking in code

### Moving all open files into a change
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

### Shelving
    p4 shelve -c <CLN>
    p4 revert -c <CLN>

### List shelves
`p4 changes -u <USERNAME> -s shelved`

### See the contents of a shelf
`p4 describe -S <CLN>`

### Diff current workspace vs. shelf
`p4 diff "@=<Shelf #>"`

### Unshelving
`p4 unshelve -s <Shelf Number> [-c <CLN>]`

### Deleting shelf
`p4 shelve -d -c <CLN>`

## Undo the damage

### Reverting default change list
`p4 revert -c default //...`

### Backout a change
`p4 undo "@<CLN>"`

## Crosporting change
    p4 integrate  //depot/<path>...@CLN,CLN  //depot/<path>...
    p4 integrate  //depot/<path>...@=CLN  //depot/<path>...
    p4 resolve

### Mass crosporting
    p4 integrate  //depot/<path>...  //depot/<path>...
    p4 resolve
