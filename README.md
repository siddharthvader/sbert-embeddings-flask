# SBERT Flask Application

This repository contains a Flask application that provides an API to compute sentence embeddings using Sentence-BERT.

## Running the Application on an EC2 Instance

Follow these steps to run the application on an AWS EC2 instance.

### Prerequisites

- An AWS account.
- An EC2 instance running Ubuntu (You can follow this [guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-basic-instance.html) to set up an EC2 instance).
- Ensure that port 5000 is open in the security group associated with your EC2 instance to receive incoming traffic.

### Steps

1. SSH into your EC2 instance.

    ```
    ssh -i path-to-your-private-key.pem ubuntu@your-ec2-public-ip
    ```

2. Update the package manager.

    ```
    sudo apt update
    ```

3. Install Docker on your EC2 instance. Follow the [official documentation](https://docs.docker.com/engine/install/ubuntu/) for detailed instructions.

4. Clone this GitHub repository onto your EC2 instance.

    ```sh
    git clone https://github.com/siddharthvader/sbert-embeddings-flask.git
    cd sbert-embeddings-flask/
    ```

5. Build the Docker image.

    ```sh
    docker build -t sbert-flask -f docker/Dockerfile .
    ```

6. Run the Docker container. Make sure to open the relevant port in the EC2 security group.

    ```sh
    docker run -p 5000:5000 -e MODEL_NAME='all-MiniLM-L6-v2' sbert-flask
    ```

7. Your Flask application should now be running at `http://your-ec2-public-ip:5000`.

## Using the API with Python's requests library

You can use Python's `requests` library to send text to the Flask application and receive the sentence embeddings in response.

Here is an example code:

```python
import requests

url = 'http://your-ec2-public-ip:5000/embed'
headers = {'Content-Type': 'application/json'}
data = {'sentences': ['This is an example.', 'Computing embeddings using Flask.']}

response = requests.post(url, json=data, headers=headers)

print(response.json())
```

This script sends a POST request to the Flask app with sentences and prints out the embeddings received in the response.

Make sure to have the requests library installed (pip install requests) and replace your-ec2-public-ip with the public IP address of your EC2 instance.
