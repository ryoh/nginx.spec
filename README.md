[![Build Status](https://copr.fedorainfracloud.org/coprs/ryoh/nginx-mainline/package/nginx-mainline/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/ryoh/nginx-mainline)

# description

nginx mainline custom build (with openssl11 and jemalloc)

## spec

- nginx 1.19.1 [link](https://nginx.org/en/)

## modules

Main modules

- mod-http-geoip
- mod-http-image-filter
- mod-http-perl
- mod-http-xslt
- mod-mail
- mod-stream
- mod-stream-geoip
- mod-njs 0.4.2 [link](https://hg.nginx.org/njs)

Additional modules

- mod-brotli 1.0.2 [link](https://github.com/eustas/ngx_brotli)
- mod-echo 0.61 [link](https://github.com/openresty/echo-nginx-module)
- mod-headers-more 0.33 [link](https://github.com/openresty/headers-more-nginx-module)
- mod-http-lua 0.10.17 [link](https://github.com/openresty/lua-nginx-module)
- mod-http-lua-upstream 0.07 [link](https://github.com/openresty/lua-upstream-nginx-module)
- mod-memc 0.18 [link](https://github.com/openresty/memc-nginx-module)
- mod-naxsi 0.56 [link](https://github.com/nbs-system/naxsi)
- mod-redis2 0.14 [link](https://github.com/openresty/redis2-nginx-module)
- mod-set-misc 0.31 [link](https://github.com/openresty/set-misc-nginx-module)
- mod-srcache 0.31 [link](https://github.com/openresty/srcache-nginx-module)
- mod-vts 0.1.16 [link](https://github.com/vozlt/nginx-module-vts)
- mod-sts 0.1.1 [link](https://github.com/vozlt/nginx-module-sts)
- mod-stream-sts 0.1.1 [link](https://github.com/vozlt/nginx-module-stream-sts)
- mod-pagespeed 1.13.35.2 [link](https://developers.google.com/speed/pagespeed/module/)
- mod-security 1.0.0 [link](https://github.com/SpiderLabs/ModSecurity-nginx)
- mod-geoip2 3.2 [link](https://github.com/leev/ngx_http_geoip2_module)


# Changelog
- 2020-07-10 bump up version nginx 1.19.1, njs 0.4.2
- 2020-04-20 bump up version nginx 1.17.10, njs 0.3.9
- 2019-09-03 Add support HPACK, Dynamic TLS record, io_uring
- 2019-08-28 bump up version nginx 1.17.3, njs 0.3.5, openssl 1.1.1c, cloudflare-zlib
- 2019-06-14 bump up version nginx 1.17.0, njs 0.3.2, openssl 1.1.1c
- 2019-04-22 bump up version nginx 1.15.12, njs 0.3.1
- 2019-04-11 bump up version nginx 1.15.11, njs 0.3.0
- 2019-01-04 Add GeoIP2 module.
- 2018-12-25 bump up version nginx 1.15.8, njs 0.2.7, and add ssl settings.
- 2018-11-29 bump up version nginx 1.15.7, njs 0.2.6, openssl 1.1.1a
- 2018-11-07 bump up version nginx 1.15.6, njs 0.2.5
- 2018-10-02 bump up version nginx 1.15.4, njs 0.2.4
- 2018-09-04 bump up version nginx 1.15.3
- 2018-08-22 add OCSP patch. add cloudflare HPACK patch
- 2018-08-16 add support TLS1.3
- 2018-08-03 bump up version nginx 1.15.2
- 2018-07-08 add mod-sts 0.1.1, mod-stream-sts 0.1.1, mod-security 1.0.0
- 2018-07-08 bumped version nginx 1.15.1, libressl 2.7.4
- 2018-06-07 bumped version nginx 1.15.0, libressl 2.7.3, mod-http-lua 0.10.13 and mod-vts 0.1.16
- 2018-04-08 bumped version nginx 1.13.11, libressl 2.7.2 and njs 0.2.0
- 2018-04-04 add modules link and copr status budge
- 2018-03-28 add copr link
- 2018-03-27 bumped version nginx 1.13.10 and libressl 2.6.4
- 2017-11-04 nginx add some modules
