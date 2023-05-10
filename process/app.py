from query import *
from process_data import *
import time
import datetime

hour = 0

# Thanks to https://stackoverflow.com/questions/45626417/how-to-sleep-my-python-script-every-hour

query_test = query("CRb_UMmVsnfFY9GOtDpUABWDerHF7eVjzDEQ3PRnA3FLIjE481PfokAL-6tJ6_5cxq-mCsOE8zIuZqupBwjfAw==",
                   "dimes",
                   "http://influxdb:8086")




if __name__ == '__main__':
    # Will run forever
    while True :
        now_hour = datetime.datetime.now().hour

        if hour != now_hour:
            def my_function():
                """This Function is just a test"""
                yen = process_data()
                print(yen)
                print("CHECK THIS OUT")
                with open('filename.txt','a') as file:
                    file.write(f'{yen}')
                    file.close()
                
                point = ( Point("yentogbp").tag("tagname1", "tagvalue1").field("currency", yen))
                query_test.write_data("my-bucket", point )
        
            my_function()

        hour = now_hour

        time.sleep(60)