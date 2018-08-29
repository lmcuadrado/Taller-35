import numpy as np
import matplotlib.pylab as plt

x=np.linspace(-1,1,100)
N=10000
Np=100000
a=0.1
b=1.0
h=(b-a)/(N-1)

def fun(x):
	f=(1.0/8.0)*(35*(x**4)-30*(x**2)+3)
	return f

#plt.plot(x,fun(x))
#plt.show()

def IntTrap(x):
	integra1= np.sum((fun(x)[0])*h/2)+((fun(x)[-1])*h/2)
	integra2= np.sum((fun(x)[1:-1])*h)
	integral= integra1 + integra2
	return integral

f=IntTrap(x)
print f

#def neg(x):

#def pos(x):

fneg=[]
fpos=[]

for i in range (len(x)):
	
	if fun(x)[i]<0:
		fn=fun(x)[i]
		fneg.append(fn)
		
	else:
		fp=fun(x)[i]
		fpos.append(fp)
		 
	
plt.plot(x,fneg)
plt.show()


