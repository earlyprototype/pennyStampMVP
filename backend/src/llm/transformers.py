from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')  # Initialize the pipeline

def generate_code(prompt):
    try:
        response = generator(prompt, max_length=200, num_return_sequences=1)  # Adjust parameters as needed
        generated_code = response[0]['generated_text']
        return generated_code
    except Exception as e:
        return f"Error generating code: {e}"