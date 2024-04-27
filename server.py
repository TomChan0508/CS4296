import os
import time
import boto3
import tempfile
import joblib
from tensorflow import keras
import numpy as np
from flask import Flask, request, jsonify
from PIL import Image

app = Flask('predict')

# AWS S3 bucket parameters
BUCKET_NAME = 'jas01' 
model_name = 'model.h5'

# Start an S3 client
s3_client = boto3.client('s3')

global model, class_names

#the name of the image
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

#import model form s3 
with tempfile.TemporaryFile() as fp:
    s3_client.download_fileobj(
        Fileobj=fp, 
        Bucket=BUCKET_NAME, 
        Key=model_name
    )
    fp.seek(0)
    model = joblib.load(fp)
print('Model loaded successfully')


@app.route('/upload', methods=['POST'])
def upload():
    start_time = time.time()
    # Check if the 'image' file is present in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'})

    test_image = request.files['image']

    # Check if the file is empty
    if test_image.filename == '':
        return jsonify({'error': 'Empty file name'})

    # Preprocess the image file
    img = Image.open(test_image)
    img = img.resize((28, 28))  # Resize to match the input size expected by the model
    img = img.convert('L')  # Convert to grayscale
    img_array = np.array(img)  # Convert image to numpy array
    img_array = img_array / 255.0  # Normalize the pixel values (if required)

    # Expand dimensions to match the input shape expected by the model
    img_array = np.expand_dims(img_array, axis=0)
    img_array = np.expand_dims(img_array, axis=3)

    probability_model = keras.Sequential([model, 
                                         keras.layers.Softmax()])
    # Perform the prediction
    predictions = probability_model.predict(img_array)
    result = class_names[np.argmax(predictions[0])]

    end_time = time.time()
    run_time = end_time - start_time
    
    response = {
        'filename': test_image.filename,
        'predicted_class': result,
        'time': run_time
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)