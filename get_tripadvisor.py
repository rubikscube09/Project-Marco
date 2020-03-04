import pandas as pd
import trip_advisor_consts
import hotels
clusters = trip_advisor_consts.CLUSTERS

def get_attr_dict(num_dests):
	destinations = pd.read_csv('preprocessing/scraping/destinations.csv')

	sample_dests = list(destinations['city'][0:num_dests])

	attractions_dict = {}
	name_desc_img = {}

	for city in sample_dests:
		data = hotels.get_attractions(city)
		name_desc_img[city] = data[0]
		attractions_dict[city] = data[1]
	return name_desc_img,attractions_dict




				

	