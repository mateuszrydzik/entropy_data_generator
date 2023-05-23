from data_generator import DataGenerator
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

@app.route('/data_generator', methods=['POST'])
def data_generator():
    req = request.get_json()

    entropy = float(req['entropy'])
    nclass = int(req['nclass'])

    if (dim := req['dim']) == "":
        dim = 8
      
    data_generator = DataGenerator(entropy=entropy, nclass=nclass, dim=int(dim))
    matrix = data_generator.generate()
    df = pd.DataFrame(matrix)
    df_json = df.to_json(orient='values')

    return jsonify({"matrix": df_json}), 200