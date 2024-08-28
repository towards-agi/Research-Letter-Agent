from openai import OpenAI
from config import config


def generate_response(system_prompt, user_prompt, model):
    client = OpenAI(api_key=config.OPENAI_API_KEY)

    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        stream=True,
    )

    response_content = ""
    total_tokens = 880

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response_content += chunk.choices[0].delta.content

    return response_content, total_tokens #Legacy Placeholder
