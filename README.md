[![Build Status](https://copr.fedorainfracloud.org/coprs/ryoh/nginx-mainline/package/nginx-mainline/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/ryoh/nginx-mainline)

# description

nginx mainline custom build (with libressl and jemalloc)

## spec

- nginx 1.13.10 (https://nginx.org/en/)
- libressl 2.7.2 (https://www.libressl.org/)
- jemalloc 3.6.0 (https://github.com/jemalloc/jemalloc)

## modules

Main modules

- mod-http-geoip
- mod-http-image-filter
- mod-http-perl
- mod-http-xslt
- mod-mail
- mod-stream
- mod-stream-geoip
- mod-njs

Additional modules

- mod-brotli 1.0.2 (https://github.com/eustas/ngx_brotli)
- mod-echo 0.61 (https://github.com/openresty/echo-nginx-module)
- mod-headers-more 0.33 (https://github.com/openresty/headers-more-nginx-module)
- mod-http-lua 0.10.10 (https://github.com/openresty/lua-nginx-module)
- mod-http-lua-upstream 0.07 (https://github.com/openresty/lua-upstream-nginx-module)
- mod-memc 0.18 (https://github.com/openresty/memc-nginx-module)
- mod-naxsi 0.55.3 (https://github.com/nbs-system/naxsi)
- mod-redis2 0.14 (https://github.com/openresty/redis2-nginx-module)
- mod-set-misc 0.31 (https://github.com/openresty/set-misc-nginx-module)
- mod-srcache 0.31 (https://github.com/openresty/srcache-nginx-module)
- mod-vts 0.1.15 (https://github.com/vozlt/nginx-module-vts)
- mod-pagespeed 1.13.35.2 (https://developers.google.com/speed/pagespeed/module/)


# Changelog
- 2018-04-04 add modules link and copr status budge
- 2018-03-28 add copr link
- 2018-03-27 bumped version nginx 1.13.10 and libressl 2.6.4
- 2017-11-04 nginx add some modules
