import csv
from getFeautures import getVectorPlacementFromFile, averageDistancesAroundAxe, getMomentInertia,VarienceDistance, getMomentInertiaWithMesh
from scipy.spatial.distance import euclidean

# path = "./Models/3DMillenium_bottle01.obj"

# X, Y, Z = getVectorPlacementFromFile(path)
# m = list(getMomentInertiaWithMesh(path))
# a = [averageDistancesAroundAxe(X, Y, Z),averageDistancesAroundAxe(Y, X, Z),averageDistancesAroundAxe(Z, X, Y)]
# d = list(VarienceDistance(path))
# f = [m + a + d]
# result = {}
# with open('Extracted_Feautures_For_Obj.csv','r',newline='') as obj:
#     reader = csv.reader(obj)
#     for row in reader:
#         feature = [float(x) for x in row[1:]]
#         res = euclidean(f,feature)

#         result[row[0]] = res
#     obj.close()

# sortedRes = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

# r = list(sortedRes.keys())
# print(r[:12])

def SimilarityCheck(path,file_data):
    X, Y, Z = getVectorPlacementFromFile(path)
    m = list(getMomentInertiaWithMesh(path))
    a = [averageDistancesAroundAxe(X, Y, Z),averageDistancesAroundAxe(Y, X, Z),averageDistancesAroundAxe(Z, X, Y)]
    d = list(VarienceDistance(path))
    f = [m + a + d]
    result = {}
    with open(file_data,'r',newline='') as obj:
        reader = csv.reader(obj)
        for row in reader:
            feature = [float(x) for x in row[1:]]
            res = euclidean(f,feature)

            result[row[0]] = res
        obj.close()
    
    return result