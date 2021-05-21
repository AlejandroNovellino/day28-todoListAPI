from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [
    {
        "label": "My first task",
        "done": False
    }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos) 

@app.route('/todos', methods=['POST'])
def add_new_todo():
    #request_body = request.data
    #print("Incoming request with the following body", request_body)
    #return 'Response for the POST todo'

    data = request.data
    todos.append(json.loads(data))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    removed_todo = todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
