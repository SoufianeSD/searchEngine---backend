from math import sqrt
import trimesh

def getVectorPlacementFromFile(path):
    l = []
    with open(path,'r') as obj:
        for line in obj.readlines():
            if line.strip().split(' ')[0] == 'v':
                l.append([float(x) for x in line.strip().split(' ')[1:]])
    coordX = [item[0] for item in l]
    coordY = [item[1] for item in l]
    coordZ = [item[2] for item in l]
    return coordX,coordY,coordZ




def averageDistancesAroundAxe(x,y,z):
    r = 0
    for i in range(len(x)):
        r += sqrt(y[i]**2 + z[i]**2)

    average = r/len(x)

    return average


def getMomentInertia(x,y,z):
    X = Y = Z = 0
    for i in range(len(x)):
        X += y[i]**2 + z[i]**2
        Y += x[i]**2 + z[i]**2
        Z += x[i]**2 + y[i]**2    
    Ix = X/len(x)
    Iy = Y/len(y)
    Iz = Z/len(z)
    
    return Ix,Iy,Iz

def getMomentInertiaWithMesh(path):

    mesh = trimesh.load_mesh(path)
    X = mesh.moment_inertia[0][0]
    Y = mesh.moment_inertia[1][1]
    Z = mesh.moment_inertia[2][2]
    
    return X,Y,Z

def VarienceDistance(path):
    X, Y, Z = getVectorPlacementFromFile(path)
    avgX = averageDistancesAroundAxe(X, Y, Z)
    avgY = averageDistancesAroundAxe(Y, X, Z)
    avgZ = averageDistancesAroundAxe(Z, X, Y)
    Dx = VarienceFormula(X,Y,Z,avgX)
    Dy = VarienceFormula(Y,X,Z,avgY)
    Dz = VarienceFormula(Z,X,Y,avgZ)

    return Dx, Dy, Dz


def VarienceFormula(X,Y,Z,avg):
    s = 0
    for i in range(len(X)):
        s += (sqrt(Y[i]**2 + Z[i]**2) - avg)**2
    
    D = s/(len(X) - 1)
    return D