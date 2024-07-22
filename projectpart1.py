from flask import Flask, request, jsonify

import csv 

app = Flask(__name__)

def getName(csv_file, file_name):
    with open(csv_file,'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Image']==file_name:
                return row['Results']
            
@app.route('/', methods=['POST'])
def post_data():
    request_data = request.get_json()
    file_name = request_data['file_name']
    print(file_name)
    result = getName('Classification_Results.csv', file_name)
    response_data = {'name':result,'status':'Success'}
    return jsonify(response_data)

