
from flask import render_template
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
   return render_template('paint.html')
app.run(debug=True)