## Perforce

### Pulling code
`p4 sync`

### Checking in code

#### Creating changelist
`p4 change`

#### Checking in to repo
`p4 submit -c <CLN>`

### Checking local state

##### See what is opened
`p4 opened`

### Crosporting change
```bash
p4 integrate  //depot/<path>...@CLN,CLN  //depot/<path>...
p4 resolve
```
