adb+:

Adb+ is external file system for browsing and editing file system on
Android powered devices using Midnight Commander.

Usage: enter "cd adb://" or Alt-C and "adb://" to view remote file system.

Script will check for, and use an existing, busybox and will load 
the whole file system tree at first run, so first run will be slow
but susbsequent operations will be fast.

Supported operations are:

  * browsing;
  * copying of files in both directtions;
  * removing of files and directories;
  * viewing and editing of files;
  * execution of commands on remote file system.

Note: Don't forget to free VFS when you want to reread directory
contents using key combination "Ctrl-X a".

adbsu+:

Adbsu+ is the su-enabled sibling of adb+.
It tries to perform actions on the Android device using su 
(access has to be granted).
Exception: Writes use the normal "adb push" without su power.


Extfs:

Also, simple "extfs" virtual system is shipped along with this package.
It can be used to check output of other VFS modules.

Usage:

  * run a module with "list" command
    ./amodule list >out.extfs

  * cd into that file using command "cd out.extfs#extfs"/
