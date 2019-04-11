#!/bin/bash

spectool -g -R nginx.spec

source scl_source devtoolset-7 ||:

rpmbuild -ba --noclean nginx.spec
