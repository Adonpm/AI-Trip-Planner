from fastapi import FastAPI
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
import os
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],  # Set specific origins in prod
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class QueryRequest(BaseModel):
    question:str

@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()

        # Creating graph and saving
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("react_graph.png", "wb") as f:
            f.write(png_graph)
        print(f"Graph saved as 'react_graph.png' at {os.getcwd()}")
        
        # Converting user question to MessagesState format and invoking
        messages = {"messages": [query.question]}
        output = react_app.invoke(messages)

        # If result is dict with messsages
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content # Last AI response content
        else:
            final_output = str(output)
        
        return {"answer": final_output}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
