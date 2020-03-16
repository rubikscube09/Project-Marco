import pandas as pd
import sys
sys.path.insert(0,'/preprocessing')
import trip_advisor_consts

def calc_score(attractions_dict,clusters = trip_advisor_consts.CLUSTERS):
    '''
    Given a list of clusters, calculate the frequency of the keywords in each
    city and output to a pandas dataframe. Also add temperatures

    Input: list of cluster objects

   	Output:
	pandas dataframe
    '''
    out = pd.DataFrame()
    rpt = False
    city_column = []
    for cluster in clusters:
        column = []
        count = 0
        for city in attractions_dict:
            count = 0
            for i in range(0,len(attractions_dict[city])):
                for attraction in attractions_dict[city][i]:
                    if attraction in clusters[cluster]:
                        # Scoring system: Tripadvisor data is scored in order of ranking.
                        # Remove weight from a city if it is further down on the list.
                        count += (len(attractions_dict[city]) - 0.5*i)/len(attractions_dict[city])
            column.append(count)
            if rpt == False:
                city_column.append(city)
        rpt = True
        out[cluster] = column
        # normalize
    out['city'] = city_column
    out = out.set_index(['city'])
    return out 
    # the ordering of the output dataframe should be the same as the order of 
    # the cities

        