# 1. Import Flask
from flask import Flask, jsonify


# 2. Create an app
app = Flask(__name__)

# 2.1 Global Variable
hello_dict = [{"Hello": "World!"},{"Hello":"Portland!"}]

# 3. Define static routes
@app.route("/")
def index():
    return "Hello, world!"

/api/v1.0/precipitation
@app.route("/")
def index():
    return "Hello, world!"

/api/v1.0/stations
@app.route("/")
def index():
    return "Hello, world!"

/api/v1.0/tobs
@app.route("/")
def index():
    return "Hello, world!"

/api/v1.0/<start>
/api/v1.0/<start>/<end>
@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)    

# 4. define jsonified route
@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)


# 5. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
