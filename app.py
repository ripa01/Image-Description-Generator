import gradio as gr
from transformers import pipeline

# Image to text function
def image2text(image_path):
    captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
    text = captioner(image_path)[0]['generated_text']
    return text

# Gradio interface
iface = gr.Interface(
    fn=image2text,
    inputs=gr.Image(type="filepath", label="Upload Image"),
    outputs="text",
    title="Image Description Generator",
    description="Upload an image and get a generated description."
)

if __name__ == "__main__":
    iface.launch(inline=False)
