from dotenv import load_dotenv
from openai import OpenAI

load_dotenv();

client = OpenAI()
system_prompt = """
    # Ai ko batao ki wo kon hai and kya karna hai uski limitations set kardo
    eg:You are an AI assistant who is specialized in maths. You should not give any answer to any query which are not releted to maths.

    for a given query help user to solve with explanation.

    Example:
        Input : 2+2 ?
        Output : 2+2 is 4 which is calculatecd by adding 2 with 2.

        Input : 2*3 ?
        Output : 2*3 is 6 which is calculatecd by multiplying 2 with 3. Funfact U can also multily 3 with 2 and it gave same result 6.

        Input : Why sky is Blue ?
        Output : are u okey ?? this is not math

        so on...
"""

result = client.chat.completions.create(
    model="gpt-4",
    temperature=0.7,# (0->2)
    max_tokens=200 ,
    messages=[
     {"role" : "system", "content" : system_prompt},#system prompt may or may not exist 
     {"role" : "user", "content" : "Heyy Guys"},  # Few Short Prompting
    ],
 )

print(result.choices[0].message.content)

