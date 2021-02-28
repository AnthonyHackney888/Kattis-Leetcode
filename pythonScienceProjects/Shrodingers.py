import matplotlib.pyplot as plt
import scipy as sp
import numpy as math

h = 6.626e-34 #plank constant
m= 9.11e-31#mass of an electron
x_list = math.linspace(0,1,100)
L = 1#the atomic weight of hydrogen

def psi(n,L,x):
    return math.sqrt(2/L)*math.sin(n*math.pi*x/L)
def psi_2(n,L,x):
    return math.square(psi(n,L,x))

"""
    1-dimension graphs of three different excitment levels
    |         |
    |---------|
    |         |
    0         L
""" 
for n in range(1,4):
    psi_2_list = []
    psi_list = []
    for x in x_list:
        psi_2_list.append(psi_2(n,L,x))
        psi_list.append(psi(n,L,x))
    plt.subplot(3,2,2*n-1)
    plt.plot(x_list, psi_list)
    plt.xlabel("L", fontsize=13)
    plt.ylabel("Ψ", fontsize=13)
    plt.xticks(math.arange(0, 1, step=0.5))
    plt.title("n="+str(n), fontsize=16)
    plt.grid()
       
    
    plt.subplot(3,2,2*n)
    plt.plot(x_list, psi_2_list)
    plt.xlabel("L", fontsize=13)
    plt.ylabel("Ψ*Ψ", fontsize=13)
    plt.xticks(math.arange(0, 1, step=0.5))
    plt.title("n="+str(n), fontsize=16)
    plt.grid()

plt.show()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#probability od 1s

def props(x,y,z):
    r = math.sqrt(math.square(x)+math.square(y)+math.square(z))
    return math.square(math.exp(-r)/math.sqrt(math.pi))

x=math.linspace(0,1,30)
y=math.linspace(0,1,30)
z=math.linspace(0,1,30)

elements = []
probability = []

for i in x:
    for j in y:
        for k in z:
            elements.append(str((i,j,k)))
            probability.append(props(i,j,k))
probability = probability/sum(probability)

coord = math.random.choice(elements, size=10000,replace = True, p=probability)
elem = [i.split(',') for i in coord]
elem = math.matrix(elem)
x_cord = [float(i.item() [1:]) for i in elem[:,0]]
y_cord = [float(i.item() ) for i in elem[:,1]]
z_cord = [float(i.item() [0:-1]) for i in elem[:,2]]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111,projection='3d')
ax.scatter(x_cord,y_cord,z_cord,alpha=0.05,s=2)
ax.set_title("Hydrogen 1s density")
plt.show()
def energies(n):
    
    L=1#L=1 as if it did not then the particle would be outside the box
    m = pow(9.1093837015,pow(10,-31))
    h =pow(4.135667696,pow(10,-15))
    E = pow(n,2)*pow(h,2)/(8*m*pow(L,2))

    return E
#plt.plot(energies(2),)
#plt.show()
def measuingHydrogen():
    Z = 1 #hydrogen
    a = pow(5.29177210903,pow(10,-11))
    p = Z/a
    rho = (1/math.sqrt(math.pi)) * (pow((Z/a),3/2) * math.exp(-p))
    return rho
#plt.plot(measuingHydrogen(),[1,2,3,4])
#plt.show()
def preliminaries():
    A=1 #constant
    B=0 #Constant
    x=0 #position
    Vx=0  #potential energy and goes to infinity
          #which could be the bounds of the graphs
  

    E=0 #energy
    mass=0  #mass of the partive
    h =pow(4.135667696,pow(10,-15))
    k = pow((8 *pow(math.pi,2)* mass*E /pow(h,2)),1/2)
    plankConst = pow(6.582119569, pow(10,-16)) #reduced planks constant in eV/s which can also be represented as hbar
    sigmaX = A* math.sin(k*x) + B* math.cos(k*x) #Wavefuntion that is time-independant
   
    """
    defining k can be quite annoying
    its the derivative of d sigma/d x = kAcos(kx)
    d^2 sigma/d x^2 = -k^2Acos(kx)
    compare that to the shrodinger equation k = (8pi^2mE/h^2)^1/2
    sigma then 
    """
