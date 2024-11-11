from transformers import pipeline
import torch
import random


def generate_random_names():
    seed = random.randint(5000, 2 ** 32 - 1)
    torch.manual_seed(seed)
    text_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
    res = text_generator(
        "Once upon a time, in a small village, there was a young boy named",
        #   max_length=1,
        max_new_tokens=1,  # Limit the output to just one word
        do_sample=True,  # Enable sampling for variety
        temperature=0.8,  # Controls randomness (higher values result in more creative output)
        top_p=0.9,  # Nucleus sampling to focus on the top possibilities
        return_full_text=False  # Only return the completion, not the prompt
    )
    print(res)


generate_random_names()
