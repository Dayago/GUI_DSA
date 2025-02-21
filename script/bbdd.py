import pandas as pd

class ensamble_data:

    def __init__(self, path, df):
        self.path = path
        self.df = df 

    def fetch_data(self, path):
        data = pd.read_csv()
