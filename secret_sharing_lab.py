# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from vec import Vec



## 1: (Task 7.7.1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    secret_list=[0 for x in range(0,6)]	    
    
    #print ("Init1")
    for i in range(0,6):
        secret_list[i]=randGF2();

    secret_vec=list2vec(secret_list)

    #print ("Init2")
    while (a0*secret_vec!=s or b0*secret_vec!=t): #Dont use AND because the while loop should go as long as even one of the conditions is true
        for i in range(0,6):
            secret_list[i]=randGF2()
        
        #print ("Iteration")
        secret_vec=list2vec(secret_list)

    return secret_vec  




## 2: (Task 7.7.2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance
"""secret_a0 = ...
secret_b0 = ...
secret_a1 = ...
secret_b1 = ...
secret_a2 = ...
secret_b2 = ...
secret_a3 = ...
secret_b3 = ...
secret_a4 = ...
secret_b4 = ...
"""
