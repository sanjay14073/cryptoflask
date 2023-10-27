import math
import os

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json(force=True)
    message = data["message"]
    key = data["key"]
    cipherText = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    encrypted_text = "".join(cipherText)
    return jsonify({"ans": encrypted_text, "key": key})


@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json(force=True)
    message = data["message"]
    key = data["key"]
    numCols = math.ceil(len(message) / key)
    numRows = key
    numShadedBoxes = (numCols * numRows) - len(message)
    plainText = [""] * numCols
    col = 0
    row = 0

    for symbol in message:
        plainText[col] += symbol
        col += 1

        if (
            (col == numCols)
            or (col == numCols - 1)
            and (row >= numRows - numShadedBoxes)
        ):
            col = 0
            row += 1

    ans = "".join(plainText)
    return jsonify({"ans": ans})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3300))
    app.run(host='0.0.0.0', port=port)




