import pandas as pd
from classes.config import data

class Write:
    def __init__(self,df,file_name):
        self.path = data["processed"]
        self._write_data(df,file_name)

    # write data to csv
    def _write_data(self,df,file_name):
        df.to_csv(self.path + file_name + '.csv', sep='\t')
