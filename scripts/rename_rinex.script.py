import softs_runner
import glob

#mes parametres
#out_dir = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/OUVA'
#input_rinex='/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/OUVA/OUVA*O'
#stat_out_name = 'ouva'
#remove = False # supprime le rinex d'origine avec le mauvais nom

out_dir = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/KOUM'
input_rinex='/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/KOUM/KOUM*O'
stat_out_name = 'koum'
remove = False # supprime le rinex d'origine avec le mauvais nom
#out_dir = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/SURP'
#input_rinex='/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/SURP/SURP*O'
#stat_out_name = 'surp'
#remove = False # supprime le rinex d'origine avec le mauvais nom
# ============= FIN DE PARAMETRES =============

inp_rnx_lis = glob.glob(input_rinex)

if inp_rnx_lis == []:
    print('inp_rnx_lis empty ...')
    print('check the path or the wildcard')

for rnx in inp_rnx_lis:
	print(rnx)
	softs_runner.rinex_renamer(rnx,out_dir,stat_out_name,remove)
