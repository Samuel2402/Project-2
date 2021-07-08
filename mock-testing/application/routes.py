from application import app
import requests

@app.route('/get/sport', methods=['GET'])
def sport():
    response = requests.get('http://api:5000/get/number')
    if response.text == "1":
        return "Football"
    elif response.text == "2":
        return "Badminton"
    elif response.text == "3":
        return "Hockey"
    else:
        return "Boxing"