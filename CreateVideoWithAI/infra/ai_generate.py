from infra.logger_setup import logger_setup
import logging

from transformers import pipeline
import torch
import random


def generate_random_name_ai():
    text_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
    retries = 10  # Maximum number of attempts

    for _ in range(retries):
        seed = random.randint(5000, 2 ** 32 - 1)
        torch.manual_seed(seed)

        # Generate text with the model
        res = text_generator(
            "Once upon a time, in a small village, there was a young boy named",
            max_new_tokens=1,  # Limit the output to just one word
            do_sample=True,
            temperature=0.8,
            top_p=0.9,
            return_full_text=False
        )

        # Extract the generated name
        generated_text = res[0]['generated_text'].strip()
        name = generated_text.split()[0]  # Get the first word

        print(f"Generated name: {name}")

        # Check if the name is equal or longer than 3 characters
        if len(name) >= 3:
            return name

    # If no valid name was found after retries
    return "James"


def determine_video_context (title, audience_labels, style_labels):
    # Initialize the zero-shot classifier
    classifier = pipeline("zero-shot-classification")

    # Classify audience
    audience_result = classifier(title, candidate_labels=audience_labels)
    audience = audience_result['labels'][0]

    # Classify style
    style_result = classifier(title, candidate_labels=style_labels)
    style = style_result['labels'][0]

    print(f"Audience: {audience}")
    print(f"Style: {style}")
