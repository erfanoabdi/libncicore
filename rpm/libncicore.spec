Name: libncicore
Version: 1.1.17
Release: 0
Summary: NCI state machine
License: BSD
URL: https://github.com/mer-hybris/libncicore
Source: %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libglibutil) >= 1.0.29
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
NFC NCI state machine implementation

%package devel
Summary: Development library for %{name}
Requires: %{name} = %{version}
Requires: pkgconfig

%description devel
This package contains the development library for %{name}.

%prep
%setup -q

%build
make LIBDIR=%{_libdir} KEEP_SYMBOLS=1 release pkgconfig

%install
rm -rf %{buildroot}
make LIBDIR=%{_libdir} DESTDIR=%{buildroot} install-dev

%check
make test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%{_includedir}/ncicore/*.h
