import pickle
from flask import Flask, request, jsonify
from src.nlpMatch import nlpMatch

app = Flask(__name__)
model = pickle.load(open('./model.pkl', 'rb'))

@app.route('/', methods=["GET"])
def home():
    data = request.get_json()
    codeArr = data["codeArr"]
    figmaArr = data["figmaArr"]
    mappings = nlpMatch(codeArr, figmaArr, model)
    return jsonify({'match': mappings})