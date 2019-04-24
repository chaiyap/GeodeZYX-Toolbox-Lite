#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os 
import shutil

def unzip_gz_Z(inp_gzip_file,out_gzip_file='',remove_inp=False, force = False,
               force_function = None):
    """
    if out_gzip_file if not precised, file will be extracted in the same folder
    as inp_gzip_file
    
    .Z decompression is implemented, but is very unstable (avoid .Z, prefer .gz)
    """
    
    import gzip,zlib

    if not force_function:
        if inp_gzip_file.endswith('.gz'):
            is_gz = True
        elif inp_gzip_file.endswith('.Z'):
            is_gz = False
        else:
            is_gz = True
    
    if out_gzip_file == '':
        out_gzip_file = os.path.join(os.path.dirname(inp_gzip_file) , 
                                     '.'.join(os.path.basename(inp_gzip_file).split('.')[:-1]))
    

    if os.path.isfile(out_gzip_file) and not force:
        print 'INFO : ' , out_gzip_file , 'already exists, skiping (use force option)'
        pass
    else:
        if is_gz:
            with gzip.open(inp_gzip_file, 'rb') as f_in, open(out_gzip_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        else:
            print "WARN : zlib decompress is unstable !! and .Z should be definitly avoided ... "
            str_object1 = open(inp_gzip_file, 'rb').read()
            str_object2 = zlib.decompress(str_object1)
            f = open(out_gzip_file, 'wb')
            f.write(str_object2)
            f.close()
           
        print 'doing the job ...'
            
    if remove_inp and os.path.getsize(out_gzip_file) > 0:
        os.remove(out_gzfil)
    
    return out_gzip_file

def find_recursive(parent_folder , pattern, sort_results = True):
    """
    Inputs :
        parent_folder : the parent folder path
        pattern       : the researched files pattern name (can manage wildcard)
    Outputs :
        matches : list of matching files paths
        
    Source :
        https://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
    """
    import fnmatch
    matches = []
    for root, dirnames, filenames in os.walk(parent_folder):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    
    if sort_results:
        matches = sorted(matches)
    
    return matches




print "================= MV IGR ================="

products_dir = '/dsk/grsp1/products_RAW_MIRROR/grsp/AC/'
igr_dir = '/dsk/grsp1/products_RAW_MIRROR/grsp/IGS/'
igr_pattern = 'igr*'

igr_files_list = find_recursive(igr_dir , igr_pattern , sort_results = True)

print igr_files_list

for igrfil in igr_files_list:
    print igrfil
    weekdir = igrfil.split('/')[-2]
    igrfilnam = os.path.basename(igrfil)
    igrac_prob_dir =  os.path.join(products_dir,'rapid',weekdir)
    if '.Z' in igrfilnam:
        igrac_prob =  os.path.join(igrac_prob_dir,igrfilnam[:-2])
    else:
        igrac_prob =  os.path.join(igrac_prob_dir,igrfilnam)        
    print 'probable file' , igrac_prob
    if not os.path.isfile(igrac_prob):
        shutil.copy(igrfil,igrac_prob_dir) 
        print 'COPY' , igrfil , igrac_prob_dir
    else:
        print 'NO COPY' , igrfil



print "=============== GZIP Prods ==============="
gz_pattern   = '*.gz' 
Z_pattern   = '*.Z' 


gz_files_list = find_recursive(products_dir , gz_pattern, sort_results = True)
#Z_files_list  = find_recursive(products_dir , Z_pattern, sort_results = True)

gzZ_files_list = gz_files_list

for gzfil in gzZ_files_list:
    print gzfil
    out_gzfil = unzip_gz_Z(gzfil, force = False)
    print out_gzfil , os.path.isfile(out_gzfil) , os.path.getsize(out_gzfil)

print "=============== GZIP Combi ==============="
gz_pattern   = '*.gz' 
Z_pattern   = '*.Z' 

combi_dir = '/dsk/grsp1/products/grsp/CMB/'

gz_files_list = find_recursive(combi_dir , gz_pattern, sort_results = True)
#Z_files_list  = find_recursive(products_dir , Z_pattern, sort_results = True)

gzZ_files_list = gz_files_list

for gzfil in gzZ_files_list:
    print gzfil
    out_gzfil = unzip_gz_Z(gzfil, force = False)
    print out_gzfil , os.path.isfile(out_gzfil) , os.path.getsize(out_gzfil)


print "===============  Z ZIP IGR ==============="
igr_dir = products_dir
igr_pattern = 'igr*Z'

igr_files_list = find_recursive(igr_dir , igr_pattern , sort_results = True)

print igr_files_list

for igrfil in igr_files_list:
    print igrfil
    week = igrfil.split('/')[-2]
    cdkom = 'cd ' + os.path.dirname(igrfil)
    os.system(cdkom + '&& uncompress ' + os.path.basename(igrfil))
    print  os.path.isfile(igrfil[:-2]) , os.path.getsize(igrfil[:-2])

print "================= MV IGR SUM ================="

sum_dir = '/dsk/ggsp1/products/ggsp/'
sum_pattern = 'igr*sum'

sum_files_list = find_recursive(sum_dir , sum_pattern , sort_results = True)

print sum_files_list

for sumfil in sum_files_list:
    print sumfil
    weekdir = sumfil.split('/')[-2]
    sumfilnam = os.path.basename(sumfil)
    sum_prob_dir =  os.path.join(products_dir,'rapid',weekdir)
    sum_prob     =  os.path.join(sum_prob_dir,sumfilnam)        
    print 'probable file' , sum_prob
    if not os.path.isfile(sum_prob) and os.path.isdir(sum_prob_dir):
        shutil.copy(sumfil,sum_prob_dir) 
        print 'COPY' , sumfil,sum_prob_dir
    #~ else:
        #~ print 'NO COPY' , sumfil




#os.system('rsync -Pah /dsk/grsp1/products_RAW_MIRROR/grsp/AC/  /dsk/grsp1/products/grsp/AC/')


