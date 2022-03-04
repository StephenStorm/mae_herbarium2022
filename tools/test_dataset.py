from util.Herbarium import Herbarium2022

anno_file = '/opt/tiger/workspace/datasets/train_metadata.json'
root = '/opt/tiger/workspace/datasets/train_images'

dataset = Herbarium2022(root, anno_file)

img, label = dataset[10000]
print(img.size)
print(label)