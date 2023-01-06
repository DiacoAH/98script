import ssl_channel , Data
from datetime import datetime , timedelta
import bot as bt
import tsi
import cci
import time
from time import sleep

dataFolder = "Data"
filename = "dataFile"
interval = 30
filepath = f"{dataFolder}/{filename}{interval}"

data = Data.Collector()
data.getNewData(interval)
ssl1 = ssl_channel.Ssl()
ssl2 = ssl_channel.Ssl()
tsi = tsi.tsi()
cci = cci.cci()

with open(filepath, 'r') as file:
            
     lts = int(file.readlines()[-1].split(',')[0])
     
next_ts = datetime.timestamp(datetime.fromtimestamp(lts) + timedelta(minutes=interval*2 , seconds=3))

bt.run()

while True :
    if time.time() >= next_ts :

        print(f"{datetime.now()}: new {interval} min kandel ({time.time()}) {next_ts}")
        # bt.send(f"{datetime.now()}: new {interval} min kandel ({time.time()}) {next_ts}")
        
        data.getNewData(interval)
        df = ssl1.apply(interval, 50,50)
        df2 = ssl2.apply(interval, 100,100)
        df3 = tsi.apply(interval, 25, 13, 13)
        df4 = cci.apply(interval, 40)
        lts = int(df['time'][df.index[-1]])
        next_ts = datetime.timestamp(datetime.fromtimestamp(lts) + timedelta(minutes=interval*2 , seconds=10))
        print(f'next_ts {next_ts}')
        if df['sig'][df.index[-1]] != df['sig'][df.index[-2]]:
            
            bt.send(f"🔵Ssl 50🔵")
            if (df['sig'][df.index[-1]] == df4['sig'][df.index[-1]]) :
                
                bt.send(f"🔵Ssl 50🔵  cci ✅")

            print(f"ssl 50 50 \n {interval} min kandel")
            
        if df2['sig'][df2.index[-1]] != df2['sig'][df2.index[-2]]:
            
            bt.send(f"🟡Ssl 100🟡")
            if (df['sig'][df.index[-1]] == df3['sig'][df.index[-1]]) :
                
                bt.send(f"🟡Ssl 100🟡 \n Tsi ✅")
                
            print(f"ssl 100 100 \n {interval} min kandel")
    else:
        # bt.send('waiting')
        print("waiting")
        sleep(60)

        