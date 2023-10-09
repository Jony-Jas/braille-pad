from flask import Flask, jsonify, request
import BrailleGenerator as BG;
import BraillePad as BP;
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/message', methods=['POST'])
def get_message():
    if request.is_json:
        data = request.get_json()
        res = BG.generateBrailleCode(data["message"])
        print(res)
        BP.run(res)
        return jsonify(data), 200
    else:
        return jsonify({"error": "Request data must be in JSON format"}), 400


if __name__ == '__main__':
   app.run()
