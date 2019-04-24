#!/bin/csh


set yesterday=`date -d "1 day ago" '+%Y%m%d'`

set WWWW=`epo -type yyyymmdd -o wwww -epo $yesterday`
set WD=`epo -type yyyymmdd -o wd -epo $yesterday`

echo "=========  ERP  ============"
cp -v /dsk/ggsp1/cf_orb/acc_combi/combi/final/pole/finals.data /dsk/grsp1/cf_orb/acc_combi/combi/final/pole/finals.data
cp -v /dsk/ggsp1/cf_orb/acc_combi/combi/rapid/pole/finals.data /dsk/grsp1/cf_orb/acc_combi/combi/rapid/pole/finals.data
cp -v /dsk/ggsp1/cf_orb/acc_combi/combi/common/erp_bull/finals.data /dsk/grsp1/cf_orb/acc_combi/combi/common/erp_bull/finals.data
cp -v /dsk/ggsp1/cf_orb/acc_combi/combi/common/erp_bull/finals.daily /dsk/grsp1/cf_orb/acc_combi/combi/common/erp_bull/finals.daily 

bash ~/copy_products_qnd.bash $WWWW

docmbrap -wwwwd ${WWWW}${WD}
