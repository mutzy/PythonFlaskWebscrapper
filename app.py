from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)
app.env = "development"

@app.route('/')
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug=True, )