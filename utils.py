from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
import os

# Define a new graph


def open_chat(project_path, prompt):
    def call_model(state: MessagesState):
        prompt_template = PromptTemplate(
            template=(
                prompt
                + "\n\nYou will be prompted about a project which is provided in the context.\n\n"
                "{context}"
            ),
        )
        cody_chain = prompt_template | model
        response = cody_chain.invoke([{"context": docs}, state["messages"]])
        return {"messages": response}

    model = ChatOpenAI(
        model_name="gpt-4o",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
    loader = DirectoryLoader(project_path, glob="**/*[!png|jpg|gif]")
    docs = loader.load()

    # Define the (single) node in the graph
    workflow = StateGraph(state_schema=MessagesState)
    workflow.add_edge(START, "model")
    workflow.add_node("model", call_model)

    # Add memory
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)

    config = {"configurable": {"thread_id": "abc123"}}

    print("Conversation has been opened.  Type 'quit' to leave\n")

    while True:
        query = input(">>> ")
        if query == "quit":
            break
        input_messages = [HumanMessage(query)]
        for chunk, metadata in app.stream(
            {"messages": input_messages}, config, stream_mode="messages"
        ):
            if isinstance(chunk, AIMessage):
                for byte in chunk.content:
                    print(byte, end="", flush=True)
        print("\n")
