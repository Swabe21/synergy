# Makefile.in generated by automake 1.6.3 from Makefile.am.
# lib/arch/Makefile.  Generated from Makefile.in by configure.

# Copyright 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002
# Free Software Foundation, Inc.
# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.



# synergy -- mouse and keyboard sharing utility
# Copyright (C) 2002 Chris Schoeneman
# 
# This package is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# found in the file COPYING that should have accompanied this file.
# 
# This package is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
SHELL = /bin/sh

srcdir = .
top_srcdir = ../..

prefix = /usr/local
exec_prefix = ${prefix}

bindir = ${exec_prefix}/bin
sbindir = ${exec_prefix}/sbin
libexecdir = ${exec_prefix}/libexec
datadir = ${prefix}/share
sysconfdir = ${prefix}/etc
sharedstatedir = ${prefix}/com
localstatedir = ${prefix}/var
libdir = ${exec_prefix}/lib
infodir = ${prefix}/info
mandir = ${prefix}/man
includedir = ${prefix}/include
oldincludedir = /usr/include
pkgdatadir = $(datadir)/synergy
pkglibdir = $(libdir)/synergy
pkgincludedir = $(includedir)/synergy
top_builddir = ../..

ACLOCAL = ${SHELL} /home/matthew/synergy/config/missing --run aclocal-1.6
AUTOCONF = ${SHELL} /home/matthew/synergy/config/missing --run autoconf
AUTOMAKE = ${SHELL} /home/matthew/synergy/config/missing --run automake-1.6
AUTOHEADER = ${SHELL} /home/matthew/synergy/config/missing --run autoheader

am__cd = CDPATH="$${ZSH_VERSION+.}$(PATH_SEPARATOR)" && cd
INSTALL = /usr/bin/ginstall -c
INSTALL_PROGRAM = ${INSTALL}
INSTALL_DATA = ${INSTALL} -m 644
install_sh_DATA = $(install_sh) -c -m 644
install_sh_PROGRAM = $(install_sh) -c
install_sh_SCRIPT = $(install_sh) -c
INSTALL_SCRIPT = ${INSTALL}
INSTALL_HEADER = $(INSTALL_DATA)
transform = s,x,x,
NORMAL_INSTALL = :
PRE_INSTALL = :
POST_INSTALL = :
NORMAL_UNINSTALL = :
PRE_UNINSTALL = :
POST_UNINSTALL = :
host_alias = 
host_triplet = x86_64-unknown-linux

EXEEXT = 
OBJEXT = o
PATH_SEPARATOR = :
AMTAR = ${SHELL} /home/matthew/synergy/config/missing --run tar
AWK = gawk
CC = gcc
CXX = g++
DEPDIR = .deps
HAVE_DOT = NO
INET_ATON_LIBS = 
INSTALL_STRIP_PROGRAM = ${SHELL} $(install_sh) -c -s
NANOSLEEP_LIBS = 
OBJC = gcc
OBJCFLAGS = -g -O2
PACKAGE = synergy
PTHREAD_CC = gcc
PTHREAD_CFLAGS = -pthread
PTHREAD_LIBS = 
RANLIB = ranlib
STRIP = 
VERSION = 1.3.1
X_CFLAGS = 
X_EXTRA_LIBS = 
X_LIBS =  -L/usr/lib64
X_PRE_LIBS =  -lSM -lICE
acx_pthread_config = 
am__include = include
am__quote = 
install_sh = /home/matthew/synergy/config/install-sh

NULL = 

COMMON_SOURCE_FILES = \
	CArch.cpp					\
	CArchDaemonNone.cpp			\
	CArchDaemonNone.h			\
	XArch.cpp					\
	CArch.h						\
	IArchConsole.h				\
	IArchDaemon.h				\
	IArchFile.h					\
	IArchLog.h					\
	IArchMultithread.h			\
	IArchNetwork.h				\
	IArchSleep.h				\
	IArchString.h				\
	IArchSystem.h				\
	IArchTaskBar.h				\
	IArchTaskBarReceiver.h		\
	IArchTime.h					\
	XArch.h						\
	$(NULL)

UNIX_SOURCE_FILES = \
	CArchConsoleUnix.cpp		\
	CArchDaemonUnix.cpp			\
	CArchFileUnix.cpp			\
	CArchLogUnix.cpp			\
	CArchMultithreadPosix.cpp	\
	CArchNetworkBSD.cpp			\
	CArchSleepUnix.cpp			\
	CArchStringUnix.cpp			\
	CArchSystemUnix.cpp			\
	CArchTaskBarXWindows.cpp	\
	CArchTimeUnix.cpp			\
	XArchUnix.cpp				\
	CArchConsoleUnix.h			\
	CArchDaemonUnix.h			\
	CArchFileUnix.h				\
	CArchLogUnix.h				\
	CArchMultithreadPosix.h		\
	CArchNetworkBSD.h			\
	CArchSleepUnix.h			\
	CArchStringUnix.h			\
	CArchSystemUnix.h			\
	CArchTaskBarXWindows.h		\
	CArchTimeUnix.h				\
	XArchUnix.h					\
	$(NULL)

WIN32_SOURCE_FILES = \
	CArchConsoleWindows.cpp		\
	CArchDaemonWindows.cpp		\
	CArchFileWindows.cpp		\
	CArchLogWindows.cpp			\
	CArchMiscWindows.cpp		\
	CArchMultithreadWindows.cpp	\
	CArchNetworkWinsock.cpp		\
	CArchSleepWindows.cpp		\
	CArchStringWindows.cpp		\
	CArchSystemWindows.cpp		\
	CArchTaskBarWindows.cpp		\
	CArchTimeWindows.cpp		\
	XArchWindows.cpp			\
	CArchConsoleWindows.h		\
	CArchDaemonWindows.h		\
	CArchFileWindows.h			\
	CArchLogWindows.h			\
	CArchMiscWindows.h			\
	CArchMultithreadWindows.h	\
	CArchNetworkWinsock.h		\
	CArchSleepWindows.h			\
	CArchStringWindows.h		\
	CArchSystemWindows.h		\
	CArchTaskBarWindows.h		\
	CArchTimeWindows.h			\
	XArchWindows.h				\
	$(NULL)


EXTRA_DIST = \
	arch.dsp					\
	CMultibyte.cpp				\
	vsnprintf.cpp				\
	$(UNIX_SOURCE_FILES)		\
	$(WIN32_SOURCE_FILES)		\
	$(NULL)


MAINTAINERCLEANFILES = \
	Makefile.in					\
	$(NULL)


noinst_LIBRARIES = libarch.a
libarch_a_SOURCES = \
	$(COMMON_SOURCE_FILES)		\
	$(UNIX_SOURCE_FILES)		\
	$(NULL)

#libarch_a_SOURCES = \
#	$(COMMON_SOURCE_FILES)		\
#	$(WIN32_SOURCE_FILES)		\
#	$(NULL)

INCLUDES = \
	-I$(top_srcdir)/lib/common	\
	$(NULL)

subdir = lib/arch
mkinstalldirs = $(SHELL) $(top_srcdir)/config/mkinstalldirs
CONFIG_HEADER = $(top_builddir)/config.h
CONFIG_CLEAN_FILES =
LIBRARIES = $(noinst_LIBRARIES)

libarch_a_AR = $(AR) cru
libarch_a_LIBADD =
am__objects_1 =
am__objects_2 = CArch.$(OBJEXT) CArchDaemonNone.$(OBJEXT) \
	XArch.$(OBJEXT) $(am__objects_1)
am__objects_3 = CArchConsoleUnix.$(OBJEXT) CArchDaemonUnix.$(OBJEXT) \
	CArchFileUnix.$(OBJEXT) CArchLogUnix.$(OBJEXT) \
	CArchMultithreadPosix.$(OBJEXT) CArchNetworkBSD.$(OBJEXT) \
	CArchSleepUnix.$(OBJEXT) CArchStringUnix.$(OBJEXT) \
	CArchSystemUnix.$(OBJEXT) CArchTaskBarXWindows.$(OBJEXT) \
	CArchTimeUnix.$(OBJEXT) XArchUnix.$(OBJEXT) $(am__objects_1)
am__objects_4 = CArchConsoleWindows.$(OBJEXT) \
	CArchDaemonWindows.$(OBJEXT) CArchFileWindows.$(OBJEXT) \
	CArchLogWindows.$(OBJEXT) CArchMiscWindows.$(OBJEXT) \
	CArchMultithreadWindows.$(OBJEXT) CArchNetworkWinsock.$(OBJEXT) \
	CArchSleepWindows.$(OBJEXT) CArchStringWindows.$(OBJEXT) \
	CArchSystemWindows.$(OBJEXT) CArchTaskBarWindows.$(OBJEXT) \
	CArchTimeWindows.$(OBJEXT) XArchWindows.$(OBJEXT) \
	$(am__objects_1)
am_libarch_a_OBJECTS = $(am__objects_2) $(am__objects_3) \
	$(am__objects_1)
#am_libarch_a_OBJECTS = $(am__objects_2) $(am__objects_4) \
#	$(am__objects_1)
libarch_a_OBJECTS = $(am_libarch_a_OBJECTS)

DEFS = -DHAVE_CONFIG_H
DEFAULT_INCLUDES =  -I. -I$(srcdir) -I$(top_builddir)
CPPFLAGS = 
LDFLAGS = 
LIBS =    -L/usr/lib64  -lSM -lICE  -lXtst -lXinerama  -lXext -lX11    
depcomp = $(SHELL) $(top_srcdir)/config/depcomp
am__depfiles_maybe = depfiles
DEP_FILES = ./$(DEPDIR)/CArch.Po \
	./$(DEPDIR)/CArchConsoleUnix.Po \
	./$(DEPDIR)/CArchConsoleWindows.Po \
	./$(DEPDIR)/CArchDaemonNone.Po \
	./$(DEPDIR)/CArchDaemonUnix.Po \
	./$(DEPDIR)/CArchDaemonWindows.Po \
	./$(DEPDIR)/CArchFileUnix.Po \
	./$(DEPDIR)/CArchFileWindows.Po \
	./$(DEPDIR)/CArchLogUnix.Po \
	./$(DEPDIR)/CArchLogWindows.Po \
	./$(DEPDIR)/CArchMiscWindows.Po \
	./$(DEPDIR)/CArchMultithreadPosix.Po \
	./$(DEPDIR)/CArchMultithreadWindows.Po \
	./$(DEPDIR)/CArchNetworkBSD.Po \
	./$(DEPDIR)/CArchNetworkWinsock.Po \
	./$(DEPDIR)/CArchSleepUnix.Po \
	./$(DEPDIR)/CArchSleepWindows.Po \
	./$(DEPDIR)/CArchStringUnix.Po \
	./$(DEPDIR)/CArchStringWindows.Po \
	./$(DEPDIR)/CArchSystemUnix.Po \
	./$(DEPDIR)/CArchSystemWindows.Po \
	./$(DEPDIR)/CArchTaskBarWindows.Po \
	./$(DEPDIR)/CArchTaskBarXWindows.Po \
	./$(DEPDIR)/CArchTimeUnix.Po \
	./$(DEPDIR)/CArchTimeWindows.Po \
	./$(DEPDIR)/XArch.Po ./$(DEPDIR)/XArchUnix.Po \
	./$(DEPDIR)/XArchWindows.Po
CXXCOMPILE = $(CXX) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) \
	$(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CXXFLAGS) $(CXXFLAGS)
CXXLD = $(CXX)
CXXLINK = $(CXXLD) $(AM_CXXFLAGS) $(CXXFLAGS) $(AM_LDFLAGS) $(LDFLAGS) \
	-o $@
CXXFLAGS = -g -O2 -g -Wall -Wno-unknown-pragmas -Werror   -DSYSAPI_UNIX=1 -DWINAPI_XWINDOWS=1 -pthread 
CFLAGS = -g -O2
COMPILE = $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) \
	$(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS)
CCLD = $(CC)
LINK = $(CCLD) $(AM_CFLAGS) $(CFLAGS) $(AM_LDFLAGS) $(LDFLAGS) -o $@
DIST_SOURCES = $(libarch_a_SOURCES)
DIST_COMMON = Makefile.am Makefile.in
SOURCES = $(libarch_a_SOURCES)

all: all-am

.SUFFIXES:
.SUFFIXES: .cpp .o .obj
$(srcdir)/Makefile.in:  Makefile.am  $(top_srcdir)/configure.in $(ACLOCAL_M4)
	cd $(top_srcdir) && \
	  $(AUTOMAKE) --gnu  lib/arch/Makefile
Makefile:  $(srcdir)/Makefile.in  $(top_builddir)/config.status
	cd $(top_builddir) && $(SHELL) ./config.status $(subdir)/$@ $(am__depfiles_maybe)

AR = ar

clean-noinstLIBRARIES:
	-test -z "$(noinst_LIBRARIES)" || rm -f $(noinst_LIBRARIES)
libarch.a: $(libarch_a_OBJECTS) $(libarch_a_DEPENDENCIES) 
	-rm -f libarch.a
	$(libarch_a_AR) libarch.a $(libarch_a_OBJECTS) $(libarch_a_LIBADD)
	$(RANLIB) libarch.a

mostlyclean-compile:
	-rm -f *.$(OBJEXT) core *.core

distclean-compile:
	-rm -f *.tab.c

include ./$(DEPDIR)/CArch.Po
include ./$(DEPDIR)/CArchConsoleUnix.Po
include ./$(DEPDIR)/CArchConsoleWindows.Po
include ./$(DEPDIR)/CArchDaemonNone.Po
include ./$(DEPDIR)/CArchDaemonUnix.Po
include ./$(DEPDIR)/CArchDaemonWindows.Po
include ./$(DEPDIR)/CArchFileUnix.Po
include ./$(DEPDIR)/CArchFileWindows.Po
include ./$(DEPDIR)/CArchLogUnix.Po
include ./$(DEPDIR)/CArchLogWindows.Po
include ./$(DEPDIR)/CArchMiscWindows.Po
include ./$(DEPDIR)/CArchMultithreadPosix.Po
include ./$(DEPDIR)/CArchMultithreadWindows.Po
include ./$(DEPDIR)/CArchNetworkBSD.Po
include ./$(DEPDIR)/CArchNetworkWinsock.Po
include ./$(DEPDIR)/CArchSleepUnix.Po
include ./$(DEPDIR)/CArchSleepWindows.Po
include ./$(DEPDIR)/CArchStringUnix.Po
include ./$(DEPDIR)/CArchStringWindows.Po
include ./$(DEPDIR)/CArchSystemUnix.Po
include ./$(DEPDIR)/CArchSystemWindows.Po
include ./$(DEPDIR)/CArchTaskBarWindows.Po
include ./$(DEPDIR)/CArchTaskBarXWindows.Po
include ./$(DEPDIR)/CArchTimeUnix.Po
include ./$(DEPDIR)/CArchTimeWindows.Po
include ./$(DEPDIR)/XArch.Po
include ./$(DEPDIR)/XArchUnix.Po
include ./$(DEPDIR)/XArchWindows.Po

distclean-depend:
	-rm -rf ./$(DEPDIR)

.cpp.o:
	source='$<' object='$@' libtool=no \
	depfile='$(DEPDIR)/$*.Po' tmpdepfile='$(DEPDIR)/$*.TPo' \
	$(CXXDEPMODE) $(depcomp) \
	$(CXXCOMPILE) -c -o $@ `test -f '$<' || echo '$(srcdir)/'`$<

.cpp.obj:
	source='$<' object='$@' libtool=no \
	depfile='$(DEPDIR)/$*.Po' tmpdepfile='$(DEPDIR)/$*.TPo' \
	$(CXXDEPMODE) $(depcomp) \
	$(CXXCOMPILE) -c -o $@ `cygpath -w $<`
CXXDEPMODE = FOO=5 depmode=gcc3
uninstall-info-am:

ETAGS = etags
ETAGSFLAGS =

tags: TAGS

ID: $(HEADERS) $(SOURCES) $(LISP) $(TAGS_FILES)
	list='$(SOURCES) $(HEADERS) $(LISP) $(TAGS_FILES)'; \
	unique=`for i in $$list; do \
	    if test -f "$$i"; then echo $$i; else echo $(srcdir)/$$i; fi; \
	  done | \
	  $(AWK) '    { files[$$0] = 1; } \
	       END { for (i in files) print i; }'`; \
	mkid -fID $$unique

TAGS:  $(HEADERS) $(SOURCES)  $(TAGS_DEPENDENCIES) \
		$(TAGS_FILES) $(LISP)
	tags=; \
	here=`pwd`; \
	list='$(SOURCES) $(HEADERS)  $(LISP) $(TAGS_FILES)'; \
	unique=`for i in $$list; do \
	    if test -f "$$i"; then echo $$i; else echo $(srcdir)/$$i; fi; \
	  done | \
	  $(AWK) '    { files[$$0] = 1; } \
	       END { for (i in files) print i; }'`; \
	test -z "$(ETAGS_ARGS)$$tags$$unique" \
	  || $(ETAGS) $(ETAGSFLAGS) $(AM_ETAGSFLAGS) $(ETAGS_ARGS) \
	     $$tags $$unique

GTAGS:
	here=`$(am__cd) $(top_builddir) && pwd` \
	  && cd $(top_srcdir) \
	  && gtags -i $(GTAGS_ARGS) $$here

distclean-tags:
	-rm -f TAGS ID GTAGS GRTAGS GSYMS GPATH
DISTFILES = $(DIST_COMMON) $(DIST_SOURCES) $(TEXINFOS) $(EXTRA_DIST)

top_distdir = ../..
distdir = $(top_distdir)/$(PACKAGE)-$(VERSION)

distdir: $(DISTFILES)
	@list='$(DISTFILES)'; for file in $$list; do \
	  if test -f $$file || test -d $$file; then d=.; else d=$(srcdir); fi; \
	  dir=`echo "$$file" | sed -e 's,/[^/]*$$,,'`; \
	  if test "$$dir" != "$$file" && test "$$dir" != "."; then \
	    dir="/$$dir"; \
	    $(mkinstalldirs) "$(distdir)$$dir"; \
	  else \
	    dir=''; \
	  fi; \
	  if test -d $$d/$$file; then \
	    if test -d $(srcdir)/$$file && test $$d != $(srcdir); then \
	      cp -pR $(srcdir)/$$file $(distdir)$$dir || exit 1; \
	    fi; \
	    cp -pR $$d/$$file $(distdir)$$dir || exit 1; \
	  else \
	    test -f $(distdir)/$$file \
	    || cp -p $$d/$$file $(distdir)/$$file \
	    || exit 1; \
	  fi; \
	done
check-am: all-am
check: check-am
all-am: Makefile $(LIBRARIES)

installdirs:

install: install-am
install-exec: install-exec-am
install-data: install-data-am
uninstall: uninstall-am

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am

installcheck: installcheck-am
install-strip:
	$(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	  INSTALL_STRIP_FLAG=-s \
	  `test -z '$(STRIP)' || \
	    echo "INSTALL_PROGRAM_ENV=STRIPPROG='$(STRIP)'"` install
mostlyclean-generic:

clean-generic:

distclean-generic:
	-rm -f Makefile $(CONFIG_CLEAN_FILES)

maintainer-clean-generic:
	@echo "This command is intended for maintainers to use"
	@echo "it deletes files that may require special tools to rebuild."
	-test -z "$(MAINTAINERCLEANFILES)" || rm -f $(MAINTAINERCLEANFILES)
clean: clean-am

clean-am: clean-generic clean-noinstLIBRARIES mostlyclean-am

distclean: distclean-am

distclean-am: clean-am distclean-compile distclean-depend \
	distclean-generic distclean-tags

dvi: dvi-am

dvi-am:

info: info-am

info-am:

install-data-am:

install-exec-am:

install-info: install-info-am

install-man:

installcheck-am:

maintainer-clean: maintainer-clean-am

maintainer-clean-am: distclean-am maintainer-clean-generic

mostlyclean: mostlyclean-am

mostlyclean-am: mostlyclean-compile mostlyclean-generic

uninstall-am: uninstall-info-am

.PHONY: GTAGS all all-am check check-am clean clean-generic \
	clean-noinstLIBRARIES distclean distclean-compile \
	distclean-depend distclean-generic distclean-tags distdir dvi \
	dvi-am info info-am install install-am install-data \
	install-data-am install-exec install-exec-am install-info \
	install-info-am install-man install-strip installcheck \
	installcheck-am installdirs maintainer-clean \
	maintainer-clean-generic mostlyclean mostlyclean-compile \
	mostlyclean-generic tags uninstall uninstall-am \
	uninstall-info-am

# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
