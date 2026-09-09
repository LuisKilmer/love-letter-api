import pandas as pd

df = pd.read_csv(
    "dataset_preparado.csv",
    sep=";",
    encoding="utf-8"
)
df.to_parquet("dados.parquet")