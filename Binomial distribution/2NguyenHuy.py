import matplotlib.pyplot as plt
import numpy as np
import math
import sys


def binodis(n, p, k):

    binom=[math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(n+1)]

    simul=[math.fsum(np.random.binomial(n, p, k)==l) for l in range(n+1)]
    
    lambd=n*p
    poisson=[lambd**j*math.exp(-lambd)/math.factorial(j) for j in range(n+2)]
        
    plt.figure(figsize=(12, 3))
    
    plt.subplot(131)                         
    plt.bar(list(range(n+1)),binom)
    plt.title('Binomial Distribution')
    
    plt.subplot(132)                          
    plt.bar(list(range(n+1)),simul)
    plt.title('Simulated binomial distribution')
    
    plt.subplot(133)                         
    plt.bar(list(range(n+2)),poisson)
    plt.title('Approximated with Poisson-distribution')
    
    plt.show()
    
    
if __name__ == "__main__":
    n=int(sys.argv[1])
    p=float(sys.argv[2])
    k=int(sys.argv[3])
    binodis(n, p, k)
    


