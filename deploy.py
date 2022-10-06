import keras
from PIL import Image
import numpy as np
from skimage import transform
class Myclass:
    def load(filename):
        prediction=""
        np_image = Image.open(filename)
        np_image = np.array(np_image).astype('float32')/255
        np_image = transform.resize(np_image, (224, 224, 3))
        np_image = np.expand_dims(np_image, axis=0)
        model=keras.models.load_model('E:\kivywork\model3.h5')
        pred=model.predict(np_image)
        arr=pred.tolist()
        if (arr[0][0] < .5):
            prediction = "covid positive"
        else:
            prediction="covid negative"
        return prediction