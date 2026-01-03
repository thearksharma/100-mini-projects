from flask import Flask, request, jsonify
from service import sum_numbers

app = Flask(__name__)

@app.route("/sum")
def sum_api():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    result = sum_numbers(a, b)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
