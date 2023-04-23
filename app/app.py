from flask import Flask, render_template, request
app = Flask(__name__)
from query import *
from datetime import datetime
from process_data import *
# Thanks to https://stackoverflow.com/questions/46482475/how-handle-a-button-click-on-python-flask
import schedule
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

# https://stackoverflow.com/questions/21214270/how-to-schedule-a-function-to-run-every-hour-on-flask

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
    
    def my_function():
        """This Function is just a test"""
        yen = process_data()
        print(yen)
        print("CHECK THIS OUT")
        with open('filename.txt','a') as file:
            file.write("yen")
            file.close()
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=my_function, trigger="interval", seconds=2)
    scheduler.start()
    # Exiting Condition
    atexit.register(lambda: scheduler.shutdown())