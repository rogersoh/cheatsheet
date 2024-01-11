# Personal Access Token
Store personal access token in credential helper store
```
git config --global credential.helper store
```
1. Just to add a note to this - after enabling this you will be prompted for your creds on your next commit. After that, they are stored. 
2. This seems to store your token in plain text in ~/.git-credentials 
