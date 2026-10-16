import tiktoken
encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size",encoder.n_vocab) #Vocab Size 200019

text = "the cat sat on mat"
tokens = encoder.encode(text)
print("Tokens : ",tokens) #Tokens :  [3086, 9059, 10139, 402, 2450]

decode = encoder.decode([3086, 9059, 10139, 402, 2450])
print("Decoded : ",decode)