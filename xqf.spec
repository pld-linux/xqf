# 
# Conditional build:
%bcond_without	geoip	# without GeoIP
%bcond_with	gtk1	# use GTK+ 1.x instead of 2.x
#
Summary:	XQF - a GTK+ frontend to qstat
Summary(pl.UTF-8):	XQF - graficzny (oparty na GTK+) interfejs do qstat
Name:		xqf
Version:	1.0.5
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/xqf/%{name}-%{version}.tar.gz
# Source0-md5:	a88cecba6abb6349107ab135f1009946
Patch0:		%{name}-desktop.patch
URL:		http://www.linuxgames.com/xqf/
%{?with_geoip:BuildRequires:	GeoIP-devel}
BuildRequires:	automake
BuildRequires:	bzip2-devel
%{?with_gtk1:BuildRequires:	gdk-pixbuf-devel}
%{!?with_gtk1:BuildRequires:	gtk+2-devel >= 1:2.0.0}
%{?with_gtk1:BuildRequires:	gtk+-devel >= 1.2.0}
BuildRequires:	qstat >= 2.7
Requires:	qstat >= 2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xqf is QuakeWorld, Quake2, Quake3, Tribes2, etc. server browser and
launcher for Linux/X11. xqf is a GTK-based frontend to qstat.

%description -l pl.UTF-8
xqf jest przeglądarką serwerów i programem ułatwiającym uruchamianie 
QuakeWorld, Quake2, Quake3, Tribes2, itd. Jest opartym na GTK+
graficznym interfejsem dla qstat.

%prep
%setup -q
%patch0 -p1

%build
cp /usr/share/automake/config.sub .
%configure \
	--enable-bzip2 \
	%{!?with_gtk1:--enable-gtk2} \
	%{!?with_geoip:--disable-geoip} \
	%{?with_geoip:--enable-geoip}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog BUGS NEWS README TODO
%attr(755,root,root) %{_bindir}/xqf
%{_datadir}/xqf
%{_mandir}/man6/xqf.6*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
