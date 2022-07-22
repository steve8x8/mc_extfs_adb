#!/usr/bin/env make -f

PACKAGE := mc-extfs-adb
VERSION := 0.20220722

all:	clean tgz deb

clean:
	rm -rf .build
	rm -f mc-extfs-adb*

tgz:
	git pull
	mkdir -p .build/$(PACKAGE)-$(VERSION)
	rsync -ax --exclude .build/ --exclude .git/ --exclude .gitignore \
	    --exclude patches/ --exclude tests/ --exclude tools/ \
	    . .build/$(PACKAGE)-$(VERSION)
	tar zcf $(PACKAGE)-$(VERSION).tar.gz -C .build $(PACKAGE)-$(VERSION)

deb:	clean tgz
	ln -f $(PACKAGE)-$(VERSION).tar.gz .build/$(PACKAGE)_$(VERSION).orig.tar.gz
	(cd .build/$(PACKAGE)-$(VERSION); dpkg-buildpackage -uc -us -tc -rfakeroot)
	mv .build/*.deb .

.PHONY:	all clean tgz deb
