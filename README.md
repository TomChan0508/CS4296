=====================================================================

**CS4296 Project**

This project can provide a server using AWS so that the client can obtain the results of the model.

=====================================================================

=====================================================================

**Flask Client**

This is a Python client code that sends a POST request to a Flask server running on a specified IP address. 
The client code uploads an image file to the server for further processing. It uses the requests library to handle the HTTP requests.

**Prerequisites**

Python 3.10

requests library

**Setup**

Clone or download the repository to your local machine.

Install the required dependencies by running the following command:

pip install requests

**Usage**

Run the Flask server: Before running the client code, make sure the Flask server is up and running on the specified IP address. The server should be configured to handle the /upload endpoint.

Open the client.py file in a text editor.

Modify the server_ip variable: Enter the IP address of the Flask server in the server_ip variable. This should be the IP address where the server is running.

Provide the image file: Place the image file you want to upload in the same directory as the client.py file. Update the image_path variable with the filename of your image file.

Run the client code: Open a terminal or command prompt, navigate to the directory where the client.py file is located, and run the following command:

python client.py

The client code will send a POST request to the Flask server with the image file. It will receive the server's response and print the classification results if the request is successful.

**Note:** If the server is not running or the specified IP address is incorrect, an error message will be displayed.

=====================================================================

=====================================================================

**Fashion MNIST Image Classification API with Flask and AWS S3 (Flask Server)**

This is a Python code that demonstrates how to create an API using Flask for image classification using a pre-trained model. 

The code loads a pre-trained model from an AWS S3 bucket, accepts an image file upload, preprocesses the image, performs classification using the model, and returns the predicted class along with the processing time.

**Prerequisites**

Python 3.10

Flask

Boto3

TensorFlow

Numpy

PIL (Pillow)

**Setup**

Clone or download the repository to your local machine.

Install the required dependencies by running the following command:

pip install flask boto3 tensorflow numpy pillow

Configure AWS credentials: Make sure you have your AWS credentials configured on your local machine or the environment where you'll be running the code.

Configure AWS S3 bucket: Set the BUCKET_NAME variable in the code to the name of your AWS S3 bucket. This is the bucket where the pre-trained model is stored.

Run the Flask server: Open a terminal or command prompt, navigate to the directory where the code is located, and run the following command:

python server.py

The Flask server will start running on http://localhost:5000 /  http://{your_IP}:5000

**Usage**

Upload an image: To classify an image, send a POST request to http://localhost:5000/upload with the image file in the request payload. 

You can use client.py to make the request. Make sure the key of the file in the request payload is image. 

Receive the response: The server will process the image, perform classification using the pre-trained model, and return a JSON response with the predicted class, the filename, and the processing time.

=====================================================================

