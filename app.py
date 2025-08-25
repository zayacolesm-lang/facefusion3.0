import gradio as gr
import cv2
from PIL import Image
import numpy as np

# Funcție de test (momentan doar încarcă imaginea și o returnează)
def run_facefusion(image):
    img = np.array(image)
    return Image.fromarray(img)

demo = gr.Interface(
    fn=run_facefusion,
    inputs=gr.Image(type="pil", label="Încarcă o imagine"),
    outputs=gr.Image(type="pil", label="Rezultatul"),
    title="FaceFusion 3.0"
)

if _name_ == "_main_":
    demo.launch(server_name="0.0.0.0", server_port=7860)
