# Creating a virtual environment using python 3.9
Here venv_local is the location to create the virtual environment.  
```python3.9 -m venv venv_local_3.9```

Activating a virtual environment  
```source venv_local_3.9/bin/activate```

The python to use should be in the venv_local bin directory  
```which python```

Leaving the virtual environment  
```deactivate```

## To install packages using a requirement file  
```python -m pip install -r requirements_3_9.txt```

See the following link for more details:  
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment