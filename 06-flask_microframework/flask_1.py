# flask 1
from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
  html='''
        <html>
          <head>
            <title>Python Flask Hello World</title>
          </head>
          <body>
            <h1>Hello Python Flask World!</h1>
          </body>
        </html>'''
  return html

