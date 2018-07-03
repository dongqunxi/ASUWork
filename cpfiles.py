# -*- coding: utf-8 -*-
"""
Functions: Script for nii.gz selection
Author: Qunxi Dong
        qdong17@asu.edu
Date: 06/26/2018

"""
# Parameters
import glob, os, shutil
import numpy as np
g_path = 'O:/Data/Group/'
g_n = 4
out_path = g_path + 't1files/'
f_type = 't1.nii'
scans = 2
# Execute
for i in range(4):
    plist_nii = glob.glob(g_path + 'Group%d/*/*_%s' %(i+1, f_type))
    plist_nii = sorted(plist_nii)
    plist_nii = np.reshape(plist_nii, (len(plist_nii)/scans, scans))
    for fn_niis in plist_nii:
        s = 0
        for fn_nii in fn_niis:
            bs_name = os.path.basename(fn_nii)
            dis_path = out_path + 'S%s_BAI_SCAN0%d_%s' %(bs_name.split\
                     ('_epoch')[0].split('nih0')[1], s+1, f_type)
            shutil.copy(fn_nii, dis_path)
            s = s + 1
    