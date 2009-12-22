Summary:   Mouse and keyboard sharing utility
Name:      synergy
Version:   1.3.1
Release:   1
License:   GPL
Packager:  Chris Schoeneman <crs23@users.sourceforge.net>
Group:     System Environment/Daemons
Prefixes:  /usr/bin
Source:    synergy-1.3.1.tar.gz
Buildroot: /var/tmp/synergy-1.3.1-root

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its
own display, without special hardware.  It's intended for users
with multiple computers on their desk since each system uses its
own display.

%prep
%setup
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr

%build
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/bin/synergyc
strip $RPM_BUILD_ROOT/usr/bin/synergys

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/bin/synergyc
/usr/bin/synergys
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc INSTALL
%doc NEWS
%doc README
%doc doc/about.html
%doc doc/authors.html
%doc doc/autostart.html
%doc doc/banner.html
%doc doc/border.html
%doc doc/compiling.html
%doc doc/configuration.html
%doc doc/contact.html
%doc doc/developer.html
%doc doc/faq.html
%doc doc/history.html
%doc doc/home.html
%doc doc/index.html
%doc doc/license.html
%doc doc/news.html
%doc doc/roadmap.html
%doc doc/running.html
%doc doc/security.html
%doc doc/tips.html
%doc doc/toc.html
%doc doc/trouble.html
%doc doc/synergy.css
%doc examples/synergy.conf
