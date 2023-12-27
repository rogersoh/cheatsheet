# Cerificate Verification fail error
For those who this problem persists: - Python 3.6 (some other versions too?) on MacOS comes with its own private copy of OpenSSL. That means the trust certificates in the system are no longer used as defaults by the Python ssl module. To fix that, you need to install a certifi package in your system.

You may try to do it in two ways:

1) Via PIP:

```pip install --upgrade certifi```

2) If it doesn't work, Search in Finder:   
```Install Certificates.command ```
run it