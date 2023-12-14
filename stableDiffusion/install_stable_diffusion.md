# Automatic Stable Diffusion Installation on Linux

Install the dependencies:

Debian-based:  
```
sudo apt install wget git python3 python3-venv libgl1 libglib2.0-0
```

Red Hat-based:  
```
sudo dnf install wget git python3
```

Arch-based:

```sudo pacman -S wget git python3```

Navigate to the directory you would like the webui to be installed and execute the following command:

```wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh```

Run
```bash webui.sh```.

Check 
```webui-user.sh``` for options.

**Note**
The misunderstanding was that the shebang (#!/usr/bin/env bash) would force the script to use bash even with sh. But actually, using sh invokes the system's default /bin/sh (often dash), ignoring the shebang. Lesson learned: for consistent results, use bash explicitly.