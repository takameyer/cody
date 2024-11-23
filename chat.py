from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage, AIMessage

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

model = ChatOpenAI(model="gpt-4o")

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


# Define the (single) node in the graph
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
