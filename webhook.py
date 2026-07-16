from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["POST"])
def alert():
    subprocess.call(["bash", "scripts/alert.sh"])
    return "Recovered"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
