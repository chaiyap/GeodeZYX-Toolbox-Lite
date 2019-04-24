#!/bin/csh

rsync -Pah /dsk/ggsp1/data/iers/eop/bula/finals.data  /dsk/grsp1/data/iers/eop/bula/finals.data
rsync -Pah /dsk/ggsp1/data/iers/eop/bula/finals.daily /dsk/grsp1/data/iers/eop/bula/finals.daily

rsync -Pah /dsk/ggsp1/cf_orb/acc_combi/combi/common/erp_bull/finals.data  /dsk/grsp1/cf_orb/acc_combi/combi/common/erp_bull/finals.data
rsync -Pah /dsk/ggsp1/cf_orb/acc_combi/combi/common/erp_bull/finals.daily /dsk/grsp1/cf_orb/acc_combi/combi/common/erp_bull/finals.daily

rsync -Pah /dsk/ggsp1/cf_orb/acc_data/erp_bull/finals.data_LAST  /dsk/grsp1/cf_orb/acc_data/erp_bull/finals.data_LAST
rsync -Pah /dsk/ggsp1/cf_orb/acc_data/erp_bull/finals.daily_LAST /dsk/grsp1/cf_orb/acc_data/erp_bull/finals.daily_LAST
