from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def healthCheckResponse():
    return jsonify({"message" : "Nothing here, used for health check. Try /api instead."})

@app.route("/api")
def getResponse():
    # read the JSON from the listed file.
    response = Response(open("test-data.json", "rb").read())
    response.headers["Content-Type"]= "application/json"

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    