import openai

# Set your OpenAI API key
openai.api_key = ''

# Define a formatted prompt
prompt = """
complete the sentence given below:

Text: "The quick brown fox"

completed sentence:
"""

# Make a request to the OpenAI API using the new ChatCompletion method
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # Use a suitable chat model
    messages=[{"role": "user", "content": prompt}],
    max_tokens=50,  # Limit the response length
    temperature=0.7,  # Control the randomness of the response
    n=1,  # Number of responses to generate
    stop=None  # Define a stopping sequence if needed
)

# Extract and print the response text
summary = response.choices[0].message.content.strip()  # Access content directly
print(f"Generated Summary:\n{summary}")
