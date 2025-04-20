from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def greet():
    return jsonify({"message":"Just Started..."})


if __name__ == "__main__":
    flask.run()

