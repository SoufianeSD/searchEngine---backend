from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_restful import Api
from flask_cors import CORS
import os
from test3 import calculeDistanceNormalize
from test3 import calculeDistance
from Backend.OBJ_Similarity import SimilarityCheck

UPLOAD_FOLDER = 'D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images_2021\\searchEngine---backend\\Backend\\static'
DATA_FOLDER = 'Backend\dataset\coil-100'

app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploader' , methods = ['GET' , 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    res = calculeDistance("D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images_2021\\searchEngine---backend\\Backend\\static\\"+filename)
    sortedRes = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}
    result = list(sortedRes.keys())
    return "/".join(result[:12]), 201, {'Access-Control-Allow-Origin': '*'}

@app.route('/uploader-normalize' , methods = ['GET' , 'POST'])
def upload_Normalize_file():
    if request.method == 'POST':
        f = request.files['image']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    res = calculeDistanceNormalize("D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images_2021\\searchEngine---backend\\Backend\\static\\"+filename)
    sortedRes = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}
    result = list(sortedRes.keys())
    return "/".join(result[:12]), 201, {'Access-Control-Allow-Origin': '*'}

@app.route('/uploader-3d' , methods = ['GET' , 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    res = SimilarityCheck("D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images_2021\\searchEngine---backend\\Backend\\static\\"+filename,'Extracted_Feautures_For_Obj.csv')
    sortedRes = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}
    result = list(sortedRes.keys())
    return "/".join(result[:12]), 201, {'Access-Control-Allow-Origin': '*'}

@app.route('/uploader-normalize-3d' , methods = ['GET' , 'POST'])
def upload_Normalize_file():
    if request.method == 'POST':
        f = request.files['image']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    res = SimilarityCheck("D:\\_Master MBD\\S3\\traitement des images\\Mini_Projet_Traitement_Images_2021\\searchEngine---backend\\Backend\\static\\"+filename,'Normalized_Feautures_For_Obj.csv')
    sortedRes = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}
    result = list(sortedRes.keys())
    return "/".join(result[:12]), 201, {'Access-Control-Allow-Origin': '*'}

if __name__ == '__main__':
   app.run(debug=True)