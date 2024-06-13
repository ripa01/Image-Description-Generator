# Image Description Generator

This project demonstrates how to use a Hugging Face model for image captioning and deploy it using Gradio and Hugging Face Spaces. The app allows users to upload an image and get a generated description of the image using a pre-trained model from Hugging Face.

## Features

- **Image Upload:** Users can upload an image from their local device.
- **Image Captioning:** The app generates a textual description of the uploaded image using the `Salesforce/blip-image-captioning-large` model.
- **User Interface:** A simple and intuitive interface built with Gradio.


## Deploying on Hugging Face Spaces

1. **Create a new Space on Hugging Face Spaces.**

2. **Choose Gradio as the SDK.**

3. **Upload the following files to your Space repository:**
   - `app.py`
   - `requirements.txt`

4. **Once the files are uploaded, the Space will automatically build and deploy your app.**


## Usage

1. Open the web application.
2. Upload an image using the provided upload button.
3. The app will generate and display a description of the uploaded image.

## Learnings

Through this project, I learned:

- How to use Hugging Face's transformers library to load and use pre-trained models.
- How to build interactive web applications with Gradio.
- How to deploy applications on Hugging Face Spaces.

## Conclusion

This project provided hands-on experience with modern machine learning tools and deployment platforms, enhancing my skills in both model deployment and web application development.


