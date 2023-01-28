from __future__ import print_function  

import matplotlib.pyplot as plt
import sys



def plot_zipf(filename):
    d = {}     
    h=0                                      
    with open(filename,"r", encoding="utf-8") as f:
        for line in f:
            w =[j.strip(',.-_?! ').lower() for j in line.strip().split()]
            for i in w:
                if i != '':
                    h=d.get(i, 0)
                    d[i]=h+1
                  
                                    
    data = sorted(d.values(), reverse=True)          
    plt.loglog(range(1, len(data)+1), data)          
    plt.show()                                       

    print(sorted(d.items(), key=lambda x:x[1], reverse=True)[0:10])

def main():
    plot_zipf(filename)

if __name__ == "__main__":
    filename = sys.argv[1]
    main()
    

