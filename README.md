# Streamlit Cloudflare Workers AI starters

This is a collection of [Streamlit](https://streamlit.io) applications that are making use of [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/)

## Installation

Copy [.env.example](.env.example) to `.env`.

```bash
python -m venv venv
source ./venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

Streamlit applications can be started like so:

```bash
python -m streamlit run prompting.py
```

```bash
python -m streamlit run masking.py
```

```bash
python -m streamlit run vision.py
```