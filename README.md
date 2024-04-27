##CS4296 Project
This project can provide a server using AWS so that the client can obtain the results of the model.
#Flask Client
This is Python client code that sends a POST request to a Flask server running on a specified IP address. 
The client code uploads an image file to the server for further processing. It uses the requests library to handle the HTTP requests.

Prerequisites
Python 3.10
requests library
Setup
Clone or download the repository to your local machine.

Install the required dependencies by running the following command:

pip install requests
Usage
Run the Flask server: Before running the client code, make sure the Flask server is up and running on the specified IP address. The server should be configured to handle the /upload endpoint.

Open the client.py file in a text editor.
Modify the server_ip variable: Enter the IP address of the Flask server in the server_ip variable. This should be the IP address where the server is running.
Provide the image file: Place the image file you want to upload in the same directory as the client.py file. Update the image_path variable with the filename of your image file.
Run the client code: Open a terminal or command prompt, navigate to the directory where the client.py file is located, and run the following command:
python client.py
The client code will send a POST request to the Flask server with the image file. It will receive the server's response and print the classification results if the request is successful.
Note: If the server is not running or the specified IP address is incorrect, an error message will be displayed.
