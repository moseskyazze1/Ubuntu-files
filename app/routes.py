from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Moses",
        "last_name": "KY",
        "hobbies": "Soccer",
        "is_online": True
    }
    return me