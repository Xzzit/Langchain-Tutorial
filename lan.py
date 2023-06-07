import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

repo_id = "stabilityai/stablelm-tuned-alpha-3b" # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0, "max_length":256})


question = "Who won the FIFA World Cup in the year 2010? "
template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.run(question))