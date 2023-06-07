import os
from langchain import HuggingFaceHub

os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

repo_id = "bigscience/bloom" # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0.1, "max_length":256})
prompt = "Who won the FIFA World Cup in the year 2018? Give me one country name."

print(llm(prompt))