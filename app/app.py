from flask import Flask, render_template, request
app = Flask(__name__)

# Influx DB
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "dimes"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/button', methods=['POST'])
def button():
    print("Hello world")
    return 'Button clicked!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)