from flask import Flask, jsonify, request
from models import Task, InMemoryStore

app = Flask(__name__)
store = InMemoryStore()

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify([t.to_dict() for t in store.list()]), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    t = store.get(task_id)
    if not t:
        return jsonify({"error": "task not found"}), 404
    return jsonify(t.to_dict()), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json() or {}
    title = data.get('title')
    if not title or not isinstance(title, str) or title.strip() == '':
        return jsonify({"error": "title is required"}), 400
    description = data.get('description', '')
    t = store.create(title.strip(), description)
    return jsonify(t.to_dict()), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    t = store.get(task_id)
    if not t:
        return jsonify({"error": "task not found"}), 404
    data = request.get_json() or {}
    if 'title' in data:
        t.title = data['title'].strip()
    if 'description' in data:
        t.description = data['description']
    if 'status' in data:
        if data['status'] not in ['todo', 'in_progress', 'done']:
            return jsonify({"error": "invalid status"}), 400
        t.status = data['status']
    store.update(t)
    return jsonify(t.to_dict()), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if not store.delete(task_id):
        return jsonify({"error": "task not found"}), 404
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
