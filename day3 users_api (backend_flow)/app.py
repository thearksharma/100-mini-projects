from flask import Flask, request, jsonify
from service import create_user, get_users


app = Flask(__name__)


@app.route("/users", methods=["POST"])
def add_user_route():
print("Controller hit, write")
data = request.get_json()
name = data.get("name")
if not name:
return jsonify({"error": "Name is required"}), 400
user = create_user(name)
return jsonify({"user": user}), 201


@app.route("/users", methods=["GET"])
def list_users_route():
print("Controller hit, read")
name = request.args.get("name")
users = get_users(name)
return jsonify({"users": users})


if __name__ == "__main__":
app.run(debug=False)