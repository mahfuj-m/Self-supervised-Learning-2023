import os
import numpy as np
from tqdm import tqdm
from PIL import Image
from sklearn.model_selection import train_test_split


class Dataset():
    def __init__(self):
        pass

    @classmethod
    def generate_train_test(self,dataset):
        img,label=list(),list()
        for val in dataset:
            img.append(val[0])
            label.append(val[1])
        x_train,y_train=(np.array(img),np.array(label).reshape(-1, 1))
        x_train,x_test,y_train,y_test=train_test_split(x_train,y_train,test_size=.2 ,stratify=y_train)

        return (x_train,y_train),(x_test,y_test)
    @staticmethod
    def get_dataset(PATH, shape=(32,32)):
        dataset={'value':[],'label':[]}
        for subpath in os.listdir(PATH):
            if not subpath.startswith('.DS_Store'):     
                for filename in tqdm(os.listdir(os.path.join(PATH,subpath))):
                    if filename.endswith(".jpg") or filename.endswith(".png"):  
                        image_path=os.path.join(PATH,subpath,filename)
                        image = Image.open(image_path)
                        image = image.convert("RGB")
                        image = image.resize(shape)
                        image_array = np.array(image)
                        #image_list.append((image_array,int(subpath)))
                        dataset.setdefault('value',[]).append(image_array)
                        dataset.setdefault('label',[]).append(int(subpath))
        dataset=list(zip(dataset['value'],dataset['label']))
        return Dataset.generate_train_test(dataset)


#Dataset.get_dataset('Test_Data/Brain_Tumor')