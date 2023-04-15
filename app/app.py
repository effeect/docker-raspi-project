from flask import Flask, render_template, request
app = Flask(__name__)
from query import *

# Thanks to https://stackoverflow.com/questions/46482475/how-handle-a-button-click-on-python-flask

ButtonPressed = 0
        
@app.route('/', methods=["GET", "POST"])
def button( ButtonPressed = 0 ):
    if request.method == "POST":
        # Put Influx Requests here when ready 
        ButtonPressed += 1 # Note this increment here
        return render_template("index.html", ButtonPressed = ButtonPressed)
    return render_template("index.html", ButtonPressed = ButtonPressed)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)