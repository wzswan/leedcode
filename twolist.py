def dict_from_list(list1, list2):
    mountain_data=dict(zip(list1, list2))
    return mountain_data
def check(object):
    for i in mountain_data.keys():
        if mountain_data.has_key(name):
            print mountain_data.get(name)
            break
        else:
            print "NULL"
            break

if __name__ =='__main__':
    list1 = ['Fujisan','Kitadake','Tateyama','Ainodake','Yarigatake','Warusawadake'
            ,'Akaisidake','Karasawadake','Kitahodakadake','Oobamidake','Maehodakadake'
            ,'Nakadake','Arakawanakadake','Ontakesan','Noutoridake','Shiomidake',
            'Minamidake','Senjougatake','Norikuradake','Okuhodakadake']
    list2 =[3775,3193,3015,3190,3180,3141,3120,3110,3160,3101,3090,3084,3083,
            3067,3051,3046,3032,3032,3026,3190]
    print "please input the mountain name"
    name = raw_input()
    mountain_data = dict_from_list(list1,list2)
    check(name)
