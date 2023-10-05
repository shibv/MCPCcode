import numpy as np


r = 12323 # the lengths of h0, h1
w = 142   # odd weight
t = 134   # the error-correction threshold
H0 = []
H1 = []

def gen_h0h1():
    num_zeroes = int(r - (w / 2))
    num_ones = int(w / 2)
    # print(num_ones, num_zeroes)
    h0 = np.array([0] * num_zeroes + [1] * num_ones)
    h1 = np.array([0] * num_zeroes + [1] * num_ones)
    np.random.shuffle(h0)
    np.random.shuffle(h1)
    return (h0, h1)

def right_circular_shift(h0, h1):
    for _ in range(r):
        H0.append(list(h0))
        np.roll(h0,1)
    
    for _ in range(r):
        H1.append(list(h1))
        np.roll(h1,1)
    
    print(H0)
    # det = np.linalg.det(H0)
    # np.linalg.det(det)
    # print(H0)

    return (H0,H1)
    







def gen_H(H0, H1):
    H = np.concatenate((H0, H1))
    return H

def gen_Q(H0, H1):
    H1_inv = np.linalg.inv(H1)
    
    Q =  np.matmul(H1_inv, H0)
    Q.transpose()
    return Q

def gen_G(H0, H1):
    I = np.identity(r)








    

def main():
    h0, h1 = gen_h0h1()
    H0,H1 = right_circular_shift(h0,h1)
    # gen_H(H0,H1)
    # det = np.linalg.det(H0)
    # np.linalg.det(det)
    

main()