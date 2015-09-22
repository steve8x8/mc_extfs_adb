There once (in the original development thread) was a precompiled busybox,
taken from CyanogenMod firmware.

This version of busybox had a bug: in case of permission problems with
link target, it prints error message on same line. adb+ script used this
bug to show error message as link content.

Since adb+ has been rewritten, this special busybox is no lomger necessary.
A preinstalled busybox is required though for proper functioning of the
list feature: "busybox ls" uses an output format that differs from that of "ls"
built into the Android firmware, and adb+ relies on this format.
