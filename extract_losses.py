import numpy as np
import sys,os,glob

################################## INPUT ##############################################
# output files
root_out = '/mnt/ceph/users/camels/Results/Gaussian_fields'
#######################################################################################

files = glob.glob('%s/losses/*'%root_out)

size = len(root_out)

for f in files:
    data = np.loadtxt(f)
    index = np.where(data[:,2]==np.min(data[:,2]))[0]
    minimum = data[index][0]
    print('%70s : %4d %.3e %.3e'%(f[size:],minimum[0],minimum[1],minimum[2]))
