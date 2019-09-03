%global         _performance_build  1
%undefine       _hardened_build

%global         nginx_user          nginx
%global         nginx_group         nginx
%global         nginx_uid           996
%global         nginx_gid           996
%global         nginx_moddir        %{_libdir}/nginx/modules
%global         nginx_confdir       %{_sysconfdir}/nginx
%global         nginx_tempdir       %{_var}/cache/nginx
%global         nginx_logdir        %{_localstatedir}/log/nginx
%global         nginx_rundir        %{_rundir}
%global         nginx_lockdir       %{_rundir}/lock/subsys/nginx
%global         nginx_home          %{_datadir}/nginx
%global         nginx_webroot       %{nginx_home}/html
%global         nginx_client_tempdir   %{nginx_tempdir}/client_body_temp
%global         nginx_proxy_tempdir    %{nginx_tempdir}/proxy_temp
%global         nginx_fastcgi_tempdir  %{nginx_tempdir}/fastcgi_temp
%global         nginx_uwsgi_tempdir    %{nginx_tempdir}/uwsgi_temp
%global         nginx_scgi_tempdir     %{nginx_tempdir}/scgi_temp
%global         nginx_proxy_cachedir   %{nginx_tempdir}/proxy_cache
%global         nginx_fastcgi_cachedir %{nginx_tempdir}/fastcgi_cache
%global         nginx_uwsgi_cachedir   %{nginx_tempdir}/uwsgi_cache
%global         nginx_scgi_cachedir    %{nginx_tempdir}/scgi_cache
%global         nginx_source_name      nginx-%{version}

%global         pkg_name            nginx-mainline
%global         main_version        1.17.3
%global         main_release        2%{?dist}

%global         mod_njs_name        njs
%global         mod_njs_version     0.3.5
%global         mod_njs_pkgname     %{mod_njs_name}-%{mod_njs_version}
%global         mod_njs_url         https://hg.nginx.org/%{mod_njs_name}/archive/%{mod_njs_version}.tar.gz#/%{mod_njs_pkgname}.tar.gz

%global         ssl_name            openssl
%global         ssl_version         OpenSSL_1_1_1c
%global         ssl_pkgname         %{ssl_name}-%{ssl_version}
%global         ssl_url             https://github.com/openssl/%{ssl_name}/archive/%{ssl_version}.tar.gz#/%{ssl_pkgname}.tar.gz

%global         zlib_name           zlib
%global         zlib_version        1.2.8
%global         zlib_pkgname        %{zlib_name}-%{zlib_version}
%global         zlib_url            https://github.com/cloudflare/%{zlib_name}/archive/v%{zlib_version}.tar.gz#%{zlib_pkgname}.tar.gz

%global         mod_ndk_name        ngx_devel_kit
%global         mod_ndk_version     0.3.0
%global         mod_ndk_pkgname     %{mod_ndk_name}-%{mod_ndk_version}
%global         mod_ndk_url         https://github.com/simpl/%{mod_ndk_name}/archive/v%{mod_ndk_version}.tar.gz#/%{mod_ndk_pkgname}.tar.gz

%global         mod_lua_name        lua-nginx-module
%global         mod_lua_version     0.10.13
%global         mod_lua_pkgname     %{mod_lua_name}-%{mod_lua_version}
%global         mod_lua_url         https://github.com/openresty/%{mod_lua_name}/archive/v%{mod_lua_version}.tar.gz#/%{mod_lua_pkgname}.tar.gz

%global         mod_lua_upstream_name    lua-upstream-nginx-module
%global         mod_lua_upstream_version 0.07
%global         mod_lua_upstream_pkgname %{mod_lua_upstream_name}-%{mod_lua_upstream_version}
%global         mod_lua_upstream_url     https://github.com/openresty/%{mod_lua_upstream_name}/archive/v%{mod_lua_upstream_version}.tar.gz#/%{mod_lua_upstream_pkgname}.tar.gz

%global         mod_headers_more_name    headers-more-nginx-module
%global         mod_headers_more_version 0.33
%global         mod_headers_more_pkgname %{mod_headers_more_name}-%{mod_headers_more_version}
%global         mod_headers_more_url     https://github.com/openresty/%{mod_headers_more_name}/archive/v%{mod_headers_more_version}.tar.gz#/%{mod_headers_more_pkgname}.tar.gz

%global         mod_echo_name            echo-nginx-module
%global         mod_echo_version         0.61
%global         mod_echo_pkgname         %{mod_echo_name}-%{mod_echo_version}
%global         mod_echo_url             https://github.com/openresty/%{mod_echo_name}/archive/v%{mod_echo_version}.tar.gz#/%{mod_echo_pkgname}.tar.gz

%global         mod_set_misc_name        set-misc-nginx-module
%global         mod_set_misc_version     0.32
%global         mod_set_misc_pkgname     %{mod_set_misc_name}-%{mod_set_misc_version}
%global         mod_set_misc_url         https://github.com/openresty/%{mod_set_misc_name}/archive/v%{mod_set_misc_version}.tar.gz#/%{mod_set_misc_pkgname}.tar.gz

%global         mod_memc_name            memc-nginx-module
%global         mod_memc_version         0.19
%global         mod_memc_pkgname         %{mod_memc_name}-%{mod_memc_version}
%global         mod_memc_url             https://github.com/openresty/%{mod_memc_name}/archive/v%{mod_memc_version}.tar.gz#/%{mod_memc_pkgname}.tar.gz

%global         mod_srcache_name         srcache-nginx-module
%global         mod_srcache_version      0.31
%global         mod_srcache_pkgname      %{mod_srcache_name}-%{mod_srcache_version}
%global         mod_srcache_url          https://github.com/openresty/%{mod_srcache_name}/archive/v%{mod_srcache_version}.tar.gz#/%{mod_srcache_pkgname}.tar.gz

%global         mod_redis2_name          redis2-nginx-module
%global         mod_redis2_version       0.15
%global         mod_redis2_pkgname       %{mod_redis2_name}-%{mod_redis2_version}
%global         mod_redis2_url           https://github.com/openresty/%{mod_redis2_name}/archive/v%{mod_redis2_version}.tar.gz#/%{mod_redis2_pkgname}.tar.gz

%global         mod_drizzle_name         drizzle-nginx-module
%global         mod_drizzle_version      0.1.10
%global         mod_drizzle_pkgname      %{mod_drizzle_name}-%{mod_drizzle_version}
%global         mod_drizzle_url          https://github.com/openresty/%{mod_drizzle_name}/archive/v%{mod_drizzle_version}.tar.gz#/%{mod_drizzle_pkgname}.tar.gz

%global         mod_vts_name             nginx-module-vts
%global         mod_vts_version          0.1.18
%global         mod_vts_pkgname          %{mod_vts_name}-%{mod_vts_version}
%global         mod_vts_url              https://github.com/vozlt/%{mod_vts_name}/archive/v%{mod_vts_version}.tar.gz#/%{mod_vts_pkgname}.tar.gz

%global         mod_sts_name             nginx-module-sts
%global         mod_sts_version          0.1.1
%global         mod_sts_pkgname          %{mod_sts_name}-%{mod_sts_version}
%global         mod_sts_url              https://github.com/vozlt/%{mod_sts_name}/archive/v%{mod_sts_version}.tar.gz#/%{mod_sts_pkgname}.tar.gz

%global         mod_stream_sts_name      nginx-module-stream-sts
%global         mod_stream_sts_version   0.1.1
%global         mod_stream_sts_pkgname   %{mod_stream_sts_name}-%{mod_stream_sts_version}
%global         mod_stream_sts_url       https://github.com/vozlt/%{mod_stream_sts_name}/archive/v%{mod_stream_sts_version}.tar.gz#/%{mod_stream_sts_pkgname}.tar.gz

%global         mod_naxsi_name           naxsi
%global         mod_naxsi_version        0.55.3
%global         mod_naxsi_pkgname        %{mod_naxsi_name}-%{mod_naxsi_version}
%global         mod_naxsi_url            https://github.com/nbs-system/%{mod_naxsi_name}/archive/%{mod_naxsi_version}.tar.gz#/%{mod_naxsi_pkgname}.tar.gz

%global         mod_pagespeed_name       pagespeed
%global         mod_pagespeed_version    1.13.35.2
%global         mod_pagespeed_pkgname    %{mod_pagespeed_name}-%{mod_pagespeed_version}
%global         mod_pagespeed_url        https://github.com/apache/incubator-pagespeed-ngx/archive/v%{mod_pagespeed_version}-stable.tar.gz#/%{mod_pagespeed_pkgname}-stable.tar.gz
%global         psol_url                 https://dl.google.com/dl/page-speed/psol/%{mod_pagespeed_version}-x64.tar.gz

%global         mod_cache_purge_name     ngx_cache_purge
%global         mod_cache_purge_version  2.4.2
%global         mod_cache_purge_pkgname  %{mod_cache_purge_name}-%{mod_cache_purge_version}
%global         mod_cache_purge_url      https://github.com/nginx-modules/%{mod_cache_purge_name}/archive/%{mod_cache_purge_version}.tar.gz#/%{mod_cache_purge_pkgname}.tar.gz

%global         mod_brotli_name          ngx_brotli
%global         mod_brotli_version       0.1.2
%global         mod_brotli_pkgname       %{mod_brotli_name}-%{mod_brotli_version}
%global         mod_brotli_url           https://github.com/eustas/%{mod_brotli_name}/archive/v%{mod_brotli_version}.tar.gz#/%{mod_brotli_pkgname}.tar.gz

%global         brotli_name              brotli
%global         brotli_version           1.0.4
%global         brotli_pkgname           %{brotli_name}-%{brotli_version}
%global         brotli_url               https://github.com/google/%{brotli_name}/archive/v%{brotli_version}.tar.gz#/%{brotli_pkgname}.tar.gz

%global         mod_security_name        ModSecurity-nginx
%global         mod_security_version     1.0.0
%global         mod_security_pkgname     %{mod_security_name}-%{mod_security_version}
%global         mod_security_url         https://github.com/SpiderLabs/%{mod_security_name}/archive/v%{mod_security_version}.tar.gz#/%{mod_security_pkgname}.tar.gz

%global         mod_geoip2_name          ngx_http_geoip2_module
%global         mod_geoip2_version       3.2
%global         mod_geoip2_pkgname       %{mod_geoip2_name}-%{mod_geoip2_version}
%global         mod_geoip2_url           https://github.com/leev/%{mod_geoip2_name}/archive/%{mod_geoip2_version}.tar.gz#/%{mod_geoip2_pkgname}.tar.gz

%bcond_without  http_v2_hpack_enc
%bcond_without  dynamic_tls
%bcond_with     io_uring
%bcond_with     source


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
Source12:       nginx.logrotate
Source13:       nginx.conf
Source14:       nginx-http.conf
Source15:       nginx-http-log_format.conf
Source16:       nginx-http-client.conf
Source17:       nginx-http-proxy.conf
Source18:       nginx-http-gzip.conf
Source19:       nginx-http-ssl.conf
Source20:       nginx-http-security_headers.conf
Source21:       nginx-http-proxy_headers.conf
Source50:       00-default.conf

Source100:      %{ssl_url}
Source101:      %{zlib_url}

Source200:      %{mod_ndk_url}
Source201:      %{mod_lua_url}
Source202:      %{mod_lua_upstream_url}
Source203:      %{mod_headers_more_url}
Source204:      %{mod_echo_url}
Source205:      %{mod_set_misc_url}
Source206:      %{mod_memc_url}
Source207:      %{mod_srcache_url}
Source208:      %{mod_redis2_url}
Source209:      %{mod_vts_url}
Source210:      %{mod_security_url}
Source211:      %{mod_naxsi_url}
Source212:      %{mod_pagespeed_url}
Source213:      %{psol_url}
Source214:      %{mod_cache_purge_url}
Source215:      %{mod_njs_url}
Source216:      %{mod_brotli_url}
Source217:      %{brotli_url}

Source218:      %{mod_sts_url}
Source219:      %{mod_stream_sts_url}
Source220:      %{mod_geoip2_url}

Patch101:       nginx_hpack_push_1.17.3.patch
Patch102:       https://raw.githubusercontent.com/centminmod/centminmod/123.09beta01/patches/cloudflare/nginx__dynamic_tls_records_1015008.patch
Patch103:       https://raw.githubusercontent.com/hakasenyang/openssl-patch/master/nginx_io_uring.patch
Patch200:       https://raw.githubusercontent.com/hakasenyang/openssl-patch/master/openssl-equal-1.1.1b_ciphers.patch

Requires:       openssl
Requires:       jemalloc
Requires(pre):  shadow-utils
Requires(post):   systemd 
Requires(preun):  systemd 
Requires(postun): systemd 
BuildRequires:    systemd

BuildRequires:  make gcc automake autoconf libtool
BuildRequires:  zlib-devel pcre-devel
BuildRequires:  apr apr-util
BuildRequires:  jemalloc-devel
BuildRequires:  cmake ninja-build golang


%description
nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server,
and a generic TCP/UDP proxy server, originally written by Igor Sysoev.


%if %{with source}
%package source
Summary:        nginx source files
Requires:       %{name} = %{version}-%{main_release}

%description source
%{summary}.
%endif


%package mod-http-xslt
Summary:        nginx http xslt module
Requires:       %{name} = %{version}-%{main_release}
Requires:       libxml2 libxslt
BuildRequires:  libxml2-devel libxslt-devel

%description mod-http-xslt
%{summary}.


%package mod-http-perl
Summary:        nginx http perl module
Requires:       %{name} = %{version}-%{main_release}
BuildRequires:  perl(ExtUtils::Embed)

%description mod-http-perl
%{summary}.


%package mod-http-image-filter
Summary:        nginx http image filter module
Requires:       %{name} = %{version}-%{main_release}
Requires:       gd
BuildRequires:  gd-devel

%description mod-http-image-filter
%{summary}.


%package mod-http-geoip
Summary:        nginx http GeoIP module
Requires:       %{name} = %{version}-%{main_release}
Requires:       GeoIP
BuildRequires:  GeoIP-devel

%description mod-http-geoip
%{summary}.


%package mod-stream-geoip
Summary:        nginx stream GeoIP module
Requires:       %{name} = %{version}-%{main_release}
Requires:       %{name}-mod-stream = %{version}-%{main_release}
Requires:       GeoIP
BuildRequires:  GeoIP-devel

%description mod-stream-geoip
%{summary}.


%package mod-stream
Summary:        nginx stream module
Requires:       %{name} = %{version}-%{main_release}

%description mod-stream
%{summary}.


%package mod-mail	
Summary:        nginx mail module
Requires:       %{name} = %{version}-%{main_release}

%description mod-mail
%{summary}.


%package mod-http-lua
Summary:        nginx Lua module (for http module)
Release:        %{mod_lua_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}
Requires:       luajit
BuildRequires:  luajit-devel

%description mod-http-lua
%{summary}.


%package mod-http-lua-upstream
Summary:        nginx Lua upstream module (for http module)
Release:        %{mod_lua_upstream_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}
Requires:       %{name}-mod-http-lua

%description mod-http-lua-upstream
%{summary}.


%package mod-headers-more
Summary:        nginx headers more module
Release:        %{mod_headers_more_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-headers-more
%{summary}.


%package mod-echo
Summary:        nginx echo module
Release:        %{mod_echo_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-echo
%{summary}.


%package mod-set-misc
Summary:        nginx set misc module
Release:        %{mod_set_misc_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-set-misc
%{summary}.


%package mod-memc
Summary:        nginx memc module
Release:        %{mod_memc_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-memc
%{summary}.


%package mod-srcache
Summary:        nginx srcache module
Release:        %{mod_srcache_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-srcache
%{summary}.


%package mod-redis2
Summary:        nginx redis2 module
Release:        %{mod_redis2_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-redis2
%{summary}.


%package mod-naxsi
Summary:        nginx naxsi module
Release:        %{mod_naxsi_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-naxsi
%{summary}.


%package mod-vts
Summary:        nginx virtualhost traffic status module
Release:        %{mod_vts_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-vts
%{summary}.


%package mod-sts
Summary:        nginx stream server traffic status module
Release:        %{mod_sts_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}
Requires:       %{name}-mod-stream = %{version}-%{main_release}

%description mod-sts
%{summary}.


%package mod-pagespeed
Summary:        nginx pagespeed module
Release:        %{mod_pagespeed_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}
BuildRequires:  gcc-c++ libuuid-devel

%description mod-pagespeed
%{summary}.


%package mod-cache-purge
Summary:        nginx cache purge module
Release:        %{mod_cache_purge_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-cache-purge
%{summary}.


%package mod-njs
Summary:        nginx nginScript module
Release:        %{mod_njs_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}
Requires:       %{name}-mod-stream = %{version}-%{main_release}
BuildRequires:  expect-devel libedit-devel

%description mod-njs
%{summary}.


%package mod-brotli
Summary:        nginx brotli module
Release:        %{mod_brotli_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}

%description mod-brotli
%{summary}.


%package mod-security
Summary:        nginx ModSecurity module
Release:        %{mod_security_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}
Requires:       libmodsecurity
BuildRequires:  libmodsecurity-devel

%description mod-security
%{summary}.


%package mod-geoip2
Summary:        nginx geoip2 module
Release:        %{mod_geoip2_version}.%{main_release}
Requires:       %{name} = %{version}-%{main_release}
Requires:       %{name}-mod-stream
Requires:       libmaxminddb
BuildRequires:  libmaxminddb-devel

%description mod-geoip2
%{summary}.


%prep
%setup -q -n %{nginx_source_name}
%if %{with http_v2_hpack_enc}
%patch101 -p1 -b.hpack_push
%endif

%if %{with dynamic_tls}
%patch102 -p1 -b.dynamic_tls
%endif

%if %{with io_uring}
%patch103 -p1 -b.io_uring
%endif

%__tar xf %{SOURCE200}
%__tar xf %{SOURCE201}
%__tar xf %{SOURCE202}
%__tar xf %{SOURCE203}
%__tar xf %{SOURCE204}
%__tar xf %{SOURCE205}
%__tar xf %{SOURCE206}
%__tar xf %{SOURCE207}
%__tar xf %{SOURCE208}
%__tar xf %{SOURCE209}
%__tar xf %{SOURCE210}
%__tar xf %{SOURCE211}
%__tar xf %{SOURCE214}
%__tar xf %{SOURCE215}
%__tar xf %{SOURCE218}
%__tar xf %{SOURCE219}
%__tar xf %{SOURCE220}

# Pagespeed
%__mkdir %{mod_pagespeed_pkgname}
%__tar xf %{SOURCE212} -C %{mod_pagespeed_pkgname} --strip-components 1
pushd %{mod_pagespeed_pkgname}
%__tar xf %{SOURCE213}
popd

# Brotli
%__tar xf %{SOURCE216}
pushd %{mod_brotli_pkgname}/deps
%__tar xf %{SOURCE217} -C brotli --strip-components 1
popd

# SSL
%__mkdir %{ssl_name}
%__tar xf %{SOURCE100} -C %{ssl_name} --strip-components 1
pushd %{ssl_name}
#$%__patch -z.backup -p1 <%{PATCH200}
%patch200 -z.backup -p1
popd

# Cloudflare Zlib
%__mkdir %{zlib_name}
%__tar xf %{SOURCE101} -C %{zlib_name} --strip-components 1


%build
CFLAGS="${CFLAGS:--O3 -march=native -fuse-ld=gold %{optflags} $(pcre-config --cflags) -Wno-error=strict-aliasing -Wformat -Werror=format-security -Wimplicit-fallthrough=0 -fcode-hoisting -Wno-cast-function-type -Wno-format-extra-args -Wno-deprecated-declarations -gsplit-dwarf}"; export CFLAGS;
LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS} -Wl,-E -ljemalloc}"; export LDFLAGS;

export LUAJIT_LIB="%{_libdir}"
export LUAJIT_INC="$(pkg-config --cflags-only-I luajit | sed -e 's/-I//')"

%enable_devtoolset8

./configure \
  --with-cc-opt="${CFLAGS} -DTCP_FASTOPEN=23" \
  --with-ld-opt="${LDFLAGS}" \
  --with-openssl=./%{ssl_name} \
  --with-openssl-opt="enable-ec_nistp_64_gcc_128 enable-tls1_3" \
  --with-zlib=./%{zlib_name} \
  %{?_with_http_v2_hpack_enc} \
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
  --http-uwsgi-temp-path=%{nginx_uwsgi_tempdir} \
  --http-scgi-temp-path=%{nginx_scgi_tempdir} \
  --user=%{nginx_user} \
  --group=%{nginx_group} \
  --build=%{name}-%{version}-%{release} \
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
  --add-dynamic-module=%{mod_ndk_pkgname} \
  --add-dynamic-module=%{mod_lua_pkgname} \
  --add-dynamic-module=%{mod_lua_upstream_pkgname} \
  --add-dynamic-module=%{mod_headers_more_pkgname} \
  --add-dynamic-module=%{mod_echo_pkgname} \
  --add-dynamic-module=%{mod_set_misc_pkgname} \
  --add-dynamic-module=%{mod_memc_pkgname} \
  --add-dynamic-module=%{mod_srcache_pkgname} \
  --add-dynamic-module=%{mod_redis2_pkgname} \
  --add-dynamic-module=%{mod_vts_pkgname} \
  --add-dynamic-module=%{mod_security_pkgname} \
  --add-dynamic-module=%{mod_naxsi_pkgname}/naxsi_src \
  --add-dynamic-module=%{mod_pagespeed_pkgname} \
  --add-dynamic-module=%{mod_cache_purge_pkgname} \
  --add-dynamic-module=%{mod_njs_pkgname}/nginx \
  --add-dynamic-module=%{mod_brotli_pkgname} \
  --add-dynamic-module=%{mod_sts_pkgname} \
  --add-dynamic-module=%{mod_stream_sts_pkgname} \
  --add-dynamic-module=%{mod_geoip2_pkgname} \

#touch %{ssl_name}/.openssl/include/openssl/ssl.h

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
%{__install} -p -d -m 0755 %{buildroot}%{nginx_uwsgi_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_scgi_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_proxy_cachedir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_fastcgi_cachedir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_uwsgi_cachedir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_scgi_cachedir}

# Add systemd service unit file
%{__install} -p -D -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/nginx.service

# sysconfig
%{__install} -p -D -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/sysconfig/nginx

# logrotate
%{__install} -p -D -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/logrotate.d/nginx

# nginx config
unlink %{buildroot}%{nginx_confdir}/koi-utf
unlink %{buildroot}%{nginx_confdir}/koi-win
unlink %{buildroot}%{nginx_confdir}/win-utf
%{__install} -p -D -m 0640 %{SOURCE13} %{buildroot}%{nginx_confdir}/nginx.conf
%{__install} -p -D -m 0640 %{SOURCE14} %{buildroot}%{nginx_confdir}/conf.d/http.conf
%{__install} -p -D -m 0640 %{SOURCE15} %{buildroot}%{nginx_confdir}/conf.d/http/log_format.conf
%{__install} -p -D -m 0640 %{SOURCE16} %{buildroot}%{nginx_confdir}/conf.d/http/client.conf
%{__install} -p -D -m 0640 %{SOURCE17} %{buildroot}%{nginx_confdir}/conf.d/http/proxy.conf
%{__install} -p -D -m 0640 %{SOURCE18} %{buildroot}%{nginx_confdir}/conf.d/http/gzip.conf
%{__install} -p -D -m 0640 %{SOURCE19} %{buildroot}%{nginx_confdir}/conf.d/http/ssl.conf
%{__install} -p -D -m 0640 %{SOURCE20} %{buildroot}%{nginx_confdir}/conf.d/http/security_headers.conf
%{__install} -p -D -m 0640 %{SOURCE21} %{buildroot}%{nginx_confdir}/conf.d/http/proxy_headers.conf

%{__install} -p -D -m 0640 %{SOURCE50} %{buildroot}%{nginx_confdir}/vhost.d/http/00-default.conf

# nginx reset paths
%{__sed} -i \
  -e 's|${rundir}|%{_rundir}|g' \
  -e 's|${sbindir}|%{_sbindir}|g' \
  -e 's|${sysconfdir}|%{_sysconfdir}|g' \
  -e 's|${logdir}|%{nginx_logdir}|g' \
  -e 's|${pkg_name}|nginx|g' \
  %{buildroot}%{_unitdir}/nginx.service \
  %{buildroot}%{_sysconfdir}/sysconfig/nginx \
  %{buildroot}%{_sysconfdir}/logrotate.d/nginx \
  %{buildroot}%{nginx_confdir}/nginx.conf

%{__sed} -i \
  -e 's|${client_tempdir}|%{nginx_client_tempdir}|g' \
  %{buildroot}%{nginx_confdir}/conf.d/http/client.conf

# Add add_module configs
%{__install} -p -d -m 0755 %{buildroot}%{nginx_confdir}/conf.modules.d
for mod_fullpath in $(find %{buildroot}%{nginx_moddir} -type f -name '*.so'); do
  mod_path=$( echo ${mod_fullpath} | sed -re 's|%{buildroot}||' )
  mod_name=$(basename ${mod_path} .so)
  cat > %{buildroot}%{nginx_confdir}/conf.modules.d/${mod_name}.conf <<-___EOL___
	# ${mod_name} loading file
	load_module ${mod_path};
	___EOL___
done
%{__mv} %{buildroot}%{nginx_confdir}/conf.modules.d/{,00-}ngx_stream_module.conf

# Add nginx sources
%if %{with source}
%{__install} -p -d -m 0755 %{buildroot}%{_usrsrc}
%{__cp} -Rp %{_builddir}/%{nginx_source_name} %{buildroot}%{_usrsrc}/%{nginx_source_name}

pushd %{buildroot}%{_usrsrc}

pushd ./%{nginx_source_name}/%{ssl_name}
%{__make} clean ||:
popd

pushd ./%{nginx_source_name}
%{__make} clean
unlink CHANGES
unlink CHANGES.ru
unlink LICENSE
unlink README

find . -type d -name '.deps' -print0    | xargs -r -0 %{__rm} -rf
find . -type d -name '.openssl' -print0 | xargs -r -0 %{__rm} -rf

popd

%{__tar} czf %{nginx_source_name}.tar.gz %{nginx_source_name}
%{__rm}  -rf %{nginx_source_name}

popd
%endif

# njs packaging
%{__install} -D -p -m 0755 %{_builddir}/%{nginx_source_name}/%{mod_njs_pkgname}/build/njs %{buildroot}%{_bindir}/njs


%clean
%{__rm} -rf "%{buildroot}"


%pre
case $1 in
  1)
  : install
  getent group %{nginx_group} >/dev/null 2>&1 \
    || groupadd -r -g %{nginx_gid} %{nginx_group} \
    || groupadd -r %{nginx_group}

  getent passwd %{nginx_user} >/dev/null 2>&1 \
    || useradd -r -g %{nginx_group} -u %{nginx_uid} %{nginx_user} \
    || useradd -r -g %{nginx_group} %{nginx_user}
  ;;
  2)
  : update
  ;;
esac

%post
%systemd_post nginx.service
case $1 in
  1)
  : install
  ;;
  2)
  : update
  ;;
esac

%preun
%systemd_pre nginx.service
case $1 in
  0)
  : uninstall
  ;;
  1)
  : update
  ;;
esac

%postun
%systemd_postun nginx.service
case $1 in
  0)
  : uninstall
  getent passwd %{nginx_user} >/dev/null 2>&1 \
    && userdel %{nginx_user} >/dev/null 2>&1 ||:

  getent group %{nginx_group} >/dev/null 2>&1 \
    && groupdel %{nginx_group} >/dev/null 2>&1 ||:
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
%config(noreplace) %{nginx_confdir}/conf.d/http.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/client.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/gzip.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/log_format.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/proxy.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/ssl.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/security_headers.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/proxy_headers.conf
%config(noreplace) %{nginx_confdir}/vhost.d/http/00-default.conf

%{_mandir}/man3/nginx.3pm.gz

%dir %{nginx_home}
%dir %{nginx_webroot}
%{nginx_webroot}/50x.html
%{nginx_webroot}/index.html

%config(noreplace) %{_unitdir}/nginx.service
%config(noreplace) %{_sysconfdir}/sysconfig/nginx
%config(noreplace) %{_sysconfdir}/logrotate.d/nginx

%dir %{nginx_rundir}
%dir %{nginx_lockdir}

%defattr(-,%{nginx_user},%{nginx_group})
%dir %{nginx_logdir}
%dir %{nginx_tempdir}
%dir %{nginx_client_tempdir}
%dir %{nginx_proxy_tempdir}
%dir %{nginx_fastcgi_tempdir}
%dir %{nginx_uwsgi_tempdir}
%dir %{nginx_scgi_tempdir}
%dir %{nginx_proxy_cachedir}
%dir %{nginx_fastcgi_cachedir}
%dir %{nginx_uwsgi_cachedir}
%dir %{nginx_scgi_cachedir}

%if %{with source}
%files source
%{_usrsrc}/%{nginx_source_name}.tar.gz
%endif

%files mod-http-xslt
%{nginx_moddir}/ngx_http_xslt_filter_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_xslt_filter_module.conf

%files mod-http-perl
%{nginx_moddir}/ngx_http_perl_module.so
%dir %{perl_vendorarch}/auto/nginx
%{perl_vendorarch}/nginx.pm
%{perl_vendorarch}/auto/nginx/nginx.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_perl_module.conf

%files mod-http-image-filter
%{nginx_moddir}/ngx_http_image_filter_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_image_filter_module.conf

%files mod-http-geoip
%{nginx_moddir}/ngx_http_geoip_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_geoip_module.conf

%files mod-stream-geoip
%{nginx_moddir}/ngx_stream_geoip_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_stream_geoip_module.conf

%files mod-stream
%{nginx_moddir}/ngx_stream_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/00-ngx_stream_module.conf

%files mod-mail
%{nginx_moddir}/ngx_mail_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_mail_module.conf

%files mod-http-lua
%{nginx_moddir}/ndk_http_module.so
%{nginx_moddir}/ngx_http_lua_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ndk_http_module.conf
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_lua_module.conf

%files mod-http-lua-upstream
%{nginx_moddir}/ngx_http_lua_upstream_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_lua_upstream_module.conf

%files mod-headers-more
%{nginx_moddir}/ngx_http_headers_more_filter_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_headers_more_filter_module.conf

%files mod-echo
%{nginx_moddir}/ngx_http_echo_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_echo_module.conf

%files mod-set-misc
%{nginx_moddir}/ngx_http_set_misc_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_set_misc_module.conf

%files mod-memc
%{nginx_moddir}/ngx_http_memc_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_memc_module.conf

%files mod-srcache
%{nginx_moddir}/ngx_http_srcache_filter_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_srcache_filter_module.conf

%files mod-redis2
%{nginx_moddir}/ngx_http_redis2_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_redis2_module.conf

%files mod-naxsi
%{nginx_moddir}/ngx_http_naxsi_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_naxsi_module.conf

%files mod-vts
%{nginx_moddir}/ngx_http_vhost_traffic_status_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_vhost_traffic_status_module.conf

%files mod-pagespeed
%{nginx_moddir}/ngx_pagespeed.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_pagespeed.conf

%files mod-cache-purge
%{nginx_moddir}/ngx_http_cache_purge_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_cache_purge_module.conf

%files mod-njs
%{_bindir}/njs
%{nginx_moddir}/ngx_http_js_module.so
%{nginx_moddir}/ngx_stream_js_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_js_module.conf
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_stream_js_module.conf

%files mod-brotli
%{nginx_moddir}/ngx_http_brotli_filter_module.so
%{nginx_moddir}/ngx_http_brotli_static_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_brotli_filter_module.conf
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_brotli_static_module.conf

%files mod-sts
%{nginx_moddir}/ngx_http_stream_server_traffic_status_module.so
%{nginx_moddir}/ngx_stream_server_traffic_status_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_stream_server_traffic_status_module.conf
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_stream_server_traffic_status_module.conf

%files mod-security
%{nginx_moddir}/ngx_http_modsecurity_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_modsecurity_module.conf

%files mod-geoip2
%{nginx_moddir}/ngx_http_geoip2_module.so
%{nginx_moddir}/ngx_stream_geoip2_module.so
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_http_geoip2_module.conf
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_stream_geoip2_module.conf


%changelog
* Tue Sep 03 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.17.3-2
- Add support HPACK enc patch
- Add support dynamic tls record patch
- Add support io_uring patch
* Tue Aug 27 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.17.3-1
- Bump up version njs 0.3.4 -> 0.3.5
* Thu Aug 15 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.17.3-0
- Bump up version nginx 1.17.0 -> 1.17.3
- Bump up version njs 0.3.1 -> 0.3.4
* Thu Jun 13 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.17.0-0
- Bump up version nginx 1.15.11 -> 1.17.0
* Mon Apr 22 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.12-1
- Bump up version nginx 1.15.11 -> 1.15.12
- Bump up version njs 0.3.0 -> 0.3.1
* Thu Apr 11 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.11-1
- Bump up version nginx 1.15.10 -> 1.15.11
* Wed Apr 10 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.10-3
- Add njs binary
* Wed Apr 10 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.10-2
- Bump up version nginx 1.15.8 -> 1.15.10
- Bump up version njs 0.2.7 -> 0.3.0
- Add proxy_headers.conf
* Fri Jan 04 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.8-3
- Change file path for copr.
* Fri Jan 04 2019 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.8-2
- Add geoip2 module
* Thu Dec 27 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.8-1
- Bump up version nginx 1.15.8 -> 1.15.8
- Bump up version njs 0.2.6 -> 0.2.7
* Sat Dec 01 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.7-2
- Change ssl.conf (for OpenSSL 1.1.1)
- Sepalate security_headers.conf from ssl.conf
* Thu Nov 29 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.7-1
- Bump up version nginx 1.15.6 -> 1.15.7
- Bump up version njs 0.2.5 -> 0.2.6
- Change ssl library boringssl -> openssl
* Wed Nov 07 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.6-1
- Bump up version nginx 1.15.5 -> 1.15.6
- Bump up version njs 0.2.4 -> 0.2.5
* Fri Oct 05 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.5-1
- Bump up version nginx 1.15.4 -> 1.15.5
* Tue Oct 02 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.4-1
- Bump up version nginx 1.15.3 -> 1.15.4
- Bump up version njs 0.2.3 -> 0.2.4
* Tue Sep 04 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.3-1
- Bump up version nginx 1.15.2 -> 1.15.3
* Tue Aug 14 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.2-3
- Add TLS1.3 support (use boringssl. and remove libressl)
- Add support TLS1.3 Early Data
- Add ssl.conf
- Add default server config (00-default.conf)
* Sat Aug 04 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.2-2
- Bump up verions njs 0.2.3
* Fri Aug 03 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.2-1
- Bump up version nginx 1.15.1 -> 1.15.2
- Fix typo. uwscgi -> uwsgi
- Change lock file parent path. %{_localstatedir} -> %{_rundir}
- Delete CFLAGS option "-DNGX_LUA_ABORT_AT_PANIC"
- Disable configure option "--with-select_module", "--with-pool_module"
- Enable create debuginfo package. (For binary strip)
- And some fix
* Mon Jul 09 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.1-2
- Add ModSecurity module.
* Mon Jul 09 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.15.1-1
- Bumpup 1.15.1
- Add stream server traffic status module.
* Wed Apr 04 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.10-8
- Add fedora support.
- Add cache purge module.
- Add nginScript module.
- Add brotli module.
* Mon Apr 02 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.10-7
- Bumped libressl 2.7.2
* Thu Mar 29 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.10-6
- Add pagespeed module.
* Wed Mar 28 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.10-5
- Bug fix copr build error.
* Wed Mar 28 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.10-4
- implement jemalloc
* Tue Mar 27 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.10-3
- Add nginx sources.
* Tue Mar 27 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.10-2
- Bumpup libressl 2.6.4
* Tue Mar 27 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.10-1
- Bumpup 1.13.10
* Tue Mar 27 2018 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.4-3
- Add naxsi module.
- Add vts module.
* Fri Nov 03 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.4-2
- Add http Lua module.
- Add http Lua upstream module.
- Add headers more module.
- Add echo module.
- Add set misc module.
- Add memc module.
- Add srcache module.
- Add redis2 module.
* Fri Aug 18 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.4-1
- Create module packages.
* Sun Aug 13 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.4-1
- Bumpup 1.13.4-1
* Sun Aug 13 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.3-1
- Add Requires/BuildRequires
* Wed Jul 26 2017 Ryoh Kawai <kawairyoh@gmail.com> - 1.13.3-1
- first created
