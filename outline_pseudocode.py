#FUNCTIONS TO FILL DATAFRAME
def get_destinations(starting_url,n):
    '''
    Crawl pages on lonely planet. Return a dataframe table with n vacation
    destinations, and the words assosciated with each vacation destination.
    '''
def get_keywords(destinations,j,k, df):
    '''
    Extract j non-common words that are best at binning the destinations into k
    bins above. Return a dataframe with only these key words.
    '''

def get_weather(df, travel_dates):
    '''
    Add weather info to dataframe.
    '''

def get_languages(df):
    '''
    Add language info to dataframe.
    '''

def get_safety(df):
    '''
    Add safety info to dataframe
    '''

def get_flight_costs(df, travel_dates, starting_dest):
    '''
    Get best flights to each dest, add to dataframe
    '''

def get_hotel_costs(df, travel_dates):
    '''
    Get best hotels in each dest, add to dataframe
    '''
#FUNCTIONS TO POPULATE TREE
class tree:
    '''
    Leaves are vacations. Nodes are answers to questions above.
    '''

def populate_tree(df):
    '''
    Returns: tree object
    '''

def query_tree:
    '''
    Query our tree and return relevant info.
    '''
    
