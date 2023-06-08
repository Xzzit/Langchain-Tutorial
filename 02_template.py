from llms import *
from langchain import PromptTemplate

# Define the template
user_text = """
唉,老铁,我瞅你咋地？
你这瓜不对吧？卖这么贵给谁吃呢？
我看你就是黑吃黑,打一架？
"""
user_style = """
英语,生气的口气
"""
template = """
Translate the text
that is delimited by triple backticks 
into a style that is {style}.
text: ```{text}```
"""
prompt = PromptTemplate(
    input_variables=["style", "text"],
    template=template
)
print('-'*50)
print(prompt.format(style=user_style, text=user_text))
print('-'*50)
print(llm(prompt.format(style=user_style, text=user_text)))