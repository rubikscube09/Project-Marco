import vacation_id3
import pandas as pd
import hotels

df=pd.read_csv('preprocessing/destinations_with_static_info.csv')

del df['Unnamed: 0']
df['safety']=df.apply(lambda row: int(row['safety'][6]),  axis=1)

def query(k,n, df=df):
    '''
    k: cities to filter on keywords
    n: cities to return
    '''
    num_adults=input("Number of travelers: ")
    check_in=input("Travel date: ")
    nights=input("Nights: ")
    
    cities=vacation_id3.traverse(k)

    safety_weight=int(input('How important is safety? '))
    lang_weight=int(input('How important is English navigability? '))
    

    df=df[df['city'].isin(cities)]
    df['comp_score']=df.apply(lambda row: float(row['safety'])*safety_weight+float(row['language'])*lang_weight,axis=1)
    df=df.sort_values('comp_score', ascending=False).iloc[:n]

    #DO FLIGHT DATA
    
    df['hotels']=df.apply(lambda row: hotels.get_hotels(row['trip_advisor_id'], num_adults, check_in, nights), axis=1)
    df['best_price']=df.apply(lambda row: row['hotels'][0][1], axis=1)
    
    return df[['city','country','best_price', 'hotels','text','image']].sort_values('best_price', ascending=False)

