from flask import Flask

app = Flask(__name__)

@app.route('/script')
def script():
    return """
    echo "Hello from remote script"
    """
    
if __name__ == "__main__":
    app.run(debug=True)