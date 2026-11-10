import pandas as pd

df = pd.read_csv("u_food_marketing.csv")

df.head()
df.describe()


df["value"].min()
#getting max value
