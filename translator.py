import pandas as pd

data = pd.read_json('agencies.json')
data.to_csv('agencies.csv')