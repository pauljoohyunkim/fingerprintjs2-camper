from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=["POST"])
def handle():
    print(request.remote_addr)
    json_str = json.loads(request.data)
    json_formatted = json.dumps(json_str, indent=2)
    print(json_formatted)
    return "test"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)
