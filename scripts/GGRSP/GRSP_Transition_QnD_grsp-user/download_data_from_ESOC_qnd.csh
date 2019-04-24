#!/bin/csh

set passfile='/home/grsp/SCRIPTS_qnd/password_ESOC.txt' 
set PASSWORD="7+dTHSz2"

foreach i (`seq 1 4`)
  set DAY=`date -d "$i day ago" '+%Y%m%d'`
  set DDD=`epo -o ddd -type yyyymmdd -epo $DAY`
  set YYYY=`epo -o yyyy -type yyyymmdd -epo $DAY`
  mkdir -p /dsk/grsp1/data_RAW_MIRROR/gss/hourly/y${YYYY}/d${DDD}/
  python /home/grsp/SCRIPTS_qnd/ftpmirror.py -s '.*d.gz' -v -l gfz -p $PASSWORD 195.74.166.126   /output/data/gss/hourly/y${YYYY}/d${DDD}/ /dsk/grsp1/data_RAW_MIRROR/gss/hourly/y${YYYY}/d${DDD}/
end

