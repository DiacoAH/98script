import pandas as pd 
class tsi():
    def __init__(self):
        self.dataFolder = "Data"
        self.filename = "dataFile"
        self.lastkandel = None
    def apply(self,interval, long, short, signal):
        df = pd.read_csv(f"{self.dataFolder}/{self.filename}{interval}")
        close = df['Close']
        
        diff = close - close.shift(1)
        abs_diff = abs(diff)
        
        diff_smoothed = diff.ewm(span = long, adjust = False).mean()
        diff_double_smoothed = diff_smoothed.ewm(span = short, adjust = False).mean()
        abs_diff_smoothed = abs_diff.ewm(span = long, adjust = False).mean()
        abs_diff_double_smoothed = abs_diff_smoothed.ewm(span = short, adjust = False).mean()
        
        tsi = (diff_double_smoothed / abs_diff_double_smoothed) * 100
        signal = tsi.ewm(span = signal, adjust = False).mean()
       
        df['tsi'] = round(tsi , 4)
        df['signal'] = round(signal , 4)
        df.dropna(inplace=True)
        df['sig'] = df.apply(lambda row : self.condition(row) , axis=1)
        df.dropna(inplace=True)

        return df
         
    def condition(self, row):
        if row['tsi'] > 0 and row['signal'] > 0 and row['tsi'] > row['signal'] :
            return 1 
        elif row['tsi'] < 0 and row['signal'] < 0 and row['tsi'] < row['signal']:
            return -1
        else:
            return 0
if __name__ == '__main__':
        
    a= tsi()
    mydata = a.apply(30, 25, 13, 13)

    breakpoint()