import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

tick = 0
m= [
{
    'm':1.989 * 10**30,
    'p':[0,0,0],
    'v':[0,0,0],
    'a':[0,0,0],
    'r':6.96*10**8,
    'c':'000000',
    'n':'sun'
},

{
    'm':6.39 * 10**23,
    'p':[0,2.28*10**11,0],
    'v':[25000,0,0],
    'a':[0,0,0],
    'r':3.38*10**6,
    'c':'r',
    'n':'mars'
},

{
    'm':5.9722 * 10**24,
    'p':[0,-1.496*10**11,0],
    'v':[0,0,30000],
    'a':[0,0,0],
    'r':6.3781*10**6,
    'c':'#BBBBBB',
    'n':'USA'
}]

G = 6.67*10**-11

def timePass(t,tick,plotSpacing):
    if tick%plotSpacing==0:
        for idx in range(len(m)):
            plt.plot(m[idx]['p'][0], m[idx]['p'][1],m[idx]['p'][2], color=m[idx]['c'], marker='o',markersize=3)
            if tick==0:
                ax.text(m[idx]['p'][0], m[idx]['p'][1],m[idx]['p'][2],m[idx]['n'])
    for idx in range(len(m)):
        netAcc = [0,0,0]
        for otherObj in range(len(m)):
            if otherObj!=idx:
                x = m[otherObj]['p'][0]-m[idx]['p'][0]
                y = m[otherObj]['p'][1]-m[idx]['p'][1]
                z = m[otherObj]['p'][2]-m[idx]['p'][2]
                hyp = (x**2+ y**2 + z**2)**0.5
                newAcc = G*m[otherObj]['m']/(hyp**2)
                netAcc[0] += (x/hyp)* newAcc
                netAcc[1] += (y/hyp)* newAcc
                netAcc[2] += (z/hyp)* newAcc
                if hyp<m[otherObj]['r']+m[idx]['r']:
                    del m[otherObj]
                    del m[idx]
                    return True
        m[idx]['a'][0] = netAcc[0]
        m[idx]['a'][1] = netAcc[1]
        m[idx]['a'][2] = netAcc[2]

    for idx in range(len(m)):
        m[idx]['v'][0]+= m[idx]['a'][0]*t
        m[idx]['v'][1]+= m[idx]['a'][1]*t
        m[idx]['v'][2]+= m[idx]['a'][2]*t

    for idx in range(len(m)):
        m[idx]['p'][0]+= m[idx]['v'][0]*t
        m[idx]['p'][1]+= m[idx]['v'][1]*t
        m[idx]['p'][2]+= m[idx]['v'][2]*t

for i in range(10000):
    if timePass(8000,tick,100):
        print('impact')
    tick+=1
plt.show()
