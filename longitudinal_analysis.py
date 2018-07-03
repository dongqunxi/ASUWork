# -*- coding: utf-8 -*-
"""
Longitudinal analysis as batch processing way

Qunxi Dong <qdong17@asu.edu>
"""
import xlrd,glob, os
import subprocess
do_copy = True
sc = ['SCAN_1','SCAN_2']
hs = ['L','R']
exe_path = 'O:\\s1_s2\\SurfStat.exe'
if do_copy:
    
    file_location = "O:\\New_HP_final\\0-all.xls"
    #fn_eval = 'O:\\s1_s2\\eval.txt'
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_name('Sheet1')
    x = []
    for cell in sheet.col(0):
        for h in hs:
            FNULL = open(os.devnull, 'w') 
            path_m1 = glob.glob('O:\\Data\\HP\\Final_HP\\%s\\%s\\%s*' %(sc[0], h, cell.value))[0]
            path_m2 = glob.glob('O:\\Data\\HP\\Final_HP\\%s\\%s\\%s*' %(sc[1], h, cell.value))[0]
            output_m = 'O:\\Data\\HP\\Final_HP\\SCAN1-2\\%s\\%s_%s_s1-2.m' %(h,cell.value, h)
            args = exe_path + ' -TwoTDiff %s %s %s' %(path_m1, path_m2, output_m)
            #with open(fn_eval, "a") as f:
             #   f.write('%s\n' %args)
            subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)
        #fn_list = glob.glob('O:/Data/HP/Final_HP//*/%s*' %cell.value)
   
#fn_eval = 'O:\s1_s2\BNI_s1-s2.txt'
#exe_c = 'O:\s1_s2\SurfStat.exe -TwoTDiff'
#
#    path_m1 = 'O:\Data\HP\Final_HP\SCAN_1\L\S8033_left_S1.m'
#    path_m2 = 'D:\BNI_S2\jfeature\left_jfeatures_S2\S8033_left_S2.m'
#    output_m = 'D:\BNI_S2\jfeature\scan1_2\S8033_left_S1_2.m'
#    with open(fn_eval, "a") as f:
#        
#        f.write('%s %s %s %s\n' %(exe_c, path_m1, path_m2, output_m))