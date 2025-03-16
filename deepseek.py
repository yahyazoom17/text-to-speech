from groq import Groq
import re
from helper import remove_thinking

client = Groq(api_key="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")

def ask_deepseek(user_input):
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[{
            "role": "system",
            "content": "Your name is Vectora. You are a friendly helpful assistant created by Yahya. Don't reveal your actual information about who you are and who created you. Just say that you are vectora created by Yahya.If you don't know any answers say that you don't know."
        },
        {
            "role": "user",
            "content": f"{user_input}"
        }],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=0.95,
        stream=False,
        stop=None,
    )

    # Extract and return only the response text
    response_text = completion.choices[0].message.content
    text = remove_thinking(response_text)
    return [text, completion]