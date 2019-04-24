#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os 
import shutil
from glob import iglob

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


def cat(outfilename, *infilenames):
    """
    Is for concatenating files ...
    For just a print, use cat_print ! 
    http://stackoverflow.com/questions/11532980/reproduce-the-unix-cat-command-in-python
        kindall response
    """
    with open(outfilename, 'w') as outfile:
        for infilename in infilenames:
            with open(infilename , 'r+') as infile:
                for line in infile:
                    if line.strip():
                        outfile.write(line)
    return outfilename


def cat_remove_header(infilepath,outfilepath,header='', header_included = False):
    
    bool_out = False
    F = open(infilepath,'r+')

    with open(outfilepath, 'w') as outfile:
        for line in F:
            if header in line:
                bool_out = True
                if not header_included:
                    continue           
            if bool_out:
                outfile.write(line)
    
    return outfilepath
        


gss_path = '/dsk/grsp1/data_RAW_MIRROR/gss/hourly'

d = gss_path
#day_dir_list = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

day_dir_list = list(reversed(sorted(iglob(gss_path + '/y*/d*/'))))

#find /dsk/grsp1/data_RAW_MIRROR/ -name '*BAD' -exec readlink -f {} \; | xargs rm -v

print day_dir_list

debug_suffix = 'BAD'

os.system("find /dsk/grsp1/data_RAW_MIRROR/ -name '*BAD' -exec readlink -f {} \; | xargs rm -v")
os.system("find /dsk/grsp1/data_RAW_MIRROR/ -name '*_rm_head.tmp' -exec readlink -f {} \; | xargs rm -v")


for day_dir in day_dir_list:
    yyyy = day_dir.split('/')[-3][1:]
    yy   = str(int(yyyy) - 2000)
    doy  = day_dir.split('/')[-2][1:]
    
    print 'INFO : ' , yyyy , yy ,doy , day_dir , day_dir.split('/')[-1]
    
    day_hour_gz_rnx_lis = find_recursive(day_dir,'*o.gz')
    code_list = sorted(list(set([ os.path.basename(e)[0:4] for e in day_hour_gz_rnx_lis])))
    
    print code_list
    
    for code in code_list:
        rnx_poten_nam = code + doy + '0' + '.'  + yy + 'o'
        rnx_poten_path = os.path.join(day_dir,rnx_poten_nam)
        if os.path.isfile(rnx_poten_path) and not os.path.isfile(rnx_poten_path +debug_suffix+ '_NOT_COMPLETE'):
            print 'INFO : RNX exists and is complete !' , rnx_poten_path
            continue
        else:
            gz_hour_rnx_lis = [e for e in day_hour_gz_rnx_lis if (code + doy) in e]
            print 'aaaaa' , gz_hour_rnx_lis
            ungz_hour_rnx_lis = sorted([unzip_gz_Z(e) for e in gz_hour_rnx_lis])
            
            ungz_hour_rnx_lis_wo_first = ungz_hour_rnx_lis[1:]
            
            ungz_hour_rnx_lis_wo_first_wo_header = []
            for f in ungz_hour_rnx_lis_wo_first:
                fout = cat_remove_header(f,f + '_rm_head.tmp','END OF HEADER')
                ungz_hour_rnx_lis_wo_first_wo_header.append(fout)
                
            print ungz_hour_rnx_lis
            
            print 'WITHOUT HEADER' , ungz_hour_rnx_lis_wo_first_wo_header
            
            #teqcfct = ' '.join(('cd', day_dir , '&& teqc ' ) + ungz_hour_rnx_lis + ('>',rnx_poten_nam+debug_suffix) ) 
            #os.system(teqcfct)
            final_rnx_hour_stk = [ ungz_hour_rnx_lis[0] ] + ungz_hour_rnx_lis_wo_first_wo_header

            cat(rnx_poten_path+debug_suffix , *final_rnx_hour_stk )
            if len(final_rnx_hour_stk) != 24:
                os.system('touch ' + rnx_poten_path+debug_suffix+ '_NOT_COMPLETE' )
            elif os.path.isfile(rnx_poten_path +debug_suffix+ '_NOT_COMPLETE'):
                pass
                #os.remove(rnx_poten_path +debug_suffix+ '_NOT_COMPLETE')
                
            print 'INFO : ' , rnx_poten_path+debug_suffix ,  os.path.isfile(rnx_poten_path+debug_suffix)
    


