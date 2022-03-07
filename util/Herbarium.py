from torchvision.datasets import VisionDataset
# torchvision.datasets.ImageFolder
import json
from PIL import Image


class Herbarium2022(VisionDataset):
    '''
        15501 classes 
    '''
    def __init__(self, root, anno_file, transform=None, target_transform = None):
        super(Herbarium2022, self).__init__(root, transform=transform, target_transform=target_transform)
        self.root_dir = root
        self.transform = transform
        # if target_transform is not None:
        self.target_transform = target_transform
        self.anno_file = anno_file

        # open anno file 
        print('loading dataset annotation file ...')
        anno_f = open(self.anno_file, 'r')

        anno = json.load(anno_f)
        annotations = anno['annotations']
        
        self.samples = []
        for item in annotations:
            category_id = item['category_id']
            image_id = item['image_id']
            # (image_id, cat_id)
            self.samples.append((image_id, category_id))
        
        #prepare cat_id to cat_name
        categories = anno['categories']
        self.class_to_idx = dict()
        for cat in categories:
            category_id = cat['category_id']
            scientificName = cat['scientificName']
            self.class_to_idx[scientificName] = category_id
        
        anno_f.close()
        print('load datasets done !!!, dataset len: {}, class nums : {}'.format(self.__len__(), len(self.class_to_idx)))
    
                
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        image_id, label = self.samples[idx]
        # image_id : 00147__049
        sub_folder1 = image_id[:3]
        sub_folder2 = image_id[3:5]

        image_path = self.root_dir + '/' + sub_folder1 + '/' + sub_folder2 + '/'+ image_id + '.jpg'
        img = self.pil_loader(image_path)
        
        if self.transform is not None:
            img = self.transform(image=img)["image"]
        if self.target_transform is not None :
            label = self.target_transform(label)
            
        return img, label

    def pil_loader(self, path: str) -> Image.Image:
        # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')