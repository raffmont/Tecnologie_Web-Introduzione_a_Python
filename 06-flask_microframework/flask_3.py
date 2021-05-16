# flask 3
from flask import Flask, jsonify, request
from codicefiscale import codicefiscale

app = Flask(__name__)

@app.route("/italian-fiscal-code", methods=["POST"])
def get_italian_fiscal_code():
  fiscal_code = codicefiscale.encode(
    surname=request.form["surname"],
    name=request.form["name"],
    sex=request.form["sex"],
    birthdate=request.form["birthdate"],
    birthplace=request.form["birthplace"])
  result={ "fiscalCode":fiscal_code }
  return jsonify(result)
