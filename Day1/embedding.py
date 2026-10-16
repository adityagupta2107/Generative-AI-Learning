from dotenv import load_dotenv
from openai import OpenAI

load_dotenv();

client = OpenAI();
text = "Eiffel Tower is in paris and is a famous landmark , it is 324 meter tall"

responce = client.embeddings.create(
    input=text,
    model="--"
)

print("Vector Embedding : ",responce.data[0].embedding)