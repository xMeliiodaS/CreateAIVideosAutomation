from transformers import pipeline

# Initialize the text generation pipeline
text_generator = pipeline("text-generation", model="distilgpt2")

# Generate text
res = text_generator(
    "In this sentence, we will generate a human name, the human name is",
    max_length=30,
    num_return_sequences=2,
)

print(res)
