import os
from langchain import HuggingFaceHub

# Set the API key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

# Select the LLMs model
repo_id = "bigscience/bloom" # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0.1, "max_length":24})