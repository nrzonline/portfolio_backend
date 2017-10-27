#!/bin/bash
set -e

HOST=nrzonline@vps.danielterhorst.nl
HOST_USER_ROOT=home/nrzonline
BACKEND_ROOT=${HOST_USER_ROOT}/nrzonline/portfolio-backend
MEDIA_ROOT=media
TAR_NAME=media.tar.gz

GREEN='\033[0;32m'
LIGHT_GREEN='\033[1;32m'
RED='\033[0;31m'
ORANGE='\033[0;33m'
LIGHT_GREEN='\033[0;32m'
RESET='\033[0m'

unconfirmed=true
while $unconfirmed; do
    echo "${RED}\nYou are about to synchronize your local environment with the live data, this cannot be undone${RESET}"
    echo "${ORANGE}INSTRUCTION${RESET}: This synchronization file must be executed from te project's ROOT directory!"
    echo "${ORANGE}WARNING${RESET}: This will override your current database and the media directory!\n"

    read -p "Are you sure you want to continue? (y/n): " yn
    case $yn in
        [Yy]* ) unconfirmed=false; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes/y or no/n.";;
    esac
done

echo "${LIGHT_GREEN}Tarring '${HOST}:/${BACKEND_ROOT}/${MEDIA_ROOT}' as '${TAR_NAME}' ..${RESET}"
ssh ${HOST} "tar -vcjf ${TAR_NAME} -C /${BACKEND_ROOT}/${MEDIA_ROOT} ."

echo "${LIGHT_GREEN}Secure copying '${HOST}:/${HOST_USER_ROOT}/${TAR_NAME}' to '$(pwd)' ..${RESET}"
scp ${HOST}:/${HOST_USER_ROOT}/${TAR_NAME} .

if [ ! -d "${MEDIA_ROOT}" ]; then
    echo ${LIGHT_GREEN}"Creating media directory locally as '${MEDIA_ROOT}'${RESET}"
    mkdir -p ${MEDIA_ROOT}
fi

echo "${LIGHT_GREEN}Extracting contents of '${TAR_NAME}' into local '${MEDIA_ROOT}' ..${RESET}"
tar -xvf ${TAR_NAME} -C ./${MEDIA_ROOT}

echo "${LIGHT_GREEN}Removing tar '$(pwd)/${TAR_NAME} ..${RESET}"
rm ${TAR_NAME}

echo "${LIGHT_GREEN}Removing tar '${HOST_USER_ROOT}/${TAR_NAME} ..${RESET}"
ssh ${HOST} "rm media.tar.gz"

echo "${LIGHT_GREEN}Secure copying db.sqlite3 to '$(pwd)/db.sqlite3 ..${RESET}"
scp ${HOST}:/${BACKEND_ROOT}/db.sqlite3 db.sqlite3
