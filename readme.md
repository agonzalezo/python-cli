# Python CLI
Python CLI is a Python command-line utility built using the Click and qrcode library for educational purposes.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/agonzalezo/python-cli.git
   cd python-cli
1. Create a virtual env   
   ```bash
    python -m venv venv
1. Install dependences
    ```bash
    pip install -r requirements.txt
## Usage
- To generate an ascii QR
    ```bash
    # return an ascii QR pointing to netsys url
    python src/cli.py genqr --data "https://netsys.uno/"
    
    # Generate a qr.png QR file pointing to netsys url
    python src/cli.py genqr --qrtype image --data "https://netsys.uno/"
- To list users
    ```bash
    python src/cli.py list # return all users in the json file
    python src/cli.py user 1 # return user with id 1
- To Create users
    ```bash
    python src/cli.py new --name pepito --lastname perez
- To Delete user
    ```bash
    python src/cli.py rm 1 # To delete user with id 1
- To Update user
    ```bash
    python src/cli.py update 1 --name new-name --lastname new-lastname # To set new data to userid 1