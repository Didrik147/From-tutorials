# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('avocado.csv')

#print(df.tail(2))

#print(df["AveragePrice"].head())

albany_df = df[df["region"] == "Albany"]

#print(albany_df.head())

#print(albany_df.index)

albany_df = albany_df.set_index("Date")
#albany_df.set_index("Date", inplace=True)

print(albany_df.head())

albany_df["AveragePrice"].plot()