import json


'''


{ 
    "annotations" : [annotation], 
    "categories" : [category], 
    "genera" : [genus] 
    "images" : [image], 
    "distances" : [distance], 
    "licenses" : [license], 
    "institutions" : [institution] 
}

annotation { 
    "image_id" : int, 
    "category_id" : int,
    "genus_id" : int, 
    "institution_id" : int
}

image {
    "image_id" : int, 
    "file_name" : str, 
    "license" : int 
}

category { 
    "category_id" : int, 
    "scientificName" : str, # We also provide a super-category for each species. 
    "authors" : str, # correspond to 'authors' field in the wcvp "family" : str, # correspond to 'family' field in the wcvp "genus" : str, # correspond to 'genus' field in the wcvp "species" : str, # correspond to 'species' field in the wcvp 
}

genera { 
    "genus_id" : int, 
    "genus" : str 
}

distance { 
    # We provide the pairwise evolutionary distance between categories (genus_id0 < genus_id1). 
    "genus_id_x" : int,
    "genus_id_y" : int,
    "distance" : float 
}
'''


anno_file = '/opt/tiger/workspace/datasets/train_metadata.json'

anno_f = open(anno_file, 'r')

anno = json.load(anno_f)

annotations = anno['annotations']
categories = anno['categories']

print('categories nums : {}'.format(len(categories))) # 15501


# get cat_id to name str
catid_name = dict()
for cat in categories :
    category_id = cat['category_id']
    scientificName = cat['scientificName']
    catid_name[category_id] = scientificName





clsid_imageids = dict()


# statistic samples num for each cls
for item in annotations:
    category_id = item['category_id']
    image_id = item['image_id']
    if category_id not in clsid_imageids :
        # clsid_imageids[category_id] = [image_id]
        clsid_imageids[category_id] = 1
    else :
        # clsid_imageids[category_id].append(image_id)
        clsid_imageids[category_id] += 1
sorted_dict = sorted(clsid_imageids.items(), key = lambda item : item[1], reverse=True) # list, tuple as element

# print(type(sorted_dict))
with open('/opt/tiger/workspace/mae/parse_res/dataset_statistic.txt', 'w') as wf:
    for item in sorted_dict:
        wf.write('{}\t{}\t{}\n'.format(catid_name[item[0]], item[0], item[1]))
    
        




    





