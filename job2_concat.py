import pandas as pd
from Tools.scripts.objgraph import ignore

df = pd.read_csv('./crawling_data/reviews_2020_1page.csv')
df.info()

df = pd.DataFrame()
for i in range(1, 38):
    df_temp = pd.read_csv('./crawling_data/reviews_2017_{}page.csv'.format(i))
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    df = pd.concat([df, df_temp], ignore_index = True)
df.drop_duplicates(inplace=True)
df.info()
my_year = 2017
df.to_csv('./crawling_data/reviews_{}.csv'.format(my_year))