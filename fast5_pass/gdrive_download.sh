#!/bin/sh
# Script source https://gist.github.com/guysmoilov/ff68ef3416f99bd74a3c431b4f4c739a
# Usage: gdrive_download 123-abc ./output.zip
gdrive_download() {
  CONFIRM=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://drive.google.com/uc?export=download&id=$id" -O- | sed -En 's/.*confirm=([0-9A-Za-z_]+).*/\1/p')
  echo $CONFIRM
  wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$CONFIRM&id=$id" -O $outfile
  rm -f /tmp/cookies.txt
}

id=$1
outfile=$2
gdrive_download
