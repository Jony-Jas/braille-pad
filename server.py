from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/message', methods=['POST'])
def get_message():
    if request.is_json:
        data = request.get_json()
        print(data["message"])
        return jsonify(data), 200
    else:
        return jsonify({"error": "Request data must be in JSON format"}), 400


if __name__ == '__main__':
   app.run()