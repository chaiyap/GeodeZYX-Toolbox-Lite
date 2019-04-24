#!/bin/bash


WWWWtmp=`perl /dsk/grsp1/BIN/SOFT_GRSP_EPOS/SOFT_EPOS8_BIN_TOOLS/SCRIPTS/get_epoch.pl -o wwww`

excludR='p1r' 
excludP='p1p'
excludR='aaaaaa' 
excludP='aaaaaa'

if [ -z ${1+x} ]; then WWWW=$WWWWtmp ; else WWWW=$1   ; fi

echo "===== RAPID ====="
cd /dsk/ggsp1/products/ggsp/AC/rapid/w${WWWW}
mkdir -p /dsk/grsp1/products/grsp/AC/rapid/w${WWWW}
ls | grep -v "$excludR" | xargs cp -p -v --parents -t /dsk/grsp1/products/grsp/AC/rapid/w${WWWW}

echo "===== PREDI ====="
cd /dsk/ggsp1/products/ggsp/AC/predi/w${WWWW}
mkdir -p /dsk/grsp1/products/grsp/AC/predi/w${WWWW}
ls | grep -v "$excludP" | xargs cp -p -v --parents -t /dsk/grsp1/products/grsp/AC/predi/w${WWWW}

