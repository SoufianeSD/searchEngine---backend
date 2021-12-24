import cv2,csv
from scipy.spatial.distance import euclidean
from tamura_ import coarseness,contrast,directionality,roughness


def normalize(lst):
    s = sum(lst)
    return list(map(lambda x: float(x)/s, lst))

# function to extract haralick textures from an image
def extract_features(img):
        fcrs = coarseness(img, 5)
    	# print("coarseness: %f" % fcrs);
        fcon = contrast(img)
        #print("contrast: %f" % fcon)
        fdir= directionality(img)
        #print("directionality: %f" % fdir)
        f_r=roughness(fcrs,fcon)
        #print("roughness: %f" % f_r)
    
        return [fcrs,fcon,fdir,f_r]

def checkTheEuclidienDistance(feature,newFeature):
    	return euclidean(feature,newFeature)

def calculeDistance(imageUploaded):
    img = cv2.imread(imageUploaded)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    featuresNewImage = extract_features(gray)
    # print(featuresNewImage)
    result = {}
    with open('Tamura_BreakHis_temp_png.csv','r') as obj:
        reader = csv.reader(obj)
        
        for row in reader:
            feature = [float(x) for x in row[1:]]
            
            res = checkTheEuclidienDistance(feature,featuresNewImage)
            # print(feature)
            result[row[0]] = res

        obj.close()    
        
    return result

def calculeDistanceNormalize(imageUploaded):
	img = cv2.imread(imageUploaded)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	featuresNewImage = normalize(extract_features(gray))
	# print(featuresNewImage)
	result = {}
	with open('Normalized_Tamura_temp_png.csv','r') as obj:
		reader = csv.reader(obj)
		for row in reader:

			feature = [float(x) for x in row[1:]]
            
			res = checkTheEuclidienDistance(feature,featuresNewImage)
			print(feature)
			result[row[0]] = res

		obj.close()	
		
	return result

# res = calculeDistance("D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images\\Backend\\static\\obj1__0.png")
# sortedRes = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}

# result = list(sortedRes.keys())
# print(result[:12])
