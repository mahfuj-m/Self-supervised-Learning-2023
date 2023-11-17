## Self-supervised-Learning-2023
### Goal
This project is focused on identifying brain tumors using a self-supervised method. Instead of training the model in a traditional way, I utilized two different methods known as encoder and contrastive models. These models have distinct ways of learning the underlying features from an image. The primary goal is to develop the pretext functions and the models to pretrain using the available training samples. Following the pretraining phase, additional layers are added to fine-tune the models for the precise classification of brain tumors.

### Dataset
Dataset is available on this webpage: https://figshare.com/articles/dataset/brain_tumor_dataset/1512427/5
There is a less amount of data available from the source. So, the samples were distributed as follows:
Number of training samples: 2451

Number of finetuning samples: 12

Number of testing samples: 490
### Encoder model
This model works like an unsupervised model. Where the training sample were masked using random mask size. In the training, masked image and the original image passed to the network to learn the missing part of an image. Here is an example of an image and the same image after masking.
![mmasked](media/masked.png)
