from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader

import os


def load_documents():
    loader = DirectoryLoader("./.test/kitchensink/", glob="**/*[!png|jpg|gif]")
    docs = loader.load()
    return docs


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
    docs = load_documents()
    prompt = PromptTemplate(
        input_variables=["code"],
        template=(
            "You are an expert JBoss and Spring Boot application developer. Given the context.  Tell me about the controllers and how they work.  Also tell me what dependencies are in the pom.xml:\n\n"
            "{context}"
        ),
    )
    cody_chain = prompt | llm
    return cody_chain.invoke({"context": docs})


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
