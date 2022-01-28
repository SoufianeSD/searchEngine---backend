import csv
import pandas as pd
from sqlalchemy import column

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

with open('Normalized_Feautures_For_Obj.csv','w',newline='') as obj:
    csv_writer = csv.writer(obj,delimiter=",")
    for index, row in df.iterrows():
        print(index)
        if index != 0:
            norm_mx = (row[1] - Mx_min)/(Mx_max - Mx_min)
            norm_my = (row[2] - My_min)/(My_max - My_min)
            norm_mz = (row[3] - Mz_min)/(Mz_max - Mz_min)
            norm_ax = (row[4] - Ax_min)/(Ax_max - Ax_min)
            norm_ay = (row[5] - Ay_min)/(Ay_max - Ay_min)
            norm_az = (row[6] - Az_min)/(Az_max - Az_min)
            norm_dx = (row[7] - Dx_min)/(Dx_max - Dx_min)
            norm_dy = (row[8] - Dy_min)/(Dy_max - Dy_min)
            norm_dz = (row[9] - Dz_min)/(Dz_max - Dz_min)

            csv_writer.writerow([row[0]] + [norm_mx, norm_my, norm_mz, norm_ax, norm_ay, norm_az, norm_dx, norm_dy, norm_dz])
            obj.flush()
    obj.close()