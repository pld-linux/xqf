# Conditional build:
%bcond_without	geoip
%bcond_without	gtk2
#

Summary:	XQF
Name:		xqf
Version:	0.9.14
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	bzip2-devel
BuildRequires:	qstat >= 2.5b
%{?with_geoip:BuildRequires:	GeoIP-devel}
%{!?with_gtk2:BuildRequires:	gtk+-devel >= 1.2.0}
%{!?with_gtk2:BuildRequires:	gdk-pixbuf-devel}
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2.0.0}
Requires:	qstat >= 2.5b
URL:		http://www.linuxgames.com/xqf/

%define		_prefix	/usr

%description
XQF is QuakeWorld, Quake2, Quake3, Tribes2, etc. server browser and
launcher for Linux/X11. It uses the GTK toolkit. XQF is a frontend to
QStat.

%prep

%setup -q
%patch -p1

%build
%configure \
    --enable-bzip2 \
    %{?with_gtk2:--enable-gtk2} \
    %{!?with_geoip:--disable-geoip} \
    %{?with_geoip:--enable-geoip}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS BUGS ChangeLog NEWS TODO
%attr(0755,root,root)%{_bindir}/xqf
%{_datadir}/xqf/
%{_mandir}/man6/xqf.6.gz
%{_desktopdir}/*
%{_pixmapsdir}/*
