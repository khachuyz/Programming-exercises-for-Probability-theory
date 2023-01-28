from math import comb
import math


class Drv:
    """
    Define a class for discrete random variables

    xk is a list of monoton increasing values
    pk is the list of probabilities belonging to xk
    """

    name = "Discrete random variable"    

    def __init__(self, xk=[0], pk=[1]):
        self.xk = xk                   
        self.pk = pk                   

    def pdf(self, x):
        """
        Return the value of the probability density function at x.
        x:: any real number
        """
        
        for i in range(len(self.xk)):
            if x==self.xk[i]:
                return self.pk[i]
        return 0    
        pass 

    def cdf(self, x):
        """
        Return the value of the cumulative distribution function at x.
        x:: any real number
        """
        return math.fsum([self.pk[j] for j in range(len(self.xk)) if x > self.xk[j]])
            
        pass

    def e(self):
        """
        Return the expected value of the discrete random variable.
        """
        return math.fsum([self.xk[a]*self.pk[a] for a in range(len(self.xk))])
        
        pass
    

    def is_nonneg(self):
        """
        Return True if the random variable is non negative.
        Otherwise False.
        """       
        return all((a>=0 for a in self.xk))
        
        pass 

    def reweight(self):
        """
        Reweighting a random variable using the expected 
        value of the random variable. 
        """
        
        self.yk=[((self.xk[b])*(self.pk[b]))/self.e() for b in range(len(self.xk))]
        class weight(Drv):
            def __init__(self, xk, pk):
                super().__init__(xk, pk)
        return weight(self.xk,self.yk)
            
    
        pass

    def __repr__(self):
        xk = self.xk
        pk = self.pk
        n = len(xk)
        x = '' . join(['('+str(xk[l]) + ', ' + str(pk[l]) + ') '
                      for l in range(min(n, 10))])
        if n > 10:
            x += '...'
        return self.name + ": " + x


class Binomial(Drv):
    """
    Class for binomial random variable derives from Drv.
    Parameters needed: n, p.
    """

    name = "Binomial random variable"

    def __init__(self, n=1, p=1):
        self.n = n
        self.p = p
        values=[k for k in range(0,n+1)]
        probabilities=[comb(n, k)*(p**k)*((1-p)**(n-k)) for k in range(0,n+1)]
        super().__init__(values, probabilities) 

    def e(self):
        return (self.n)*(self.p)
        pass 

    def is_nonneg(self):
        
        return True


class Uniform(Drv):
    """
    Class for a uniform random variable derives from Drv.
    n is the number a values (which are 1,2,...,n).
    """

    name = "Uniform random variable"

    def __init__(self, n=1):
        self.n = n
        value=[d for d in range(1,n+1)]
        probability=[1/n]*n
        super().__init__(value, probability)

    def e(self):
        """
        Return the expected value of the uniform random variable.
        """
        return (self.n+1)/2
        pass 

    def is_nonneg(self):
        return True
    
    
    