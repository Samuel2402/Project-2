sudo apt install python3 python3-pip python3-venv curl -y

python3 -m venv venv

. venv/bin/activate

pip3 install -r requirements.txt

python3 app.py