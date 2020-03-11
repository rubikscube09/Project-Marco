BOAT_TOURS = 'Kayaking & canoeing,Stand-Up Paddleboarding,Waterskiing & jetskiing,Swim with dolphins,Surfing,\
Windsurfing & Kitesurfing,Submarine tours,Shark diving,Scuba & snorkelling,River rafting & tubing,\
Parasailing & paragliding,Water sports,Speed boats tours,Duck tours,Boat Tours,Boat rentals,\
Dolphin & whale watching,Fishing charters & tours,Gondola cruises'.split(',')



CASINOS = ['Casinos']

CONCERTS_SHOWS = 'Jazz Bars,Performances,Dinner Theaters,Concerts,Operas,Symphonies,Ballets,Theaters,Cabaret,Cirque du Soleil,Luaus,Sporting events & packages,Theater & musicals,Blues Bars,Piano Bar,Country Western Bars,Comedy Club'.split(',')

FOOD_DRINK = 'Farmers markets,Distillery Tours,Wineries,Breweries,Distilleries,Beer tastings & tours,Coffee & tea tours,Cooking classes,Food tours,Wine tastings & tours,Wine Bar,Other food and wine'.split(',')

MUSEUMS = 'Observatories/ Planetariums,Military Museums,Museums,Natural History Museums,Children\'s Museums,Science Museums,Specialty Museums,Art Galleries,Art Museums,History Museums'.split(',')


SEA_NATURE = ['Beaches', 'Bodies of Water', 'Reefs','Islands','Marinas','Swim with dolphins',\
'Duck tours','Bodies of Water','Caves','Dams','Waterfalls','Caverns/ Caves','Dams'] 


SEA_OUTDOOR = 'River rafting & tubing,Boat rentals,Dolphin & whale watching,\
Gondola cruises,Speed boats tours,Kayaking & canoeing,Stand-Up Paddleboarding,Shark diving,\
Scuba & snorkelling, Waterskiing & jetskiing,Swim with dolphins,Surfing,Windsurfing & Kitesurfing'.split(',') + BOAT_TOURS + SEA_NATURE

NATURE_PARKS = 'National Parks,Biking Trails,Equestrian Trails,Hiking Trails,\
Beaches,Zoos,Bodies of Water,Canyons,Caverns/ Caves,Dams,Deserts,\
Forests,Gardens,Geologic Formations,Hot Springs/ Geysers,Islands,Marinas,Mountains,\
Nature/ Wildlife Areas,Parks,Reefs,State Parks,Valleys,Volcanos,Waterfalls,Other nature and parks,Nature & wildlife tours'.split(',') + SEA_NATURE

    
GROUND_NATURE = list(set(NATURE_PARKS) - set(SEA_NATURE))

OUTDOOR_ACTIVITIES = 'Cross-country Ski Areas,Ski/ Snowboard Areas,Ski & snow tours,Sports Camps/ Clinics,Horseback Riding Stables,Golf Courses,\
Motorcycle Trails,Hiking Trails,Zoos,Surf Camps,Submarine tours,Parasailing & paragliding,\
Shark diving,Scuba & snorkelling,Equestrian Trails,Off road/All Terrain Vehicle Trails,\
Biking Trails,Trails,Beaches,Scenic Drives,Horse-Drawn Carriage Tours,Jogging Paths/ Tracks,\
Resort Communities,Other outdoor activities,Zipline tours,Stand-Up Paddleboarding,\
Safaris,Running tours,Canyoning & Rappelling Tours,Air tours,\
Boat Tours,Hiking & camping tours,Golf tours & tee times,\
Fishing charters & tours,Eco tours,Climbing tours,Bike tours,Balloon rides,\
Adrenaline & extreme tours,4WD,ATV & off-road tours,Duck tours,\
Waterskiing & jetskiing,Swim with dolphins,Surfing,Windsurfing & Kitesurfing,\
Gear rentals,Water sports'.split(',')

COLD_OUTDOOR = ['Cross-country Ski Areas', 'Ski/ Snowboard Areas','Ski & snow tours','Mountains']

LAND_OUTDOOR = list(set(list(set(OUTDOOR_ACTIVITIES) - set(SEA_OUTDOOR)) + NATURE_PARKS) - set(SEA_NATURE)) 

SHOPPING = 'Malls,Shops,Specialty Shops,Art Galleries,Airport Shops,Shopping tours,Fashion shows & tours,Farmers markets,Department Stores,Factory Outlets,Antique Shops,Flea/ Street Markets'.split(',')


TOURS = 'Gondola cruises,Skydiving,Day Trips,Boat rentals,Dolphin & whale watching,Speed boats tours,Kayaking & canoeing,Parasailing & paragliding, River rafting & tubing,Scuba & snorkelling,Shark diving,Submarine tours,Scenic Railroads,Tours,Factory Tours,Walking tours,Bus tours,Segway Tours,Water sports,Surfing,Windsurfing & Kitesurfing,Swim with dolphins,Waterskiing & jetskiing,Duck tours,Beer tastings & tours,Coffee & tea tours,Food tours,Wine tastings & tours,4WD,ATV & off-road tours,Adrenaline & extreme tours,Balloon rides,Bike tours,Climbing tours,Eco tours,Fishing charters & tours,Golf tours & tee times,Hiking & camping tours,Nature & wildlife tours,Running tours,Air tours,Archaeology tours,City tours,Cultural tours,Ghost & vampire tours,Helicopter tours,Historical & heritage tours,Hop-on Hop-off tours,Literary,art & music tours,Motorcycle tours,Movie & TV tours,Night tours,Ports of Call tours,Private tours,Rail tours,Self-guided tours & rentals,Skip-the-Line tours,Vespa,scooter & moped tours,Bar,club & pub tours,Fashion shows & tours,Shopping tours,Horse-Drawn Carriage Tours,Photography Tours,Stand-Up Paddleboarding,Canyoning & Rappelling Tours,Distillery Tours,Boat Tours,Zipline tours'.split(',')

AMUSEMENT_PARKS = 'Amusement/ Theme Parks,Disney,Water Parks'.split(',')

ZOOS = 'Zoos,Aquariums,Other zoos & aquariums'.split(',')

SIGHTS_AND_LANDMARKS = 'Neighborhoods,Universities,Educational Sites,Government Buildings,\
Reservations, Historic Walking Areas,Mines,Civic Centers,Ghost Towns,Military Bases/ Facilities,\
Battlefields,Missions,Farms,Landmarks/ Points of Interest,Architectural Buildings,\
Monuments/ Statues,Bridges,Scenic Drives,Observation Decks/ Towers,Lookouts,\
Lighthouses,Ships,Wharfs/ Piers/ Boardwalks,Fountains, Mysterious Sites,Arenas/ Stadiums/ Fields\
,Race Car Tracks'.split(',') + ['Religious Sites','Historic Sites', 'Ancient Ruins', 'Castles', 'Cemeteries', 'Churches/ Cathedrals', 'Historic Walking Areas' ]



HISTORIC = ['Religious Sites','Historic Sites', 'Ancient Ruins', 'Castles', 'Cemeteries', 'Churches/ Cathedrals', 'Historic Walking Areas' ]

CLUSTERS = {'SEA_OUTDOOR':SEA_OUTDOOR,
            'LAND_OUTDOOR':LAND_OUTDOOR,
            'CASINOS':CASINOS,
            'CONCERTS_SHOWS':CONCERTS_SHOWS,
            'FOOD_DRINK':FOOD_DRINK,
            'GROUND_NATURE':GROUND_NATURE,
            'COLD_OUTDOOR':COLD_OUTDOOR,
            'MUSEUMS':MUSEUMS,
            'NATURE_PARKS':NATURE_PARKS,
            'OUTDOOR_ACTIVITIES':OUTDOOR_ACTIVITIES, 
            'SHOPPING':SHOPPING,
            'HISTORIC':HISTORIC,
            'TOURS':TOURS,
            'AMUSEMENT_PARKS':AMUSEMENT_PARKS,
            'ZOOS':ZOOS,
            'SEA_NATURE':SEA_NATURE,
            'SIGHTS_AND_LANDMARKS':SIGHTS_AND_LANDMARKS}



