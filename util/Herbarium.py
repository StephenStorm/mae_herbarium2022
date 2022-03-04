import cv2
from torchvision.datasets import ImageFolder
# torchvision.datasets.ImageFolder

class Herbarium2022(ImageFolder):
    '''
        15501 classes 
    '''
    def __init__(self, root_dir, df, transforms=None):
        self.root_dir = root_dir
        self.df = df
        self.transforms = transforms
        
    def __len__(self):
        return len(self.df)
    
    def __getitem__(self, idx):
        filename = self.df.iloc[idx, 0]
        image_path = os.path.join(TRAIN_DIR, filename)
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        label = self.df.iloc[idx, 5]
        
        if self.transforms is not None:
            img = self.transforms(image=img)["image"]
            
        return img, label