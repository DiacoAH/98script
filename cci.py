import pandas as pd 
class cci():
    def __init__(self):
        self.dataFolder = "Data"
        self.filename = "dataFile"
        self.lastkandel = None
    
    def apply(self , interval , ndays):
        df = pd.read_csv(f"{self.dataFolder}/{self.filename}{interval}")
        df['TP'] = (df['High'] + df['Low'] + df['Close']) / 3 
        df['sma'] = df['TP'].rolling(ndays).mean()
        df['mad'] = df['TP'].rolling(ndays).apply(lambda x: pd.Series(x).mad())
        df['CCI'] = (df['TP'] - df['sma']) / (0.015 * df['mad'])
        df['CCI'] = round(df['CCI'] , 2)
        df['sig'] = df.apply(lambda row : self.condition(row) , axis=1)
        df.dropna(inplace=True)        
        return df
    
    def condition(self, row):
        
        if row['CCI'] > 100 :
            return 1 
        
        elif row['CCI'] < -100 :
            return -1
        
        else:
            return 0
        
if __name__ == '__main__':
    
    a = cci()
    a = a.apply(30, 40)
    breakpoint()