Summary:	SimpleBurn is a basic burning tool for CDs and DVDs
Name:		simpleburn
Version:	1.6.4
Release:	1
Group:		Archiving/Cd burning
License:	CeCILL
URL:		http://simpleburn.tuxfamily.org/
Source0:	http://simpleburn.tuxfamily.org/IMG/bz2/%{name}-%{version}.tar.bz2
Patch0:		simpleburn-1.6.4_desktop.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(gtk+-2.0)

Requires:	cdrkit
Requires:	vorbis-tools
Requires:	mpg123
Requires:	normalize

%description
SimpleBurn is a basic burning application for CDs and DVDs.

%prep
%setup -q
%apply_patches

%build
export CFLAGS="$CFLAGS -lm"
%cmake \
	-DDETECTION=UDEV \
	-DBURNING=CDRTOOLS

%make

%install
%makeinstall_std -C build
rm -rf %{buildroot}/usr/doc/

%find_lang %{name}

%files -f %{name}.lang
%doc doc/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}*
%{_datadir}/pixmaps/*.png



%changelog
* Sun May 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.6.4-1
+ Revision: 800832
- imported package simpleburn

