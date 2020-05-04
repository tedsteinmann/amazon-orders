import pandas as pd
from classes.config import data

class Read:
  def __init__(self,file_name):
      path = data["raw"]
      self.df = _read_data(path,file_name)

# get data from csv
def _read_data(path,file_name):
    return pd.read_csv(path + file_name)