# Git Pull Request Merge
1.  if there is no merge confict detected
- Click on the Merge button from Github browser

2. At **Terminal** to pull the latest update to the main
```
git checkout main
git pull
```

# Start a new branch  

```git checkout -b <new branch name>```  

example *git checkout -b csv_file_reader_phase_2*

## Start a new branch branching off an old branch
```git checkout -b <new branch> <old branch> ```

# Remove a local branch
```git branch --delete <branchname>```

# Using Git to move a file to different folder
```
git mv <filename> <new folder/>
```
