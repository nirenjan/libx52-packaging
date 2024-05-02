Name:           libx52
Version:        0.3.0
Release:        1%{?dist}
Summary:        Saitek X52/X52pro drivers & controller mapping software for Linux

License:        GPLv2
URL:            https://nirenjan.github.io/libx52
Source0:        https://github.com/nirenjan/libx52/releases/download/v%{version}/%{name}_%{version}.orig.tar.gz

BuildRequires:  hidapi-devel libusb1-devel libevdev-devel
BuildRequires:  autoconf automake gettext-devel findutils libtool pkg-config python3
BuildRequires:  systemd-rpm-macros
Requires:       hidapi libusb1 libevdev gettext

%description
libx52 is a user-space driver for the Saitek/MadCatz X52 Pro flight control
system. The X52 pro is a HOTAS (hand on throttle and stick) with 7 axes, 39
buttons, 1 hat and 1 thumbstick and a multi-function display which is
programmable.

While the joystick itself is detected on recent Linux kernels, the LED and
MFD functionality must be handled through this package.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%configure --disable-static --disable-Werror
%make_build

%check
make -C %{_builddir}/%{name}-%{version} check

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%{?ldconfig_scriptlets}


%files
%license LICENSE
%{_sysconfdir}/x52d/x52d.conf
%{_bindir}/
%{_libdir}/*.so.*
%{_unitdir}/x52d.service
%{_udevrulesdir}/
%{_datadir}/doc/%{name}/
%{_mandir}/man1/

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/

%exclude
%{_datadir}/locale/xx_PL/

%changelog
* Thu May 02 2024 nirenjan <nirenjan@gmail.com>
- 
