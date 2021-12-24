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
	featuresNewImage = [float(y) for y in featuresNewImage]
	# print(featuresNewImage)
	result = {}
	with open('Haralick_BreaKHis_temp_png.csv','r') as obj:
		reader = csv.reader(obj)
		for row in reader:

			feature = [float(x) for x in row[1:]]
			res = checkTheEuclidienDistance(feature,featuresNewImage)
			result[row[0]] = res

		obj.close()	
		
	return result

res = calculeDistance("C:\\Users\\Probook\\Desktop\\Master SIM\\S3\\Analysis, Mining and Indexing in big multimedia systems\\searchEngine---backend\\Backend\\static\\obj1__0.png")
sortedRes = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}
# print(sortedRes["obj1__0.png"])

result = list(sortedRes.keys())
print(result[:12])




# # loop over the test images
# test_path = "D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images\\Backend\\static"
# for file in glob.glob(test_path + "\\*m"):
# 	# read the input image
# 	image = cv2.imread(file)

# 	# convert to grayscale
# 	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
# 	# extract haralick texture from the image
# 	features = extract_features(gray)

# 	# evaluate the model and predict label
# 	prediction = loaded_model.predict(features.reshape(1, -1))[0]
    
# 	# show the label
# 	cv2.putText(image, prediction, (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255), 3)
# 	print("Prediction - {}".format(prediction))
    