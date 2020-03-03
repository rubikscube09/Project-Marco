import pandas as pd


def calc_score(clusters, cities):
    '''
    Given a list of clusters, calculate the frequency of the keywords in each
    city and output to a pandas dataframe.
    '''

    out = pd.DataFrame()
    for cluster in clusters:
        column = []
        count = 0
        for city in cities:
            # unpack the list of lists into a flat list
            flat_list = [item for sublist in city for item in sublist]
            for item in flat_list:
                if item in cluster:
                    count += 1
            column.append(count)
        out[cluster] = column
        # normalize
        out[cluster] = out[cluster] / out[cluster].sum()
    # the ordering of the output dataframe should be the same as the order of 
    # the cities

        