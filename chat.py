from openai import OpenAI 
# requires an OpenAI key lol

client = OpenAI()

user_prompt=("Prompt: ") # where the user can input questions and stuff for the ai
system_prompt = "Limit your answer to one sentence. Pretend you're a cat." # instructions for the ai to do

response = client.responses.create(
    input=user_prompt,
    instructions=system_prompt,
    model="gpt-5"
)

print(response.output_text)