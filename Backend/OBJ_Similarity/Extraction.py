import csv
from getFeautures import getVectorPlacementFromFile, averageDistancesAroundAxe, getMomentInertia,VarienceDistance, getMomentInertiaWithMesh
import os



train_path  = "./Models"
train_names = os.listdir(train_path)

print(len(train_names))

with open('Extracted_Feautures_For_Obj.csv','w',newline='') as obj:
    writer = csv.writer(obj,delimiter=",")
    for name in train_names:
        path = train_path + "/" + name
        X, Y, Z = getVectorPlacementFromFile(path)
        m = list(getMomentInertiaWithMesh(path))
        a = [averageDistancesAroundAxe(X, Y, Z),averageDistancesAroundAxe(Y, X, Z),averageDistancesAroundAxe(Z, X, Y)]
        d = list(VarienceDistance(path))
        writer.writerow([name] + m + a + d)
    obj.close()
