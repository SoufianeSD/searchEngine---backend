import csv
import pandas as pd
from getFeautures import getVectorPlacementFromFile, averageDistancesAroundAxe, getMomentInertia,VarienceDistance, getMomentInertiaWithMesh
from scipy.spatial.distance import euclidean


def SimilarityNormalizedCheck(path):
    col_list = ["Name","Mx","My","Mz","Ax","Ay","Az","Dx","Dy","Dz"]
    df = pd.read_csv('Extracted_Feautures_For_Obj.csv',names=col_list)

    Mx_max = df["Mx"].max()
    Mx_min = df["Mx"].min()
    My_max = df["My"].max()
    My_min = df["My"].min()
    Mz_max = df["Mz"].max()
    Mz_min = df["Mz"].min()
    Ax_max = df["Ax"].max()
    Ax_min = df["Ax"].min()
    Ay_max = df["Ay"].max()
    Ay_min = df["Ay"].min()
    Az_max = df["Az"].max()
    Az_min = df["Az"].min()
    Dx_max = df["Dx"].max()
    Dx_min = df["Dx"].min()
    Dy_max = df["Dy"].max()
    Dy_min = df["Dy"].min()
    Dz_max = df["Dz"].max()
    Dz_min = df["Dz"].min()


    # path = "./Models/3DMillenium_bottle01.obj"

    X, Y, Z = getVectorPlacementFromFile(path)
    m = list(getMomentInertiaWithMesh(path))
    a = [averageDistancesAroundAxe(X, Y, Z),averageDistancesAroundAxe(Y, X, Z),averageDistancesAroundAxe(Z, X, Y)]
    d = list(VarienceDistance(path))
    norm_mx = (m[0] - Mx_min)/(Mx_max - Mx_min)
    norm_my = (m[1] - My_min)/(My_max - My_min)
    norm_mz = (m[2] - Mz_min)/(Mz_max - Mz_min)
    norm_ax = (a[0] - Ax_min)/(Ax_max - Ax_min)
    norm_ay = (a[1] - Ay_min)/(Ay_max - Ay_min)
    norm_az = (a[2] - Az_min)/(Az_max - Az_min)
    norm_dx = (d[0] - Dx_min)/(Dx_max - Dx_min)
    norm_dy = (d[1] - Dy_min)/(Dy_max - Dy_min)
    norm_dz = (d[2] - Dz_min)/(Dz_max - Dz_min)
    f = [norm_mx, norm_my, norm_mz, norm_ax, norm_ay, norm_az, norm_dx, norm_dy, norm_dz]
    result = {}
    with open('Normalized_Feautures_For_Obj.csv','r',newline='') as obj:
        reader = csv.reader(obj)
        for row in reader:
            feature = [float(x) for x in row[1:]]
            res = euclidean(f,feature)

            result[row[0]] = res
        obj.close()
    
    return result
# sortedRes = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

# r = list(sortedRes.keys())
# print(r[:12])