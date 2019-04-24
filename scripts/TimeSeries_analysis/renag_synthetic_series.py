
from megalib import *
import geoclass as gcls

#filein         = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/DATA/RENAG-Synthetiques/RENAG-Synthetiques/RU02.neu"
#discont_filein = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/DATA/RENAG-Synthetiques/RENAG-Synthetiques/RU02.off"
#
#
#filein         = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/DATA/RENAG-Synthetiques/RENAG-Synthetiques/RU02.neu"
#discont_filein = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/DATA/RENAG-Synthetiques/RENAG-Synthetiques/RU02.off"
#
#filein = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/DATA/RENAG-Synthetiques/RENAG-Synthetiques/MR01.neu"
#discont_filein = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/DATA/RENAG-Synthetiques/RENAG-Synthetiques/MR01.off"

path = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/DATA/RENAG-Synthetiques/RENAG-Synthetiques/"
path = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/DATA/RENAG-Synthetiques-v2/RENAG-Synthetiques-v2/"

export_path = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/HECTOR_WORK/v2/RAW_NEU"

plots_path  = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/PLOTS_v2"

gf.create_dir(export_path)
gf.create_dir(plots_path)

Files = glob.glob(path + "/*")

Stat_list = sorted(list(set([os.path.basename(e).split(".")[0] for e in Files])))

# FOR A VERY FIRST RUN, DONT FORGET TO DISABLE THE"DISCONT POINTER" SECTION
if 0:
    Stat_list_selected =  Stat_list
# FOR AN OPTIMIZED SELECTION USING THE POINTER, 
#SELECT 1 STATION WHICH NEEDS MANU POINTING
if 1:
    i = 1
    Stat_list_selected = [Stat_list[i]]
    Stat_list_selected = ["SU06"]

for stat in Stat_list_selected: 
    stat_files = sorted(glob.glob(path + stat + "*"))
    
    if len(stat_files) == 1: # READ FILES
        ts = gcls.read_renag_synthetic(stat_files[0])
    else:
        ts = gcls.read_renag_synthetic(stat_files[0],stat_files[1])
        
    if 1: # DISCONT POINTER
        fig = ts.plot(diapt=2)
        ts.plot_discont()    
        multi , cid = ts.discont_manu_click(fig)    

    if 0: # NEU FILE SAVER, 
          # 1 : for the First General processing
          # 0 : for a manual pointing BUT RUN THIS MANUALLY AFTER THE POINTING
        gcls.export_ts_as_neu(ts, export_path , "")

    if 0: # CLEANER (not very useful ... don't use it)
        ts2 = gcls.sigma_cleaner(ts,2,cleantype='any') 
        ts2 = gcls.mad_cleaner(ts2,2,'dist')
        ts.plot(symbol="+r")
        ts2.plot(symbol="xb")
    
    if 0: # PLOTTER
          # 1 : for the First General processing
          # 0 : for a manual pointing BUT RUN THIS MANUALLY AFTER THE POINTING
        plt.ioff()
        gcls.export_ts_plot(ts,plots_path)


