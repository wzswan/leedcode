print "please input the mountain name"
name = raw_input()

mountain_data = {'Fujisan':3775,'Kitadake':3193,'Tateyama':3015,'Ainodake':3190,
                 'Yarigatake':3180,'Warusawadake':3141,'Akaisidake':3120,'Karasawadake':3110,
                 'Kitahodakadake':3160,'Oobamidake':3101,'Maehodakadake':3090,'Nakadake':3084,
                 'Arakawanakadake':3083,'Ontakesan':3067,'Noutoridake':3051,'Shiomidake':3046,
                 'Minamidake':3032,'Senjougatake':3032,'Norikuradake':3026,'Okuhodakadake':3190}

for i in mountain_data.keys():
    if mountain_data.has_key(name):
        print mountain_data.get(name)
        break
    else:
        print "NULL"
        break
