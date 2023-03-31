from flask import Flask, request, send_from_directory, abort, render_template, make_response
import requests
import os

app = Flask(__name__)

# 生データを取得するエンドポイント
@app.route('/raw-data/<path:filename>')
def raw_data(filename):
    if filename == "sheet.txt":
        url = "https://script.google.com/macros/s/AKfycbz6xvtbSFZ30LsjnSQPchgiRiTlMkouUr55P_ukmLECFICabPFOme8_chpA4EoeND1Zsw/exec?mode=view"
        response = requests.get(url)
        print(response.text)

        httpres = make_response(response.text, 200)
        httpres.mimetype = "text/plain"
        return httpres
    else:
        abort(404)

if __name__ == "__main__":
    app.run()
