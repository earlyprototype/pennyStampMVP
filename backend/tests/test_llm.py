from ..src.llm.llama import generate_output

prompt = "Print 'Hello Thom' in your next response, only. Include no other text"
generated_output = generate_output(prompt)
print(generated_output)