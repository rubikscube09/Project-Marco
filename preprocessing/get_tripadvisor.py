import pandas as pd
import trip_advisor_consts
import hotels
import get_trip_advisor_static
clusters = trip_advisor_consts.CLUSTERS


def get_attr_dict():
	'''
	getting the list of attraction informations from trip_advisor_consts

	Input: None

	Output:
	a list of image links and attractions dictionary.
	'''
	destinations = pd.read_csv('destinations_with_static_info.csv')
	print(destinations)
	sample_dests = list(zip(list(destinations['city']),list(destinations['trip_advisor_id'])))
	attractions_dict = {}
	name_desc_img = {}

	for city,t_id in sample_dests:
		data = get_trip_advisor_static.get_attractions(t_id)
		name_desc_img[city] = data[0]
		attractions_dict[city] = data[1]
	return [name_desc_img,attractions_dict]
