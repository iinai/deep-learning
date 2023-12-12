# Flask Image Classifier

## Overview

This Flask project is a simple web application that uses a pre-trained machine learning model to classify images as either a dog or a cat.

## Prerequisites

Make sure you have the following installed on your machine:

* Python 3.x
* Flask
* NumPy
* TensorFlow
* Keras
* Pillow (PIL)

## Getting Started

1. Clone the repository

    ```bash
    git clone https://gitlab.labranet.jamk.fi/AB7766/syvaoppiminen-tehtavat.git
    ```

2. Navigate to the project directory

    ```bash
    cd flask-app
    ```

3. Install the required Python packages described in Prerequisites.

## Running the Application

1. Make sure you are in the project directory.
2. Run the Flask application

    ```bash
    python app.py
    ```

    or

    ```bash
    flask run
    ```

3. Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. Once the application is running, you can navigate to the home page.
2. Upload an image using the provided form.
3. Click the "Predict" button to classify the uploaded image.
4. The result will be displayed, indicating whether the image is likely to be a dog or a cat.

## Model Information

The project uses a pre-trained machine learning model (model2.keras) for image classification. The model is loaded into memory when the Flask application starts.

## Project Structure

```bash
│   app.py /The main Flask application script.
│   model2.keras
│   README.md
│
├───static /Contains static files such as stylesheets.
│   │   styles.css
│   │
│   └───img /Contains all images used in the application.
│           favicon.ico
│           holographic.jpg
│           morri_ja_nakki_bgless.png
│
└───templates /Contains HTML templates for rendering web pages.
        index.html
```

## Notes

* This project assumes that the pre-trained model file (model2.keras) is in the same directory as app.py.
* The model expects images to be resized to 64x64 pixels.
