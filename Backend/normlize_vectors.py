import glob
import csv,cv2
import pandas as pd
import os


def normalize(lst):
    s = sum(lst)
    return list(map(lambda x: float(x)/s, lst))

# def fnct(df):
#     df.columns = range(df.shape[1])
#     df = df.apply()
#     sum = float(i)/sum()
       
# load the training dataset
train_path  = "C:\\Users\\Probook\\Desktop\\Master SIM\\S3\\Analysis, Mining and Indexing in big multimedia systems\\searchEngine---backend\\Backend\\static\\dataset\\coil-100"
train_names = os.listdir(train_path)

# loop over the training dataset
cur_path = os.path.join(train_path, '*g')
cur_label = train_names
i = 0

df = pd.read_csv("Tamura_BreaKHis_temp_png.csv",names=['Object_Name','coarseness','contrast','directionality','roughness'])


#df[['coarseness','contrast','directionality','roughness']] = normalize(df[['coarseness','contrast','directionality','roughness']])

#df[['coarseness','contrast','directionality','roughness']] = df[['coarseness','contrast','directionality','roughness']].apply([float(i)/sum(df[['coarseness','contrast','directionality','roughness']]) for i in df[['coarseness','contrast','directionality','roughness']]])

# for index, row in df.iterrows():
#     print(index)
#     if index != 0:
#         df[['coarseness','contrast','directionality','roughness']][index] = [float(i)/sum(row[1:]) for i in row[1:]]
        
with open('Normalized_Tamura_temp_png.csv','w',newline='') as obj:
    csv_writer = csv.writer(obj,delimiter=",")
    for index, row in df.iterrows():
        print(index)
        if index != 0:
            norm= [float(i)/sum(row[1:]) for i in row[1:]]
        
            csv_writer.writerow([row[0]] + norm)
            obj.flush()
    obj.close()


# print("-------------------------------")
# print(df)

# df.to_csv("Normalized_Tamura_temp_png.csv")
