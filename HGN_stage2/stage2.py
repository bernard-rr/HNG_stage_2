from flask import *
from flask_cors import CORS

#configure the app
app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

@app.route('/')
def home():
    return "HNG STAGE 2 TASK"


@app.route('/api/calc', methods= ['POST'])
def calculate():
    operation_type = request.json['operation_type']
    x = request.json['x']
    y = request.json['y']
      
    result = 0
    if operation_type == "minus" or operation_type == "substract" or operation_type == "substraction":
        result = x - y
    if operation_type == "plus" or operation_type == "add" or operation_type == "addition":
        result = x + y
    if operation_type == "times" or operation_type == "multiply" or operation_type == "multiplication":
        result = x * y
    return jsonify({
            'slackUsername': "bernardchidi5",
            'operation_type': operation_type,
            'result': result
        })
    
if __name__ == '__main__':
    app.run(port=7776)