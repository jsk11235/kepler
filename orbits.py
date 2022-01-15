import matplotlib.pyplot as plt
import math

tick = 0
m= [{
    'm':1.989 * 10**30,
    'p':[0,0],
    'v':[0,0],
    'a':[0,0],
    'r':0.03
},

{
    'm':5.9722 * 10**24,
    'p':[0,-1.496*10**11],
    'v':[30000,0],
    'a':[0,0],
    'r':0.03
},

{
    'm':6.39 * 10**23,
    'p':[0,2.28*10**11],
    'v':[25000,0],
    'a':[0,0],
    'r':0.03
}]

G = 6.67*10**-11

def timePass(t,tick,plotSpacing):
    if tick%plotSpacing==0:
        for idx in range(len(m)):
            plt.plot(m[idx]['p'][0], m[idx]['p'][1], 'bo')
    for idx in range(len(m)):
        netAcc = [0,0]
        for otherObj in range(len(m)):
            if otherObj!=idx:
                x = m[otherObj]['p'][0]-m[idx]['p'][0]
                y = m[otherObj]['p'][1]-m[idx]['p'][1]
                hyp = (x**2+ y**2)**0.5
                newAcc = G*m[otherObj]['m']/(hyp**2)
                netAcc[0] += (x/hyp)* newAcc
                netAcc[1] += (y/hyp)* newAcc
                if hyp<m[otherObj]['r']+m[idx]['r']:
                    return True
        m[idx]['a'][0] = netAcc[0]
        m[idx]['a'][1] = netAcc[1]

    for idx in range(len(m)):
        m[idx]['v'][0]+= m[idx]['a'][0]*t
        m[idx]['v'][1]+= m[idx]['a'][1]*t

    for idx in range(len(m)):
        m[idx]['p'][0]+= m[idx]['v'][0]*t
        m[idx]['p'][1]+= m[idx]['v'][1]*t

for i in range(10000):
    if timePass(8000,tick,100):
        print('impact')
        break
    tick+=1
plt.show()


