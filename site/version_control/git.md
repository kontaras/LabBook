# git

## Pulling code

### Checking out remote changes
`git pull`: Same as doing `git fetch ; git merge`  
`git pull --rebase`: Same as doing `git fetch ; git rebase`  
`git fetch`: Pull code from a remote repo into the local one  
`git merge`: Apply remote changes (already in your repo) into your checked out state  
`git rebase`: Apply the changes in your checked out state to the state pulled from the remote repo

### Blowing away changes that are committed
`git reset --hard origin/master`

### Move all changes from one branch to another
`git checkout foo
git merge origin/master`

## Undo local change
`git checkout <file path>`

## Pushing code

### Adding files to change
`git add`, `git rm`, `git mv`

### Checking in
`git commit` Commit local changes to local repo  
`git commit -m <message>`: Provide the commit message inline  
`git push`: Push changes from local repo to remote

### Adding more changes to local checkin
`git commit --amend`

### Moving uncommited work from branch to branch
`git checkout -b <new-branch>`  
Then `add` and `commit` as usual

## Looking at repo state

### Find the files that are open and not commited
`git status`

### Diffing against repo
`git diff HEAD`: Diff against local repo  
`git diff origin/master`: Diff against master repo

### What has not been pushed
`git log origin/master..HEAD`: See what has been committed but not pushed  
`git diff origin/master..HEAD`: Diff between what has been committed and what has been pushed
