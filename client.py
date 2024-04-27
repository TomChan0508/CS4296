import requests

server_ip = input('Input server IP:')

server_url = f'http://{server_ip}:5000/upload'

image_path = 'image.jpg' 

files = {'image': ('image.jpg',open(image_path, 'rb'),'image/jpg',{})}
response = requests.post(server_url, files=files, timeout=10)

if response.status_code == 200:
    # Print the response content (classification results)
    print(response.json())

else:
    # Handle the error
    print('Error:', response.text) 