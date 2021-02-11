# Creating A Logcat

In this guide you will learn how to create a logcat to help app developers fix bugs

---

## About Logcat

Logcat is a command line tool that dumps Android system logs, including stuff like errors or warnings.

These logs are very important to figure out what's going wrong!

---

## Prerequisites

### You will need

- EITHER a PC with adb set up - A guide to do this can be found [here](./SettingUpAdb.md)
- OR a rooted phone

---

## Creating a logcat

There are two ways to create a logcat. Either via a pc and adb or via a terminal on your Phone, but this requires root.

You can technically create a logcat with only your phone and no root, but this will only include limited info so it is not very useful!

### Creating a logcat using adb on your PC

- Run the following adb command. Unless you added adb to PATH, add a `.\` before the command. Having issues? Check the [Guide](./SettingUpAdb.md#Getting%20started%20using%20adb)

```bash
adb shell logcat -c
adb shell logcat *:W > logcat.txt
```

- If this prints nothing and just freezes your terminal, perfect! That means it's working
- Now just do whatever is needed to cause the issue on your phone
- Once that is done, simply press CTRL+C or close the terminal to stop the logcat
- Your logcat can be found in the adb folder as logcat.txt

### Creating a logcat using a rooted Android

- First you need a Terminal. I recommend [Termux](https://play.google.com/store/apps/details?id=com.termux)
- Open it up and run the following command

```bash
su -c "logcat -c && logcat *:W > /sdcard/logcat.txt"
```

- Grant root if prompted
- Now just do whatever is needed to cause the issue on your phone
- Once that is done, simply press CTRL+C or close the terminal to stop the logcat
- Your logcat can be found at /sdcard/logcat.txt which is the root of your file system where there's also stuff like your Download folder
