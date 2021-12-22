import glob
import cv2,csv
import pickle
import mahotas as mt
from mahotas import features
from scipy.spatial.distance import euclidean

# filename = "D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images\\model.sav"
# loaded_model = pickle.load(open(filename, 'rb'))


# function to extract haralick textures from an image
def extract_features(image):
    # calculate haralick texture features for 4 types of adjacency
    textures = mt.features.haralick(image)

    # take the mean of it and return it
    ht_mean  = textures.mean(axis=0)
    return ht_mean

def checkTheEuclidienDistance(feature,newFeature):
    	return euclidean(feature,newFeature)

def calculeDistance(imageUploaded):
	img = cv2.imread(imageUploaded)
    
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
	featuresNewImage = extract_features(gray)
	result = {}
	print(featuresNewImage)
	with open('Haralick_BreaKHis_temp.csv','r') as obj:
		reader = csv.reader(obj)
		for row in reader:
    			
			feature = float(row[1])
			res = checkTheEuclidienDistance(feature,featuresNewImage[0])
			result[row[0]] = res

		obj.close()	
		
	return result

res = calculeDistance("D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images\\Backend\\static\\obj1__15.ppm")
sortedRes = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}
print(sortedRes)

