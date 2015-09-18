Precompiled busybox is taken from CyanogenMod firmware.

This version of busybox has bug: in case of permission problems with
link target, it prints error message on same line. adb+ script uses this
bug to show error message as link content.
