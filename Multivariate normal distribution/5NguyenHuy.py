import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from numpy.linalg import eig

def eigsort(cov):
    vals,vecs=eig(cov)
    order = vals.argsort()[::-1]
    return vals[order], vecs[:, order]

def cov_ellipse(points, cov):
    vals, vecs = eigsort(cov)
    theta = np.degrees(np.arctan2(*vecs[:, 0][::-1]))
    width, height = 6 * np.sqrt(vals)

    return width, height, theta

def Elle():
    transformation_matrix = np.array(input_nums)

    random_points = np.array([np.random.normal(size = 1000),np.random.normal(size=1000)])

    res_1 = (transformation_matrix.dot(random_points))


    cov_matrix = np.matmul(transformation_matrix,transformation_matrix.T)

    res_2 = np.random.multivariate_normal(mean = (0,0), cov = cov_matrix, size = 1000).T
    
    width1, height1, theta1 = cov_ellipse(res_1, cov_matrix)
    width2, height2, theta2 = cov_ellipse(res_2, cov_matrix)


    f, (ax1,ax2) = plt.subplots(1,2, figsize = (12,6))
    ax1.scatter(res_1[0], res_1[1], marker = 'x', c = 'r')
    ax2.scatter(res_2[0], res_2[1], marker = 'x', c = 'b')
    ell1=Ellipse(xy=(0,0),width=width1,height=height1,angle=theta1, edgecolor='b', facecolor='none')
    ax1.add_patch(ell1)  
    
    ell2=Ellipse(xy=(0,0),width=width2,height=height2,angle=theta2, edgecolor='r', facecolor='none')
    ax2.add_patch(ell2)
           
    plt.show()
    
if __name__ == "__main__":
    input_nums = [[int(sys.argv[1]), int(sys.argv[2])],[int(sys.argv[3]), int(sys.argv[4])]]
    Elle()
    
