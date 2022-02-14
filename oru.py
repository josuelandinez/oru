#!/usr/bin/env python

import numpy as np

#create matrix unitary vectors
e=np.eye(3, dtype=int)
print(e)
#create example matrix 
a=np.arange(1,10).reshape((3,3))
#a=np.arange(1,10).reshape((3,3)).transpose()
print(a)

#outer product exchange column
print("shape e0", np.shape(e[0,:]))
print("shape e2", np.shape(e[2,:].transpose()))#
#op=np.outer(e[0,:],e[2,:].transpose())
#op=np.outer(e[0,:],e[2,:])

pnew=np.array([25,26,27])
du=pnew-a[0,:]
op=np.outer(e[0,:],du)
print(op)
#au=np.dot((np.eye(3)+op),a)
au=a+op;
print("au",au)

#inverse sherman morrison
# Anew=A+uv'
#
