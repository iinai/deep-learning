from flask import Flask, render_template, request, send_file
import numpy as np
import tensorflow
import keras
from keras.preprocessing import image
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

# Load the machine learning model
model = keras.models.load_model('model2.keras')

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/predict', methods=["GET", "POST"])
def displayImage():
    image_file = request.files['image']

    # Open the image using PIL
    img = Image.open(image_file)

    # Resize the image to 64x64 pixels
    img = img.resize((64, 64))

    # Convert the PIL image to a numpy array
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images/255.0, batch_size=8, verbose=0)
    print(classes)

    # Save the PIL image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    img_data_url = f"data:image/png;base64,{base64.b64encode(img_io.read()).decode()}"

    if classes[0] > 0.5:
        return render_template('index.html', prediction='This is likely to be a DOG', image_data=img_data_url)
    else:
        return render_template('index.html', prediction='This is likely to be a CAT', image_data=img_data_url)

if __name__ == '__main__':
    app.run(debug=True)
