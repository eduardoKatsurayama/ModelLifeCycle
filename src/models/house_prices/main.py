import pandas as pd
import sys

ROOTH_PATH = __file__[:__file__.index('src')]
sys.path.append(ROOTH_PATH)

from src.models.house_prices import train_model

df = pd.read_parquet(f'fake_cloud_storage/house_prices_train.parquet')
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

model_name = 'house_prices'
train_model.run(X, y, model_name, to_production=True)
