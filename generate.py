import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

def generate_solution_with_openai(prompt):
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="o1-preview",
)
    
    return response['choices'][0]['message']['content']

# Example prompt (adjust this as needed)
prompt = """Write a bash script that takes a matrix represented as a string with format '[1,2],[3,4],[5,6]' and prints the transpose in the same format."""

# Get the response from OpenAI
solution = generate_solution_with_openai(prompt)