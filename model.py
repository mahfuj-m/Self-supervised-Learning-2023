import tensorflow as tf
from tensorflow.keras import layers, models


class Model():
    def __init__(self,input_shape,num_class,epochs,batch_size):
        self.input_shape=input_shape
        self.num_class=num_class
        self.epochs=epochs
        self.batch_size=batch_size
    # Define the model architecture
    def contrastive_model(self):
        base_model = models.Sequential()
        base_model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=self.input_shape))
        base_model.add(layers.MaxPooling2D((2, 2)))
        base_model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        base_model.add(layers.MaxPooling2D((2, 2)))
        base_model.add(layers.Flatten())
        base_model.add(layers.Dense(256, activation='relu'))

        input_a = layers.Input(shape=self.input_shape)
        input_b = layers.Input(shape=self.input_shape)

        output_a = base_model(input_a)
        output_b = base_model(input_b)

        # Contrastive loss layer
        distance = layers.Lambda(lambda x: tf.reduce_sum(tf.square(x[0] - x[1]), axis=1, keepdims=True),
                                output_shape=lambda x: (x[0][0], 1))([output_a, output_b])

        contrastive_model = models.Model(inputs=[input_a, input_b], outputs=distance)
        contrastive_model.compile(optimizer='adam', loss='mse',metrics=['accuracy'])
        return contrastive_model    


    def self_supervised_model(self):
        model=models.Sequential()
        model.add(layers.Conv2D(32,(3,3),activation='relu',padding='same',input_shape=self.input_shape))
        model.add(layers.Conv2D(32,(3,3),activation='relu',padding='same'))
        model.add(layers.MaxPooling2D((2,2)))

        model.add(layers.Conv2D(64,(3,3),activation='relu',padding='same'))
        model.add(layers.Conv2D(64,(3,3),activation='relu',padding='same'))
        model.add(layers.MaxPooling2D((2,2)))

        model.add(layers.Conv2D(128,(3,3),activation='relu',padding='same'))
        model.add(layers.Conv2D(128,(3,3),activation='relu',padding='same'))
        model.add(layers.MaxPooling2D((2,2)))

        model.add(layers.Conv2D(128,(3,3),activation='relu',padding='same'))
        model.add(layers.Conv2D(128,(3,3),activation='relu',padding='same'))
        model.add(layers.UpSampling2D((2,2)))


        model.add(layers.Conv2D(64,(3,3),activation='relu',padding='same'))
        model.add(layers.Conv2D(64,(3,3),activation='relu',padding='same'))
        model.add(layers.UpSampling2D((2, 2)))

        model.add(layers.Conv2D(32,(3,3),activation='relu',padding='same'))
        model.add(layers.UpSampling2D((2, 2)))

        model.add(layers.Conv2D(3,(3,3),activation='sigmoid',padding='same'))

        model.compile(optimizer=tf.keras.optimizers.Adam(),
                loss=tf.keras.losses.MeanSquaredError(),metrics=['accuracy'])

        return model

    def classification_model(self,input_dimension=None):
        if input_dimension==None:
            input_dimension=self.input_shape
        model=models.Sequential()
        model.add(layers.Conv2D(32,(3,3),activation='relu',padding='same',input_shape=input_dimension))
        model.add(layers.Conv2D(64,(3,3),activation='relu',padding='same'))
        model.add(layers.Flatten())
        model.add(layers.Dense(64,activation='relu'))
        model.add(layers.Dense(self.num_class,activation='softmax'))

        model.compile(optimizer=tf.keras.optimizers.Adam(),
                loss=tf.keras.losses.MeanSquaredError(),
                metrics=['accuracy'])


        return model


# mm=Model((256,256,3),3,10,32)
# xxl=mm.self_supervised_model()
# xxl.summary()

                    


