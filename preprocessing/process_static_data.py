import pandas as pd
import process_city_keywords
import country
import language
import safety

#df=process_city_keywords.df
df=pd.read_csv("/scraping/destinations.csv")

df['country']=df.apply(lambda row: country.get_country(row['city']),axis=1)
df['language']=df.apply(lambda row: language.get_language(row['country']),axis=1)
df['safety']=df.apply(lambda row: safety.get_safety(row['country']), axis=1)



