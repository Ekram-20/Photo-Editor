from flask import Flask, render_template, request, url_for, session
import cv2
import numpy as np
import os
from edit_operations import *

current_image_name = None

app = Flask(__name__)

@app.route('/')
def home():
    image_path =  url_for('static', filename=f'upload-icon.jpeg')
    return render_template('index.html', image_path=image_path)


@app.route('/', methods=['POST'])
def process_image():

    # Retrieve the uploaded image file
    image_file = request.files['image']
    filepath = os.path.join(app.root_path, 'static/', image_file.filename)
    image_file.save(filepath)
    image_array = cv2.imread(filepath, 1)

    

    
    # Apply the selected image processing operation
    operation = request.form.get('operation')
    update_img = editImage(operation, image_array)
    
    # Save the processed image to a temporary file
    new_file_name = operation  + "_" + image_file.filename
    cv2.imwrite(os.path.join(app.root_path, 'static/', new_file_name), update_img)
    
    # Display the processed image on the result page
    image_path = url_for('static', filename= new_file_name)
    return render_template('index.html', image_path=image_path)


# return updated image
def editImage(operation, image_array):
    if operation == 'gray':
        return gray(image_array)

    if operation == 'blur':
        return blur(image_array)

    if operation == 'rescale':
        return resize(image_array)

    if operation == 'border':
        return addBorder(image_array)

    if operation == 'flip':
        return flip(image_array)
    
    return image_array




if __name__ == '__main__':
    app.run(debug=True, port=6060)
