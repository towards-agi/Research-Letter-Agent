import openai
from config import config

def generate_response(system_prompt, user_prompt, model):
    openai.api_key = config.OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response['choices'][0]['message']['content'], response['usage']['total_tokens']
