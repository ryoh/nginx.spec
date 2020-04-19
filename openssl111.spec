%global soversion 1.1
%global _performance_build 1
%global _hardende_build    1

%define _prefix     /usr/local
%define _sysconfdir /usr/local/etc

Name:           openssl111
Version:        1.1.1f
Release:        1%{?dist}
Summary:        Utilities from the general purpose cryptography library with TLS implementation
License:        OpenSSL
URL:            https://www.openssl.org/
Source0:        https://www.openssl.org/source/openssl-%{version}.tar.gz
Source1:        https://www.openssl.org/source/openssl-%{version}.tar.gz.sha256
Source2:        https://www.openssl.org/source/openssl-%{version}.tar.gz.asc

BuildRequires:  coreutils, zlib-devel, gcc

Requires:       coreutils

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

%package devel
Summary: Files for development of applications which will use OpenSSL
Requires: pkgconfig

%description devel
OpenSSL is a toolkit for supporting cryptography. The openssl-devel
package contains include files needed to develop applications which
support various cryptographic algorithms and protocols.

%prep
%setup -q -n openssl-%{version}


%build
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" ; export CFLAGS ; 
CXXFLAGS="${CXXFLAGS:-${RPM_OPT_FLAGS}}" ; export CXXFLAGS ;
LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"; export LDFLAGS;

sslarch=%{_os}-%{_target_cpu}
sslflags=enable-ec_nistp_64_gcc_128

%enable_devtoolset9

./config \
  --prefix=%{_prefix} --openssldir=%{_sysconfdir}/pki/tls \
  ${sslflags} zlib \
  no-ssl2 no-ssl3 no-comp \
  shared \

%make_build


%install
[[ "%{buildroot}" != "/" ]] && [[ -d "%{buildroot}" ]] && rm -rf %{buildroot}
%make_install

rm -f %{buildroot}%{_sysconfdir}/pki/tls/*.dist
rm -f %{buildroot}%{_libdir}/*.a


%files
%doc
%{_bindir}/openssl
%{_bindir}/c_rehash
%{_libdir}/libcrypto.so
%{_libdir}/libcrypto.so.1.1
%{_libdir}/libssl.so
%{_libdir}/libssl.so.1.1
%{_libdir}/engines-1.1/afalg.so
%{_libdir}/engines-1.1/capi.so
%{_libdir}/engines-1.1/padlock.so
%{_sysconfdir}/pki/tls/ct_log_list.cnf
%{_sysconfdir}/pki/tls/misc/CA.pl
%{_sysconfdir}/pki/tls/misc/tsget
%{_sysconfdir}/pki/tls/misc/tsget.pl
%{_sysconfdir}/pki/tls/openssl.cnf
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_defaultdocdir}/openssl/html


%files devel
%{_includedir}/openssl/*.h
%{_libdir}/pkgconfig/*.pc


%changelog
