import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are ai assisntant who is expert in breaking down complex problem and then ressolve the user query

for the given user input analyse the user input and breaak down the problem step by step

Atlest think 5-6 steps on how to solve problem before solving it down.

the steps are u get a uesr input , you analyse , you think , you again think you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final; result.


follow the steps insequence that is "analyse" , "think" , "Output" , "Validate" and finally "result".


Rules :
1. follow the strict JSON output as per output schema 
2. Alway perform one step at a time and wait for next input.
3.Carefully analyse the user query.

Output format :
{{steps : "string" , content: "string"}}
Example : 
Input : what is 2 + 2
Output : {{step : "Analyse",contenet : "Alright! teh user is interested in maths query and he is asking a basic arthmatic operation"}}

Output : {{step : "Think" , content : "To perform the addition i must go from left to right and add all operants"}}

Output : {{step : "Validate" , content : "Seems like 4 is correct ans for 2 + 2 "}}

Output : {{step : "Result" , content : " 2 + 2 = 4 and that is calculated by adding all numbers"}}

"""
result = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system", "content":system_prompt},
        {"role":"user", "content":"what is i dont know"},

        #
        {"role":"assistant", "content":json.dumps({"jo bhi output aayega usey idhar paste kardo"})},
        {"role":"assistant", "content":json.dumps({"Firse wohi"})},
        #...so on

    ],
)
print(result.choices[0].message.content)
