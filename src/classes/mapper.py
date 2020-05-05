import pandas as pd
from classes.config import data

class Map:
    def __init__(self,file_name, index):
        path = data["lookup"]
        self.index = index
        self.mappings = _load_mappings(path,file_name)

    def map_data(self,df,df_index):
          return pd.merge(df, self.mappings, left_on=df_index, right_on=self.index)

def _load_mappings(path,file_name):
    return pd.read_csv(path + file_name)
