#!/bin/csh

set passfile='/home/grsp/SCRIPTS_qnd/password_ESOC.txt' 
set PASSWORD="7+dTHSz2"

python /home/grsp/SCRIPTS_qnd/ftpmirror.py -v -l gfz -p $PASSWORD 195.74.166.126 /output/products/ /dsk/grsp1/products_RAW_MIRROR/grsp/
find /dsk/grsp1/products_RAW_MIRROR/grsp/AC/rapid/ | egrep '.*p(2|3)r.*(snx|inx|sum|bias\.xml|srp|tro)' | xargs rm -vfr
