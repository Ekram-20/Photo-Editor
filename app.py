from flask import Flask, render_template, request
import cv2
import numpy as np
import os
from edit_operations import *


origin_img_name = 'before.jpg'
update_img_name = 'after.jpg'


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_image():
    
    # Retrieve the uploaded image file
    image_file = request.files['image']
    
    filepath = os.path.join(app.root_path, 'static/', origin_img_name)
    
    image_file.save(filepath)

    image_array = cv2.imread(filepath, 1)
    
    
    # # Read the image file using OpenCV
    # # img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
   


    # Apply the selected image processing operation
    operation = request.form.get('operation')
    
    
    if operation == 'gray':
        update_img = gray(image_array)

    elif operation == 'blur':
        update_img = blur(image_array)

    elif operation == 'rescale':
        update_img = resize(image_array)

    elif operation == 'border':
        update_img = addBorder(image_array)

    elif operation == 'flip':
        update_img = flip(image_array)
    
    else:
        update_img = image_array
    
    # Save the processed image to a temporary file
    cv2.imwrite(os.path.join(app.root_path, 'static/', update_img_name), update_img)
    
    # # Display the processed image on the result page
    # return render_template('index.html', image_path="static/aftere.jpg")
    # return render_template('index.html', filename="update_img_name")

    return render_template('index.html', filename=update_img_name)


   

if __name__ == '__main__':
    app.run(debug=True, port=5050)
