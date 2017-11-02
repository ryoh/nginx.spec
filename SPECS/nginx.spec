%global         _hardened_build     1

%global         nginx_user          nginx
%global         nginx_group         nginx
%global         nginx_uid           996
%global         nginx_gid           996
%global         nginx_moddir        %{_libdir}/nginx/modules
%global         nginx_confdir       %{_sysconfdir}/nginx
%global         nginx_tempdir       %{_var}/cache/nginx
%global         nginx_logdir        %{_localstatedir}/log/nginx
%global         nginx_rundir        %{_rundir}
%global         nginx_lockdir       %{_localstatedir}/lock/subsys/nginx
%global         nginx_home          %{_datadir}/nginx
%global         nginx_webroot       %{nginx_home}/html
%global         nginx_client_tempdir   %{nginx_tempdir}/client_body_temp
%global         nginx_proxy_tempdir    %{nginx_tempdir}/proxy_temp
%global         nginx_fastcgi_tempdir  %{nginx_tempdir}/fastcgi_temp
%global         nginx_uwscgi_tempdir   %{nginx_tempdir}/uwscgi_temp
%global         nginx_scgi_tempdir     %{nginx_tempdir}/scgi_temp
%global         nginx_proxy_cachedir   %{nginx_tempdir}/proxy_cache
%global         nginx_fastcgi_cachedir %{nginx_tempdir}/fastcgi_cache
%global         nginx_uwscgi_cachedir  %{nginx_tempdir}/uwscgi_cache
%global         nginx_scgi_cachedir    %{nginx_tempdir}/scgi_cache

%global         pkg_name            nginx-mainline
%global         main_version        1.13.4
%global         main_release        1%{?dist}

%global         ssl_name            libressl
%global         ssl_version         2.5.5
%global         ssl_pkgname         %{ssl_name}-%{ssl_version}
%global         ssl_url             https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%{ssl_pkgname}.tar.gz


Name:           %{pkg_name}
Version:        %{main_version}
Release:        %{main_release}
Summary:        A high performance web server and reverse proxy
Group:          System Environment/Daemons 
License:        BSD
URL:            https://nginx.net

Source0:        https://nginx.org/download/nginx-%{main_version}.tar.gz
Source1:        https://nginx.org/download/nginx-%{main_version}.tar.gz.asc
Source10:       nginx.service
Source11:       nginx.sysconf
Source100:      https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%{ssl_pkgname}.tar.gz
Source101:      https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%{ssl_pkgname}.tar.gz.asc

Requires(pre):  shadow-utils
%systemd_requires
BuildRequires:  systemd

BuildRequires:  make gcc automake autoconf libtool
BuildRequires:  zlib-devel pcre-devel


%description
nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server,
and a generic TCP/UDP proxy server, originally written by Igor Sysoev.


%package mod-http-xslt
Summary:        nginx http xslt module
Requires:       %{name} = %{version}-%{release}
Requires:       libxml2 libxslt
BuildRequires:  libxml2-devel libxslt-devel

%description mod-http-xslt
%{summary}.


%package mod-http-perl
Summary:        nginx http perl module
Requires:       %{name} = %{version}-%{release}
BuildRequires:  perl(ExtUtils::Embed)

%description mod-http-perl
%{summary}.


%package mod-http-image-filter
Summary:        nginx http image filter module
Requires:       %{name} = %{version}-%{release}
Requires:       gd
BuildRequires:  gd-devel

%description mod-http-image-filter
%{summary}.


%package mod-http-geoip
Summary:        nginx http GeoIP module
Requires:       %{name} = %{version}-%{release}
Requires:       GeoIP
BuildRequires:  GeoIP-devel

%description mod-http-geoip
%{summary}.


%package mod-stream-geoip
Summary:        nginx stream GeoIP module
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-mod-stream = %{version}-%{release}
Requires:       GeoIP
BuildRequires:  GeoIP-devel

%description mod-stream-geoip
%{summary}.


%package mod-stream
Summary:        nginx stream module
Requires:       %{name} = %{version}-%{release}

%description mod-stream
%{summary}.


%package mod-mail	
Summary:        nginx mail module
Requires:       %{name} = %{version}-%{release}

%description mod-mail
%{summary}.


%prep
%setup -q -n nginx-%{version} -a 100


%build
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS} $(pcre-config --cflags)}"; export CFLAGS;
LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS} -Wl,-E}"; export LDFLAGS;

pushd %{ssl_pkgname}
./configure

%make_build
popd

./configure \
  --with-cc-opt="${CFLAGS}" \
  --with-ld-opt="${LDFLAGS}" \
  --with-openssl=./%{ssl_pkgname} \
  --prefix=%{nginx_home} \
  --sbin-path=%{_sbindir}/nginx \
  --modules-path=%{nginx_moddir} \
  --conf-path=%{nginx_confdir}/nginx.conf \
  --pid-path=%{nginx_rundir}/nginx.pid \
  --lock-path=%{nginx_lockdir} \
  --error-log-path=%{nginx_logdir}/error.log \
  --http-log-path=%{nginx_logdir}/access.log \
  --http-client-body-temp-path=%{nginx_client_tempdir} \
  --http-proxy-temp-path=%{nginx_proxy_tempdir} \
  --http-fastcgi-temp-path=%{nginx_fastcgi_tempdir} \
  --http-uwsgi-temp-path=%{nginx_uwscgi_tempdir} \
  --http-scgi-temp-path=%{nginx_scgi_tempdir} \
  --user=%{nginx_user} \
  --group=%{nginx_group} \
  --build=%{name}-%{version}-%{release} \
  --with-select_module \
  --with-poll_module \
  --with-threads \
  --with-file-aio \
  --with-compat \
  --with-pcre \
  --with-pcre-jit \
  --with-http_ssl_module \
  --with-http_v2_module \
  --with-http_realip_module \
  --with-http_addition_module \
  --with-http_sub_module \
  --with-http_dav_module \
  --with-http_flv_module \
  --with-http_mp4_module \
  --with-http_gunzip_module \
  --with-http_gzip_static_module \
  --with-http_auth_request_module \
  --with-http_random_index_module \
  --with-http_secure_link_module \
  --with-http_degradation_module \
  --with-http_slice_module \
  --with-http_stub_status_module \
  --with-http_xslt_module=dynamic \
  --with-http_image_filter_module=dynamic \
  --with-http_geoip_module=dynamic \
  --with-http_perl_module=dynamic \
  --with-mail=dynamic \
  --with-mail_ssl_module \
  --with-stream=dynamic \
  --with-stream_ssl_module \
  --with-stream_realip_module \
  --with-stream_geoip_module=dynamic \
  --with-stream_ssl_preread_module \

%make_build


%install
# Install
[[ -d %{buildroot} ]] && rm -rf "%{buildroot}"
%{__mkdir} -p "%{buildroot}"
%make_install INSTALLDIRS=vendor

find %{buildroot} -type f -name .packlist -exec rm -f '{}' \;
find %{buildroot} -type f -name perllocal.pod -exec rm -f '{}' \;
find %{buildroot} -type f -empty -exec rm -f '{}' \;
find %{buildroot} -type f -iname '*.so' -exec chmod 0755 '{}' \;

# Deleting unused files
%{__rm} -f %{buildroot}%{nginx_confdir}/fastcgi.conf
%{__rm} -f %{buildroot}%{nginx_confdir}/*.default

# Create temporary directories
%{__install} -p -d -m 0755 %{buildroot}%{nginx_rundir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_lockdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_client_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_proxy_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_fastcgi_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_uwscgi_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_scgi_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_proxy_cachedir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_fastcgi_cachedir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_uwscgi_cachedir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_scgi_cachedir}

# Add systemd service unit file
%{__install} -p -D -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/%{name}.service
%{__sed} -i \
  -e 's|${rundir}|%{_rundir}|g' \
  -e 's|${sbindir}|%{_sbindir}|g' \
  -e 's|${pkg_name}|%{name}|g' \
  %{buildroot}%{_unitdir}/%{name}.service

%{__install} -p -D -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%clean
%{__rm} -rf "%{buildroot}"

%pre
case $1 in
  1)
  : install
  getent group %{nginx_group} \
    || groupadd -r -g %{nginx_gid} %{nginx_group} \
    || groupadd -r %{nginx_group}

  getent passwd %{nginx_user} \
    || useradd -r -g %{nginx_group} -u %{nginx_uid} %{nginx_user} \
    || useradd -r -g %{nginx_group} %{nginx_user}
  ;;
  2)
  : update
  ;;
esac

%post
%systemd_post %{name}.service
case $1 in
  1)
  : install
  ;;
  2)
  : update
  ;;
esac

%preun
%systemd_pre %{name}.service
case $1 in
  0)
  : uninstall
  ;;
  1)
  : update
  ;;
esac

%postun
%systemd_postun %{name}.service
case $1 in
  0)
  : uninstall
  getent passwd %{nginx_user} \
    && userdel %{nginx_user} ||:

  getent group %{nginx_group} \
    && groupdell %{nginx_group} ||:
  ;;
  1)
  : update
  ;;
esac

%files
%defattr(-,root,root)
%{_sbindir}/nginx

%config(noreplace) %{nginx_confdir}/nginx.conf
%config(noreplace) %{nginx_confdir}/mime.types
%config(noreplace) %{nginx_confdir}/fastcgi_params
%config(noreplace) %{nginx_confdir}/scgi_params
%config(noreplace) %{nginx_confdir}/uwsgi_params
%config(noreplace) %{nginx_confdir}/koi-utf
%config(noreplace) %{nginx_confdir}/koi-win
%config(noreplace) %{nginx_confdir}/win-utf

%{_mandir}/man3/nginx.3pm.gz

%dir %{nginx_home}
%dir %{nginx_webroot}
%{nginx_webroot}/50x.html
%{nginx_webroot}/index.html

%{_unitdir}/%{name}.service
%{_sysconfdir}/sysconfig/%{name}

%dir %{nginx_rundir}
%dir %{nginx_lockdir}

%defattr(-,%{nginx_user},%{nginx_group})
%dir %{nginx_logdir}
%dir %{nginx_tempdir}
%dir %{nginx_client_tempdir}
%dir %{nginx_proxy_tempdir}
%dir %{nginx_fastcgi_tempdir}
%dir %{nginx_uwscgi_tempdir}
%dir %{nginx_scgi_tempdir}
%dir %{nginx_proxy_cachedir}
%dir %{nginx_fastcgi_cachedir}
%dir %{nginx_uwscgi_cachedir}
%dir %{nginx_scgi_cachedir}

%files mod-http-xslt
%{nginx_moddir}/ngx_http_xslt_filter_module.so

%files mod-http-perl
%{nginx_moddir}/ngx_http_perl_module.so
%dir %{perl_vendorarch}/auto/nginx
%{perl_vendorarch}/nginx.pm
%{perl_vendorarch}/auto/nginx/nginx.so

%files mod-http-image-filter
%{nginx_moddir}/ngx_http_image_filter_module.so

%files mod-http-geoip
%{nginx_moddir}/ngx_http_geoip_module.so

%files mod-stream-geoip
%{nginx_moddir}/ngx_stream_geoip_module.so

%files mod-stream
%{nginx_moddir}/ngx_stream_module.so

%files mod-mail
%{nginx_moddir}/ngx_mail_module.so


%changelog
* Fri Aug 18 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.4-1
- Create module packages.
* Sun Aug 13 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.4-1
- Bumpup 1.13.4-1
* Sun Aug 13 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.3-1
- Add Requires/BuildRequires
* Wed Jul 26 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.3-1
- first created
