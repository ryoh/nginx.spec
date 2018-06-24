#!/bin/bash
#
# setup rpmbuild files
#
# set -x
set -euo pipefail

readonly RPMMACROS_FILE=".rpmmacros"
readonly HOME_RPMMACROS="${HOME}/${RPMMACROS_FILE}"

echo "Set ${RPMMACROS_FILE} to homedir"
if [[ -f "${HOME_RPMMACROS}" ]]; then
  echo "Found ${HOME_RPMMACROS} overwrite? (y/N) "
  read yesno
  case "${yesno}" in
  [yY][eE][sS] | [yY] )
    : OK
    ;;
  * )
    : No
    echo "aborted"
    exit 1
    ;;
  esac
fi

: "Set .rpmmacros file to home directory"
ln -sf "${PWD}/${RPMMACROS_FILE}" "${HOME_RPMMACROS}"

spectool -g -R -C SOURCES/ SPECS/nginx.spec
