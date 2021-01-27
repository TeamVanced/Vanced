# Vanced Issue Center 
> ###### The purpose of this repo is to help you find your way around.
___

#### Make sure you look through the issues pages to check for a issue already open that describes your problem or idea and give it a thumbs up reaction and add a comment instead of opening a duplicate issue.

#### Note that issues related to Vanced Manager, Vanced MicroG or Vanced Music do not belong here. You can find more info below.
___
<a href="https://vancedapp.com"><img src="https://cdn.discordapp.com/emojis/724333860598579290.png" alt="Vanced" height="55" align="left"></a>
## For Vanced
### Have a Vanced bug?
Head over to the [Issues Page](https://github.com/YTVanced/Vanced/issues), create a new issue and put the `[Bug]` tag as a title prefix

### Have a ideas for Vanced?
Head over to the [Issues Page](https://github.com/YTVanced/Vanced/issues), create a new issue and put the `[Idea]` tag as a title prefix
___
<a href="https://github.com/YTVanced/VancedManager"><img src="https://cdn.discordapp.com/emojis/727995382012837898.png" alt="Vanced Manager" align="left" height="70" ></a>
## Have a Manager bug? 
Head over to the [Vanced Manager Issues Page](https://github.com/YTVanced/VancedManager/issues)
___
<a href="https://github.com/YTVanced/VancedMicroG"><img src="https://cdn.discordapp.com/emojis/739533000609628191.png" alt="Vanced MicroG" height="75" align="left" ></a>
## Have a Vanced MicroG bug?
Head over to the [Vanced MicroG Issues Page](https://github.com/YTVanced/VancedMicroG/issues)
___
<img src="https://cdn.discordapp.com/emojis/771642079318638603.png" alt="Vanced SponsorBlock" height="65" align="left"></a>
## Have a Vanced Music bug?
Sorry but we don't provide support for Vanced Music at this time as it is only a side project. Unless your bug breaks the main functionality, it will most likely not be fixed
___
<a href="https://github.com/YTVanced/SponsorBlock"><img src="https://cdn.discordapp.com/attachments/548867094259826700/776979672264474644/LogoSponsorBlockSimple256px.png" alt="Vanced SponsorBlock" height="70" align="left"></a>
## Have a features request for our SponsorBlock implementation?
Head over to the [Vanced SponsorBlock Issues Page](https://github.com/YTVanced/SponsorBlock/issues)

________


## Creating a Logcat
A logcat is a log of all your system messages. This includes a lot of debug information and also any errors that might have occurred. This info can be very useful for developers in some cases.

We might ask you for one in which case you simply need to follow this guide. Please don't use your own method or a random app as that will most likely not help us. Use one of the following two methods:
#### Creating a logcat using the Android Debug Bridge (adb) on your PC
The Android Debug Bridge (adb) is a really useful tool to interface with your phone from a Terminal on your PC. In this case we will use it to create a logcat.
You will first have to enable USB Debugging on your phone:
- Enable Developer Options. You can do so by going to `Settings > About Phone` and tapping Build Number 7 times
- Now go to `Settings > System > Developer options` and enable Usb Debugging

Next you have to [download adb](https://developer.android.com/studio/releases/platform-tools) to your PC. 
- Extract the zip
- Open a command prompt in this directory. On Windows you can do so by holding shift and right clicking the folder and then pressing `Open Powershell here`

Now all that's left is to create the actual logcat:
- Run `.\adb shell logcat *:W > logcat.txt`. (Omit the `.\` if you're using Mac/Linux) Don't worry if this prints nothing, thats how it is supposed to be since we're redirecting all output into a text file
- Now do the steps necessary to cause your issue
- Finally, close your Terminal. Now you're done, your logcat can be found in the adb folder
#### Creating a logcat using Termux on your rooted Android
- Install Termux [from the Google Play Store](https://play.google.com/store/apps/details?id=com.termux)
- Open it and run the command `su` and accept the SuperUser prompt to grant Termux root
- Run `logcat *:W > /sdcard/logcat.txt`. Don't worry if this prints nothing, thats how it is supposed to be since we're redirecting all output into a text file
- Now do the steps necessary to cause your issue
- Finally, close Termux. Now you're done, your logcat can be found in the root of your sdcard (the location where you'll also find your Downloads, etc)

### Guide Contributors
- gghhkm
- Vendicated
