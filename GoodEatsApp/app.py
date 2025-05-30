from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    image = request.files.get("image")
    print(image.filename)
    return jsonify({ "message": "Image received" })

if __name__ == "__main__":
    app.run(debug=True)