import matplotlib.pyplot as plt
import math
m1 = {
    'm':1.989 * 10**30,
    'p':[0,0],
    'v':[0,0],
    'a':[0,0],
    'r':0.03
}

m2 = {
    'm':5.9722 * 10**24,
    'p':[0,1.496*10**11],
    'v':[30000,0],
    'a':[0,0],
    'r':0.03
}

G = 6.67*10**-11

def timePass(t):
    plt.plot(m1['p'][0], m1['p'][1], 'ro')
    plt.plot(m2['p'][0], m2['p'][1], 'bo')
    x = m1['p'][0]-m2['p'][0]
    y = m1['p'][1]-m2['p'][1]
    hyp = (x**2+ y**2)**0.5
    accM1 = G*m2['m']/(hyp**2)
    accM2 = G*m1['m']/(hyp**2)
    m1['a'][0] = (-x/hyp)* accM1
    m1['a'][1] = (-y/hyp)* accM1
    m2['a'][0] = (x/hyp)* accM2
    m2['a'][1] = (y/hyp)* accM2
    m1['v'][0]+= m1['a'][0]*t
    m1['v'][1]+= m1['a'][1]*t
    m2['v'][0]+= m2['a'][0]*t
    m2['v'][1]+= m2['a'][1]*t
    m1['p'][0]+= m1['v'][0]*t
    m1['p'][1]+= m1['v'][1]*t
    m2['p'][0]+= m2['v'][0]*t
    m2['p'][1]+= m2['v'][1]*t
    print(hyp-(m1['r']+m2['r']))
    if hyp<m1['r']+m2['r']:
        return True

for i in range(10000):
    if timePass(8000):
        print('impact')
        break
plt.show()


