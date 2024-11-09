import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load DistilGPT2 model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")

# Input text
input_text = "Generate a random number."

# Tokenize the input
inputs = tokenizer(input_text, return_tensors="pt", add_special_tokens=True)

# Forward pass (no gradients needed)
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# Find the predicted token (highest logit) for the next word
predicted_token_class_ids = logits.argmax(-1)

# Decode the predicted token IDs to text
predicted_tokens = tokenizer.decode(predicted_token_class_ids[0], skip_special_tokens=True)

# Print the generated text
print(predicted_tokens)

# Calculate the loss for the input
labels = predicted_token_class_ids
loss = model(**inputs, labels=labels).loss
print(f"Loss: {round(loss.item(), 2)}")
