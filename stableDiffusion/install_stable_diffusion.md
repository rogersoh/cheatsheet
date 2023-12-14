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

```Run webui.sh```.
Check ```webui-user.sh``` for options.