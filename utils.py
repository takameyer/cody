from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

import os


# Initialize the OpenAI LLM
def initialize_llm():
    return ChatOpenAI(
        model_name="gpt-4o",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )


# Analyze the file and generate a summary
def analyze_file(code):
    llm = initialize_llm()
    prompt = PromptTemplate(
        input_variables=["code"],
        template=(
            "You are an expert JBoss application developer. Look at the given source code and explain how it works to a junior developer that has never used JBoss before:\n\n"
            "{code}"
        ),
    )
    return llm.invoke(prompt.format(code=code))


# Annotate the code with comments explaining its functionality
def annotate_code(code):
    llm = initialize_llm()
    prompt = PromptTemplate(
        input_variables=["code"],
        template=(
            "You are an expert programmer. Add comments to the following code to explain its functionality:\n\n"
            "{code}"
        ),
    )
    return llm.invoke(prompt.format(code=code))
