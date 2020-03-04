import pandas as pd

def calc_score(clusters, attractions_list):
    '''
    Given a list of clusters, calculate the frequency of the keywords in each
    city and output to a pandas dataframe.
    '''
    out = pd.DataFrame()
    rpt = False
    city_column = []
    for cluster in clusters:
        print(cluster)
        column = []
        count = 0
        for city in attractions_list:
            count = 0
            for i in range(0,len(attractions_list[city])):
                for attraction in attractions_list[city][i]:
                    if attraction in clusters[cluster]:
                        count += (30 - 0.5*i)/30
            column.append(count)
            if rpt == False:
                city_column.append(city)
        rpt = True
        out[cluster] = column
        # normalize
        # out[cluster] = out[cluster] / out[cluster].sum()
    print(city_column)
    out['city'] = city_column
    out.set_index(['city'])
    return out 
    # the ordering of the output dataframe should be the same as the order of 
    # the cities

        