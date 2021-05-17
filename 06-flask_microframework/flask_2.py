# flask 2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/italian-fiscal-code")
def get_italian_fiscal_code():
  result = {"fiscalCode": "MNTRFL72E10F839I"}
  return jsonify(result)
