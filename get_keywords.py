import textrazor

def get_keywords(text):
    textrazor.api_key = "1b69ecec7f8c72d386c2c5280780e6eb6ec00510e2a221d98e246c82"
    client = textrazor.TextRazor(extractors=["entities", "topics"])

    response = client.analyze(text)
    entities = list(response.entities())
    entities.sort(key=lambda x: x.relevance_score, reverse=True)
    seen = set()
    result = {}
    for entity in entities:
        if entity.id not in seen:
            seen.add(entity.id)
            list_of_cats = []
            set_of_cats = set()
            for i in list(entity.freebase_types):
                
                i.split("/")
                if i[0] != "/":
                    i = i[0]
                else:
                    i = i.split("/")[1]
                if i in ['travel','projects','location','arts', 'food', 'sports', 'media_common', 'exhibition', 'architecture', 'geography', 'visual_art', 'travel', 'protected_sites','sports']:
                    list_of_cats.append(i)
            if list_of_cats != []:        
                result[entity.id] = list_of_cats
    return result