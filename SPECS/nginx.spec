%define         _hardened_build     1

%define         nginx_user          nginx
%define         nginx_group         nginx
%define         nginx_uid           996
%define         nginx_gid           996
%define         nginx_home          %{_datadir}/nginx
%define         nginx_moddir        %{_libdir}/nginx/modules
%define         nginx_confdir       %{_sysconfdir}/nginx
%define         nginx_tempdir       %{_sharedstatedir}/nginx
%define         nginx_logdir        %{_localstatedir}/log/nginx
%define         nginx_rundir        %{_localstatedir}/run
%define         nginx_lockdir       %{_localstatedir}/lock/subsys
%define         nginx_webroot       %{nginx_home}/html

%define         pkg_name            nginx
%define         main_version        1.13.3
%define         main_release        1%{?dist}

%define         ssl_name            libressl
%define         ssl_version         2.5.5
%define         ssl_pkgname         %{ssl_name}-%{ssl_version}
%define         ssl_url             https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%{ssl_pkgname}.tar.gz


Name:           %{pkg_name}
Version:        %{main_version}
Release:        %{main_release}
Summary:        A high performance web server and reverse
Group:          System Environment/Daemons 
License:        BSD
URL:            https://nginx.net

Source0:        https://nginx.org/download/%{pkg_name}-%{main_version}.tar.gz
Source1:        https://nginx.org/download/%{pkg_name}-%{main_version}.tar.gz.asc
Source100:      https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%{ssl_pkgname}.tar.gz
Source101:      https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%{ssl_pkgname}.tar.gz.asc


%description
%{summary}.


%prep
%setup -q -a 100


%build
CFLAGS="${CFLAGS:-%{optflags} $(pcre-config --cflags)}"; export CFLAGS;
LDFLAGS="${LDFLAGS:-$RPM_LD_FLAGS -Wl,-E}"; export LDFLAGS;

pushd %{ssl_pkgname}
./configure

%{make_build}
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
  --lock-path=%{nginx_lockdir}/nginx \
  --error-log-path=%{nginx_logdir}/error.log \
  --http-log-path=%{nginx_logdir}/access.log \
  --http-client-body-temp-path=%{nginx_tempdir}/client_body \
  --http-proxy-temp-path=%{nginx_tempdir}/proxy \
  --http-fastcgi-temp-path=%{nginx_tempdir}/fastcgi \
  --http-uwsgi-temp-path=%{nginx_tempdir}/uwsgi \
  --http-scgi-temp-path=%{nginx_tempdir}/scgi \
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

%{make_build}


%install
# Install
[[ -d %{buildroot} ]] && rm -rf "%{buildroot}"
%{__mkdir} -p "%{buildroot}"
%{__make} install DESTDIR=%{buildroot} INSTALLDIRS=vendor

find %{buildroot} -type f -name .packlist -exec rm -f '{}' \;
find %{buildroot} -type f -name perllocal.pod -exec rm -f '{}' \;
find %{buildroot} -type f -empty -exec rm -f '{}' \;
find %{buildroot} -type f -iname '*.so' -exec chmod 0755 '{}' \;

# Deleting unused files
%{__rm} -f %{buildroot}%{nginx_confdir}/fastcgi.conf
%{__rm} -f %{buildroot}%{nginx_confdir}/*.default

# Create nginx temporary directories
install -p -d -m 0700 %{buildroot}%{nginx_home}
install -p -d -m 0700 %{buildroot}%{nginx_tempdir}
install -p -d -m 0700 %{buildroot}%{nginx_tempdir}/client_body
install -p -d -m 0700 %{buildroot}%{nginx_tempdir}/proxy
install -p -d -m 0700 %{buildroot}%{nginx_tempdir}/fastcgi
install -p -d -m 0700 %{buildroot}%{nginx_tempdir}/uwsgi
install -p -d -m 0700 %{buildroot}%{nginx_tempdir}/scgi

%clean
#%{__rm} -rf "%{buildroot}"


%files
%{_sbindir}/nginx

%{nginx_confdir}/nginx.conf
%{nginx_confdir}/mime.types
%{nginx_confdir}/fastcgi_params
%{nginx_confdir}/scgi_params
%{nginx_confdir}/uwsgi_params
%{nginx_confdir}/koi-utf
%{nginx_confdir}/koi-win
%{nginx_confdir}/win-utf

%{_mandir}/man3/nginx.3pm.gz

%dir %{nginx_home}
%dir %{nginx_webroot}
%{nginx_webroot}/50x.html
%{nginx_webroot}/index.html

%{nginx_moddir}/ngx_http_geoip_module.so
%{nginx_moddir}/ngx_http_image_filter_module.so
%{nginx_moddir}/ngx_http_perl_module.so
%{nginx_moddir}/ngx_http_xslt_filter_module.so
%{nginx_moddir}/ngx_mail_module.so
%{nginx_moddir}/ngx_stream_geoip_module.so
%{nginx_moddir}/ngx_stream_module.so

%dir %{perl_vendorarch}/auto/nginx
%{perl_vendorarch}/nginx.pm
%{perl_vendorarch}/auto/nginx/nginx.so


%changelog
* Wed Jul 26 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.3-1
- first created
