#13 texture features are extracted from this

import cv2
import numpy as np
import os
import glob
import mahotas as mt
#from sklearn.svm import LinearSVC
import csv
import time
#import pickle

tic = time.time()

# function to extract haralick textures from an image
def extract_features(image):
    # calculate haralick texture features for 4 types of adjacency
    textures = mt.features.haralick(image)
    
    # take the mean of it and return it
    ht_mean  = textures.mean(axis=0)
    return ht_mean

# load the training dataset
train_path  = "C:\\Users\\Probook\\Desktop\\Master SIM\\S3\\Analysis, Mining and Indexing in big multimedia systems\\searchEngine---backend\\Backend\\dataset\\coil-100" #Enter the directory where all the images are stored
train_names = os.listdir(train_path)
# train_names = [] 

# for name in train_names_all:
#     train_names.append(name.split("_")[0])

#
# empty list to hold feature vectors and train labels
train_features = []
train_labels   = []

# loop over the training dataset
print ("[STATUS] Started extracting haralick textures..")
cur_path = os.path.join(train_path, '*g')
#cur_path = os.path.join(train_path, '*.ppm')
cur_label = train_names
i = 0
with open('Haralick_BreaKHis_temp_png.csv','w',newline='') as obj:
                writer = csv.writer(obj)
                # if i==0:
                #         writer.writerow(['Haralick1','Haralick2','Haralick3','Haralick4','Haralick5','Haralick6','Haralick7','Haralick8','Haralick9',
                #                          'Haralick10','Haralick11','Haralick12','Haralick13'])
                for file in glob.glob(cur_path):
                    print ("Processing Image - {} in {}".format(i, cur_label[i]))
                    #read the training image
                    image=cv2.imread(file)

                    #convert the image to grayscale
                    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                    
                    #extract haralick texture from image
                    features=extract_features(gray)
                    
                    #append the feature vector and label
                    train_features.append(features)
                    train_labels.append(cur_label[i])
                    

                    features = [str(f) for f in features]
                    writer.writerow([cur_label[i]] + list(features))
                    #writer.writerow(features)
                    #show loop update
                    i+=1

    
# have a look at the size of our feature vector and labels
print ("Training features: {}".format(np.array(train_features).shape))
print ("Training labels: {}".format(np.array(train_labels).shape))

# # create the classifier
# print("[STATUS] Creating the classifier..")
# clf_svm = LinearSVC(random_state=9)

# # fit the training data and labels
# print("[STATUS] Fitting data/label to model..")
# clf_svm.fit(train_features, train_labels)

# #save the model
# filename = "model.sav"
# pickle.dump(clf_svm,open(filename, 'wb'))

# # loop over the test images
# test_path = "D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images\\Backend\\dataset\\test"
# for file in glob.glob(test_path + "*f"):
# 	# read the input image
# 	image = cv2.imread(file)

# 	# convert to grayscale
# 	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 	# extract haralick texture from the image
# 	features = extract_features(gray)

# 	# evaluate the model and predict label
# 	prediction = clf_svm.predict(features.reshape(1, -1))[0]

# 	# show the label
# 	cv2.putText(image, prediction, (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255), 3)
# 	print("Prediction - {}".format(prediction))

# 	# display the output image
# 	cv2.imshow("Test_Image", image)
# 	cv2.waitKey(0)

# toc = time.time()
# print("Computation time is {} minutes.".format((toc-tic)/60))