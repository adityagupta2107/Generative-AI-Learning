from google import genai
from google.genai import types

client = genai.Client(api_key="---")
responce = client.models.generate_content(
    model="--",contents='whyy??...'
)
print(responce.text)