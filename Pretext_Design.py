import  numpy as np
from tqdm import tqdm

class Generation():
    def __init__(self,img_shape,batch_size,classes):
        self.img_shape=img_shape
        self.batch_size=batch_size
        self.num_class=classes
        
    #Random Masking
    def image_masking(self):

        masks=np.ones((self.batch_size,self.img_shape[0],self.img_shape[1],self.img_shape[2]))

        for i in range(self.batch_size):
            height=np.random.randint(5,30)
            width=np.random.randint(5,30)
            row=np.random.randint(0,self.img_shape[0]-height)
            col=np.random.randint(0,self.img_shape[1]-width)

            masks[i,row:row+height,col:col+width,:]=0

        return masks
    
    # Generate positive and negative pairs for training
    def generate_contrastive_pairs(self,images, labels, num_pairs=2000):
        num_classes = len(np.unique(labels))

        positive_pairs = []
        negative_pairs = []

        for _ in tqdm(range(num_pairs)):
            class_idx = np.random.randint(1, num_classes+1)
        
            # Positive pair (images with the same class)
            #class_images = images[labels.flatten() == class_idx]
            indices=np.where(labels.flatten() == class_idx)[0]
            if len(indices) < 2:
                continue  # Skip if there are not enough images for this class

            positive_pair = np.random.choice(indices, 2, replace=False)
            positive_pairs.append(positive_pair)

            # Negative pair (images with different classes)
            other_class_idx = np.random.choice(np.arange(1,num_classes+1)[np.arange(1,num_classes+1) != class_idx])
            #print(other_class_idx)
            other_class_indices=np.where(labels.flatten()==other_class_idx)[0]
            #print(other_class_images)
            negative_pair = [np.random.choice(indices),
                            np.random.choice(other_class_indices)]
            negative_pairs.append(negative_pair)

        return np.array(positive_pairs), np.array(negative_pairs)


    #Jigsaw Puzzle
    def image_tiles(self,img_array,num_tiles=9):
        permutation=np.random.permutation(num_tiles)
        pieces=[img_array[:,i*self.img_shape[0]:(i+1)*self.img_shape[0],:] for i in permutation]
        input_image=np.concatenate(pieces,axis=1)

        return input_image,permutation


#x_train=x_train*image_masking()

