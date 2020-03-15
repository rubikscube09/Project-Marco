import current_location
import vacation_id3
import pandas as pd
import hotels
from datetime import datetime, timedelta


current_loc=current_location.get_location()
df=pd.read_csv('preprocessing/destinations_with_static_info.csv')

del df['Unnamed: 0']
df['safety']=df.apply(lambda row: int(row['safety'][6]),  axis=1)

def query(k,n, df=df):
    '''
    Inputs:
    k:int, cities to filter on keywords
    n:int, cities to return
    df: pandas dataframe
    '''
    num_adults=input("Number of travelers: ")
    departure_date=input("Departure date: ")
    return_date=input("Return date: ")
    nights=difference =(return_date - departure_date).days
    check_in=departure_date #NOT ALWAYS TRUE
    cities=vacation_id3.traverse(k)

    safety_weight=int(input('How important is safety? '))
    lang_weight=int(input('How important is English navigability? '))
    

    df=df[df['city'].isin(cities)]
    df['comp_score']=df.apply(lambda row: float(row['safety'])*safety_weight+float(row['language'])*lang_weight,axis=1)
    df=df.sort_values('comp_score', ascending=False).iloc[:n]

    #DO FLIGHT DATA
    
    df['hotels']=df.apply(lambda row: hotels.get_hotels(row['trip_advisor_id'], num_adults, check_in, nights), axis=1)
    df['flights']=ddf.apply(lambda row: kiwi.get_flights(current_loc, row['city'], 
                departure_date, return_date, 
                roundtrip = True,
                return_from=row['city'], return_to=current_loc, 
                adults=num_adults, children=0, infants=0,
                budget=5000, currency='USD',
                people=0, 
                max_duration=50, 
                radius=50, radius_format= 'km'), axis=1)
    
    df['best_price']=df.apply((lambda row: row['hotels'][0][1]+row['flights'][0]['price']), axis=1)
    
    return df[['city','country','best_price', 'hotels','flights','text','image']].sort_values('best_price', ascending=False)

