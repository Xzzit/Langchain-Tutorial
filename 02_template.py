import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate

os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

repo_id = "bigscience/bloom"
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0.1, "max_length":256})

template = "Who won the FIFA World Cup in the year {year}? Give me one country name."
prompt = PromptTemplate(
    input_variables=["year"],
    template=template,
)

print(llm(prompt.format(year=2018)))