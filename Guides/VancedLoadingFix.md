# Vanced stuck loading / Music unable to login

This is a bug with microg. Simply follow the following steps to fix it.

A video recording of me doing them can be found attached below if you find it easier to follow that!

## Why is this happening?

Vanced uses microg to connect to your google account. Without microg you wouldn't be able to login (and Vanced would not even load).

If you are using the normal Youtube this would be managed by Google Play Services but since it uses a whitelist, Vanced nonroot can't use it!

While we do have [our own version of microg](https://github.com/YTVanced/VancedMicrog) that is much smaller than the original microg, microg is made by another developer unrelated to Vanced, so we have to wait for him to fix this issue!

If you would like to learn more, you can check the [bug report issue](https://github.com/microg/GmsCore/issues/1373) that I opened in the microg repo

## Solution

If you are fixing Vanced Music, do these steps with Music instead of Vanced

1) Open Vanced Manager
2) Uninstall Vanced and microg
3) Open Vanced Manager settings and click clear downloaded files
4) Install microg
5) Click on Vanced, select version and choose anything but the latest version
6) Confirm and install it
7) Open Vanced and login
8) Head back to Vanced Manager and update Vanced to the latest version

<!-- TODO -->Video Coming soon
