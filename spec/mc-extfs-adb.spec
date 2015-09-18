
%{!?svn_revision:%define svn_revision 1}

Name:           mc-extfs-adb
Version:        1.0.%{svn_revision}
Release:        1%{?dist}
Summary:        Browse android file system using Midnight Commander
Group:          System Environment/Base
License:        GPL
URL:            http://trac.assembla.com/bash-modules/
Source:         %{name}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       mc
Requires:       udev
Requires:       adb

# Turn of checking for binary files in noarch package,
# because busybox is compiled for ARM, while package
# can be installed on any host.
%define _binaries_in_noarch_packages_terminate_build   0

%description

External file system for browsing and editing file system on Android
powered devices using Midnight Commander.

Enter "cd #adb" or Alt-C and "#adb" to view remote file system.

Script will upload busybox and will load whole file system tree at first
run, so first run will be slow but susbsequent operations will be fast.

Note: Don't forget to free VFS using "Ctrl-X a" when you want to reload file
system tree.

%prep
%setup -n %{name}

%build

# Nothing to do

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"

cp -a src/* "$RPM_BUILD_ROOT/"

# Remove .svn directories, if any
find "$RPM_BUILD_ROOT/" -type d -name .svn | xargs -d '\n' rm -rf

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(0644,root,root,755)
%doc README.txt Changelog COPYING.GPLv2 README-busybox.txt

%attr(755,root,root) /usr/libexec/mc/extfs.d/adb+
%attr(755,root,root) /usr/libexec/mc/extfs.d/extfs

/usr/libexec/mc/extfs.d/busybox.armv5
