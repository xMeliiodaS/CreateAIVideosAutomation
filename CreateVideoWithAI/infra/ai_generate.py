import openai

openai.api_key = "your-api-key"

def generate_name():
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3 engine
        prompt="Generate a random name.",
        max_tokens=1
    )
    return response.choices[0].text.strip()

def generate_video_topics():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Give me 5 unique and interesting YouTube video topics about technology.",
        max_tokens=1
    )
    return response.choices[0].text.strip()
