import h5py
import numpy as np

#READ
dist = 0.1 #\Angstrom

opf = h5py.File("WAN_MAT_FE.h5", "r")
WOPP_FE = opf['WOPP'][:]
opf.close()

opf = h5py.File("WAN_MAT_CENT.h5", "r")
WOPP_CENT = opf['WOPP'][:]
opf.close()

# reproduce Wannier centers
# FE
WCC_FE = []
for i in range(10):
    WCC_FE.append([np.sum(WOPP_FE[0,i]).real,np.sum(WOPP_FE[1,i]).real,np.sum(WOPP_FE[2,i]).real])
    #  print(np.sum(WOPP_FE[0,i]).real,np.sum(WOPP_FE[1,i]).real,np.sum(WOPP_FE[2,i]).real)
# CENT
WCC_CENT = []
for i in range(10):
    WCC_CENT.append([np.sum(WOPP_CENT[0,i]).real,np.sum(WOPP_CENT[1,i]).real,np.sum(WOPP_CENT[2,i]).real])
    #  print(np.sum(WOPP_CENT[0,i]).real,np.sum(WOPP_CENT[1,i]).real,np.sum(WOPP_CENT[2,i]).real)
print("Total_dipole",-(np.array(WCC_FE) - np.array(WCC_CENT))[:,2].sum()*2)

# calculation
# D_imn[dir][MO][m][n][nrpt_1][nrpt_2]
# for MO_3
Z = -(WOPP_FE-WOPP_CENT)/0.1

# AO to Atom idx Pb, Ti, O1, O2, O3
idx = [[0,1,2,3],[4,5,6,7,8],[9,10,11],[12,13,14],[15,16,17]]
# MO to Atom idx Pb_s O1, O2, O3
idx_MO = [[0],[],[1,2,3],[4,5,6],[7,8,9]]

#  result = 0.0+1j*0.0
#  for atom_all in [0,2,3,4]:
#      for MO in idx_MO[atom_all]:
#          for atom in range(5):
#              for atom_1 in range(5):
#                  for nrpt in range(nrpts):
#                      for n in idx[atom]:
#                          for nrpt_1 in range(nrpts):
#                              for m in idx[atom_1]:
#                                  result += Z[2,MO,n,m,nrpt,nrpt_1]
#  result_real = result.real
#  print("Check Total Z for MO 0 (Pb s):",2*result_real)

nrpts = WOPP_FE.shape[4]
Z_total = 0.0
for atom_all in [0,2,3,4]:
    for MO in idx_MO[atom_all]:
#  for atom_all in [2]:
#      for MO in idx_MO[atom_all]:
#      for MO in [2]:
        print("Atom:",atom_all," MO:",MO)
        Z_decompose = []

        #  #Total
        #  result = 0.0+1j*0.0
        #  for atom in range(5):
        #      for atom_1 in range(5):
        #          for nrpt in range(7):
        #              for n in idx[atom]:
        #                  for nrpt_1 in range(7):
        #                      for m in idx[atom_1]:
        #                          result += Z[2,MO,n,m,nrpt,nrpt_1]
        #  Z_decompose.append(result)

        #RS
        result = 0.0+1j*0.0
        for atom in [atom_all]:
            for nrpt in [0]:
                for n in idx[atom]:
                    result += Z[2,MO,n,n,nrpt,nrpt]
        Z_decompose.append(result)

        #CT
        result = 0.0+1j*0.0
        for atom in range(5):
            for nrpt in range(nrpts):
                if (atom==atom_all and nrpt==0):
                    pass
                else:
                    for n in idx[atom]:
                        result += Z[2,MO,n,n,nrpt,nrpt]
        Z_decompose.append(result)

        #NP
        result = 0.0+1j*0.0
        for atom in range(5):
            for nrpt in range(nrpts):
                for n in idx[atom]:
                    for m in idx[atom]:
                        if n==m:
                            pass
                        else:
                            result += Z[2,MO,n,m,nrpt,nrpt]
        Z_decompose.append(result)

        #COV
        result = 0.0+1j*0.0
        for atom in range(5):
            for nrpt in range(nrpts):
                if (atom==atom_all and nrpt==0):
                    pass
                else:
                    # first idx for atom 2 at home cell
                    for n in idx[atom_all]:
                        # second idx for all other atoms and all cells
                        for m in idx[atom]:
                            result += Z[2,MO,n,m,0,nrpt]
                            result += Z[2,MO,m,n,nrpt,0]
        Z_decompose.append(result)

        #NC
        result = 0.0+1j*0.0
        for atom in range(5):
            for nrpt in range(nrpts):
                for atom_1 in range(5):
                    for nrpt_1 in range(nrpts):
                        if ((atom==atom_all and nrpt==0) or (atom_1==atom_all
                                                             and nrpt_1==0) or (atom==atom_1 and nrpt==nrpt_1)):
                            pass
                        else:
                            for n in idx[atom]:
                                for m in idx[atom_1]:
                                    result += Z[2,MO,n,m,nrpt,nrpt_1]
        Z_decompose.append(result)
        
        print(f"CT: {2*np.array(Z_decompose).real[1]}") 
        print(f"LP: {2*np.array(Z_decompose).real[2]}")
        print(f"COV: {2*np.array(Z_decompose).real[3]}")
        print(f"NC: {2*np.array(Z_decompose).real[4]}")
        #  print(np.sum(np.array(Z_decompose).real))
        Z_total += np.sum(np.array(Z_decompose).real[1:])
print("Total Z (electronic part):",2*Z_total)
print("Total Z (ionic part):",4)
print("Total Z (total):",2*Z_total+4)
