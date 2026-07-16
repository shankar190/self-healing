from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["POST"])
def alert():

    result = subprocess.run(
        ["bash", "scripts/alert.sh"],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    return "Recovered"

app.run(host="0.0.0.0", port=5001)
