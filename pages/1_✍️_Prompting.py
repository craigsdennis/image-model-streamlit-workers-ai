import requests
import streamlit as st


"# Prompting"

with st.form("text_to_image"):
    # All models at https://developers.cloudflare.com/workers-ai/models/
    model = st.selectbox(
        "Choose your Text-To-Image model",
        options=(
            "@cf/lykon/dreamshaper-8-lcm",
            "@cf/bytedance/stable-diffusion-xl-lightning",
            "@cf/stabilityai/stable-diffusion-xl-base-1.0",
        ),
    )
    prompt = st.text_area("Prompt")
    submitted = st.form_submit_button("Generate")
    if submitted:
        account_id = st.secrets["CLOUDFLARE_ACCOUNT_ID"]
        api_token = st.secrets["CLOUDFLARE_API_TOKEN"]
        headers = {
            "Authorization": f"Bearer {api_token}",
        }
        with st.spinner("Generating..."):
            url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}"
            response = requests.post(
                url,
                headers=headers,
                json={"prompt": prompt},
            )
            st.image(response.content, caption=prompt)
            f"_Generated with [Cloudflare Workers AI](https://developer.cloudflare.com/workers-ai/) using the `{model}_`"
        with st.spinner("Creating additional prompt suggestions..."):
            prompt_model = "@hf/thebloke/mistral-7b-instruct-v0.1-awq"
            prompt_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{prompt_model}"
            system_message = """
            You are a Stable Diffusion prompt engineer. 
            
            The user is going to give you a prompt, and you will provide three detailed suggestions. 
            
            Use various photo stylistic terms.
            """
            prompt_suggestion_response = requests.post(
                prompt_url,
                headers=headers,
                json={
                    "messages": [
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": prompt},
                    ]
                },
            )
            json = prompt_suggestion_response.json()
            result = json["result"]
            if "response" in result:
                st.write(result["response"])
                f"_Generated with [Cloudflare Workers AI](https://developer.cloudflare.com/workers-ai/) using the `{prompt_model}` model_"
            else:
                st.write(result)
