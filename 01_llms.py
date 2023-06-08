from llms import *

# prompt 1
prompt = "Who won the FIFA World Cup in the year 2018? Give me one country name."
print(llm(prompt))
print('-'*50)

# prompt 2
prompt = "what is 1+1?"
print(llm(prompt))
print('-'*50)

# prompt 3
customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""
style = """American English \
in a calm and respectful tone
"""
prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {style}.
text: ```{customer_email}```
"""
print(prompt)
print(llm(prompt))
print('-'*50)

# prompt 4
prompt = "热干面是哪里的小吃？"
print(llm(prompt))