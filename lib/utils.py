from .config import GROQ_API_KEY, MODEL_NAME
from groq import Groq

client = Groq(api_key=GROQ_API_KEY)

def groq_infer(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=MODEL_NAME,
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content
