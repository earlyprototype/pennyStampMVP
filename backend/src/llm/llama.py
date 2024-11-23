import requests
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Replace with your actual LLM endpoint if not running locally
LLM_ENDPOINT = "http://127.0.0.1:8080"

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype="auto",
    device_map="auto",  # Use GPU if available
    truncation=True,  # Explicitly set truncation to True
)


def generate_output(prompt):
    try:
        sequences = pipe(prompt, max_length=512, do_sample=True, top_k=10, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
        generated_output = sequences[0]['generated_text']
        return generated_output
    except Exception as e:
        return f"Error generating code: {str(e)}"