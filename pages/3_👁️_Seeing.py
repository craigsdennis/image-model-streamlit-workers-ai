import io
import os

from dotenv import load_dotenv
import requests
import streamlit as st


load_dotenv()

"# Seeing is believing"

image_upload = st.file_uploader("Gimme a photo")

if not image_upload:
    st.stop()
from PIL import Image, ImageOps

img = Image.open(image_upload)
img = ImageOps.contain(img, (600, 600))

st.image(img)

def image_to_int_array(image, format="PNG"):
    """Current Workers AI REST API consumes an array of unsigned 8 bit integers"""
    bytes = io.BytesIO()
    image.save(bytes, format=format)
    return list(bytes.getvalue())



with st.form("ask-about-photo"):
    prompt = st.text_area(
        "Ask a question about the photo",
        value="Describe what is happening in this photo.",
    )
    submitted = st.form_submit_button("Ask")
    if submitted:
        with st.spinner("Processing image..."):
            api_token = os.environ["CLOUDFLARE_API_TOKEN"]
            account_id = os.environ["CLOUDFLARE_ACCOUNT_ID"]
            headers = {
                "Authorization": f"Bearer {api_token}",
            }

            model = "@cf/unum/uform-gen2-qwen-500m"
            url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}"
            response = requests.post(
                url,
                headers=headers,
                json={
                    "prompt": prompt,
                    "image": image_to_int_array(img),
                },
            )
            if response.ok:
                json = response.json()
                st.write(json["result"]["description"])
                f"_Generated with [Cloudflare Workers AI](https://developer.cloudflare.com/workers-ai/) using the `{model}` model_"
            else:
                st.write(response.status_code)
                st.write(response.reason)
                st.code(response.content)