import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

class query:
    def __init__(self,token,org,url):
        """Intialise the Class for the Query settings to specific where it needs to go"""
        self.token = token
        self.org = org
        self.url = url
        self.write_client = influxdb_client.InfluxDBClient(url=self.url, token=self.token, org=self.org)
    
    def write_data(self,bucket,point):
        """Writing Data to InfluxDB Database"""
        self.bucket = bucket
        self.point = point

        #Settings up write request
        self.write_api = self.write_client.write_api(write_options=SYNCHRONOUS)
        self.write_api.write(bucket=bucket, org=self.org, record=self.point)


# token = os.environ.get("INFLUXDB_TOKEN")
# org = "dimes"
# url = "http://localhost:8086"
# write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

# bucket="my-bucket"

# write_api = client.write_api(write_options=SYNCHRONOUS)


if __name__ == '__main__':
    query_test = query("yourtokenhere","dimes","http://influxdb:8086")
    for value in range(5):
        point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", value)
        )
        query_test.write_data("my-bucket",point)
        time.sleep(1) # separate points by 1 second
