# Image Model Cloudflare Workers AI Streamlit starters

This is a collection of [Streamlit](https://streamlit.io) applications that are making use of [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/)

[![YouTube - Image Generation, Inpainting, and Vision Models](http://img.youtube.com/vi/8SnrvAYAJ4Q/0.jpg)](http://www.youtube.com/watch?v=8SnrvAYAJ4Q "Image Generation, Inpainting, and Vision Models")

This, like all of us, is a Work in Progress.

## Installation

Copy [.streamlit/secrets.toml.example](./.streamlit/secrets.toml.example) to `.streamlit/secrets.toml`.

```bash
python -m venv venv
source ./venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

Streamlit applications can be started like so:

```bash
python -m streamlit run Hello.py
```