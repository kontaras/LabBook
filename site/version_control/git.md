# Pulling code

## Clone repo
`git clone <URL>`

## Checking out remote changes
`git pull`: Same as doing `git fetch ; git merge`  
`git pull --rebase`: Same as doing `git fetch ; git rebase`  
`git fetch`: Pull code from a remote repo into the local one  
`git merge`: Apply remote changes (already in your repo) into your checked out state  
`git rebase`: Apply the changes in your checked out state to the state pulled from the remote repo

## Blowing away changes that are committed
`git reset --hard origin/master`

## Move all changes from one branch to another
    git checkout foo
    git merge origin/master

# You done goofed
## Undo local change
`git checkout -- <file path>`

## Backout commit
`git revert <Hash>`

## Delete an (unpushed) commit
`git reset --hard HEAD^`

## Combining two commits
`git rebase -i HEAD~2` (where HEAD~2 is the range of commits that need to be edited)  
Then mark the commit as `squash` or `fixup` (depending on whether you want to keep the commit message or not).

## Rename branch
`git branch -m <OLD NAME> <NEW NAME>`  
`git branch -m <NEW NAME> #Rename current branch`

## Undo an `add`
`git reset <file>`

## Fix author
`git config user.email <EMAIL>`  
`git commit --amend --no-edit --reset-author`

# Pushing code

## Adding files to change
`git add`, `git rm`, `git mv`

### Interactively adding select changes from a file
`git add -p <FILE NAME>` see unstaged changes  
`?` see commands  
`y` stage this chunk  
`n` leave chunk unstaged

## Checking in
`git commit` Commit local changes to local repo  
`git commit -m <message>`: Provide the commit message inline  
`git push`: Push changes from local repo to remote

## Adding more changes to local checkin
`git commit --amend`

## Creating a new branch
`git checkout -b <new-branch>`

## Deleting a branch
`git branch -d <branch>`

Force delete:  
`git branch -D <branch>`

Delete branch out of remote:  
`git push --delete <remote_name> <branch_name>`

# Looking at repo state

## Find the files that are open and not commited
`git status`

## Diffing against repo
`git diff HEAD`: Diff against local repo  
`git diff origin/master`: Diff against master repo

## What has not been pushed
`git log origin/master..HEAD`: See what has been committed but not pushed  
`git diff origin/master..HEAD`: Diff between what has been committed and what has been pushed

## See staged changes
`git diff --staged`

## See the last few changes
`git log -n <NUMBER>`

# Save credentials

## Windows
`git config --global credential.helper manager`

### Edit saved credentials
Search for `Credential Manager`

## OSX
Save: `git config --global credential.helper osxkeychain`

Delete: `git credential-osxkeychain erase`

# Stash
`git stash [push]` Push is implicit default  
`git stash pop`  
`git stash show -p` show stash as a diff

# Gerrit magical incantation  
`git push origin HEAD:refs/for/master`

# Tag a build
`git tag -a <TAG> [-m <MESSAGE>]`  
`git push --tags`

# git worktree

# Locally ignore file
Add it to `.git/info/exclude`
