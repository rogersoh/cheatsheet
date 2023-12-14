# Install python 3.10 in linux subsystem

Before installing any software, you should update repositories and install the latest versions of packages. 
```
apt update && sudo apt upgrade -y 
```

## Install Python 3.10 from PPA repository
  
To install Python 3.10 on Ubuntu 20.04 using a repository you need to add PPA repository from deadsnakes. Indeed this makes it very easy to install Python on Ubuntu  and get constant updates, bug fixes and security updates. 

Install the necessary dependencies to add the repository. 
```
apt install software-properties-common -y 
```
Now let's add the PPA repository from deadsnakes:
```
add-apt-repository ppa:deadsnakes/ppa 
```

## How to install Python 3.10 on Ubuntu 20.04
 

Now that the deadsnakes repository has been added to your Ubuntu system, we can install Python 3.10 using the command below.

```
 apt install python3.10
```

After installation, check the installed version of Python.
``` 
python3.10 --version
 ```
