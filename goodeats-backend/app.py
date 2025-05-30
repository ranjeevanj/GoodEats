from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO


app = Flask(__name__)
model = YOLO("yolov8n.pt")
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    #Grabs file and saves in folder"
    image = request.files.get("image")
    if image is None:
        return jsonify({"error:" "No image file provided"}), 400
    
    image_path = "temp.jpg"
    image.save(image_path)
    results = model(image_path)

    #Detecting items from YOLO
    detected_classes = results[0].boxes.cls.tolist()
    detected_items = [results[0].names[int(cls)] for cls in detected_classes]
    print(image.filename)
    
    return jsonify ({"detected_items": detected_items})


if __name__ == "__main__":
    app.run(debug=True)