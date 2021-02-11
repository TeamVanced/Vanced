# Setting Up adb

In this guide you will learn how to set up adb

---

## About adb

adb (Android Debug Bridge) is a command line tool that lets you communicate with your Android device from your PC.

It has a bunch of useful features like installing/uninstalling apps, collecting system logs from your phone and debugging apps.

It is an official Android sdk tool developed by Google, so it is completely safe to download and use!

---

## Prerequisites

### You will need

- PC (Windows/Mac/Linux)
- USB cable to connect your phone to your PC
- IQ higher than 70

### Enabling USB Debugging on your phone

In order to debug your phone with adb you first have to allow it. To do so, simply do the following steps on your phone:

- Enable Developer Options. You can do so by going to `Settings > About Phone` and tapping Build Number 7 times
- Now go to `Settings > System > Developer options` and enable USB Debugging

---

## Installing adb

Now on your PC:

- [Download adb](https://developer.android.com/studio/releases/platform-tools). Save it to wherever you want, it doesn't matter!
- Go to the folder you downloaded it to and extract the zip

Congratulations! You're all set and ready to use adb!

---

## Getting started using adb

### Open the adb folder in a terminal

- EITHER right click the folder and click `Open in Powershell / Open command prompt here / whatever`
- OR open a terminal manually and change directory to the adb folder with `cd PathToFullFolder` like `cd C:\Users\Ven\Downloads\adb` or `cd /home/ven/Downloads/adb`

### Now you can execute adb commands via:

- Windows: `.\adb myCommand`
- Linux: `./adb myCommand`

Make sure your phone is connected to your PC and unlocked!

---

## Let's test it!

- Unlock your phone and connect it to your PC
- Run `.\adb devices` or `./adb devices` depending on your Os
- If everything is okay, you should now get a popup on your Phone whether you want to allow USB Debugging. Select yes
- Your Terminal should print something like

```bash
List of devices attached
576OPB01    device
```

## Advanced - Adding adb to path for easier access

path is a variable that exists on all operating systems. It tells your terminal where to look for programs so you don't have to be in that program's directory all the time.

By adding adb to your path you can execute it from anywhere by simply typing `adb`. Doing so is very simple actually!

### Adding adb to your path on Windows

- Open the app search bar
- Search for env and choose `Edit the system environment variables`
- Click the Environment Variables button
- Under System Variables in the second half find PATH and click on edit
- Click New and paste the full path to the adb folder

Next time you start a terminal you can just run `adb` and it will know where to look!

### Adding adb to your path on Linux or Mac

- Open a terminal
- Find out which shell you're using via `echo $SHELL`
- Run the appropriate command for your shell:
  - zsh -> `echo "export PATH=/FULL/PATH/TO/ADB/FOLDER:$PATH" >> ~/.zshrc`
  - bash -> `echo "export PATH=/FULL/PATH/TO/ADB/FOLDER:$PATH" >> ~/.bash_profile`
- Make sure you replace `/FULL/PATH/TO/ADB/FOLDER` with the actual path
- Example with my setup: `echo "export PATH=/home/ven/Downloads/adb:$PATH" >> ~/.zshrc`

Next time you start a terminal you can just run `adb` and it will know where to look!