# nginx custom spec file

copr: https://copr.fedorainfracloud.org/coprs/ryoh/nginx-mainline/

# description

nginx mainline custom build (with libressl and jemalloc)

## spec

- nginx 1.13.10
- libressl 2.6.4
- jemalloc 3.6.0

## modules

Main modules

- mod-http-geoip
- mod-http-image-filter
- mod-http-perl
- mod-http-xslt
- mod-mail
- mod-stream
- mod-stream-geoip

Additional modules

- mod-echo 0.61
- mod-headers-more 0.33
- mod-http-lua 0.10.10
- mod-http-lua-upstream 0.07
- mod-memc 0.18
- mod-naxsi 0.55.3
- mod-redis2 0.14
- mod-set-misc 0.31
- mod-srcache 0.31
- mod-vts 0.1.15


# Changelog
- 2018-03-28 add copr link
- 2018-03-27 bumped version nginx 1.13.10 and libressl 2.6.4
- 2017-11-04 nginx add some modules
