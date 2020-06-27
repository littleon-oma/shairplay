%define major	0
%define libname	%mklibname shairplay %major
%define devname	%mklibname shairplay -d

%define snap	20160101
%define rel	1

Summary:	Apple AirPlay server implementation
Name:		shairplay
Version:	0.9.0
Release:	%mkrel 0.git%snap.%rel
# library: LGPLv2+
# application: MIT
License:	MIT
Group:		Networking/Other
URL:		https://github.com/juhovh/shairplay

Source:		%name-%snap.tar.gz
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(avahi-compat-libdns_sd)
Requires:	%{libname} = %{version}-%{release}

%description
Server for the Apple RAOP protocol, emulating an AirPort Express for the
purpose of streaming music from iTunes and compatible iPods.

%package -n %libname
Summary:	Shared library of shairplay
Group:		System/Libraries

%description -n %libname
Shairplay is an Apple RAOP protocol server, emulating an AirPort Express
for the purpose of streaming music from iTunes and compatible iPods.

This package contains the library needed to run programs dynamically
linked with libshairplay.

%package -n %devname
Summary:	Headers for libshairplay development
Group:		Development/C
Requires:	%libname = %version
Provides:	shairplay-devel = %version-%release

%description -n %devname
Shairplay is an Apple RAOP protocol server.

This package contains the headers that are needed to compile
applications that use libshairplay.

%prep
%setup -q -n %name-%snap

%build
autoreconf -fi
%configure --disable-static
%make

%install
%make_install

find %{buildroot} -name '*.la' | xargs rm

%files
%doc README.md LICENSE
%{_bindir}/%{name}

%files -n %libname
%{_libdir}/*.so.%{major}{,.*}

%files -n %devname
%{_libdir}/*.so
%dir %{_includedir}/shairplay
%{_includedir}/shairplay/*.h


