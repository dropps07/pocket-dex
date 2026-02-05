import os
import json
from langchain_ollama import ChatOllama
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage , SystemMessage

# ****************** setting up the model *************************
model = ChatOllama(model = "llama3" , format=json)

tavily = TavilySearchResults(max_results = 3)



# ****************** setting up the planner node ******************
def plan_node(state):
    print("---Planning Step---")
    task = state["task"]

    prompt = f"""
You are a Research Planner.
Your task is to break down a users request into search queries.

User Request : {task}

Return a JSON object with a single key "steps" which is a list of strings.
Example : {{"Steps" : ["search query 1" , "search query 2"]}}
"""
    response = model.invoke([HumanMessage(content=prompt)])

    # parsing the json response manually
    try:
        content = response.content.strip()
        if "```" in content :
            content = content.split("```")[1].replace("json" , "").strip()
            plan_data = json.loads(content)
            steps = plan_data.get("steps" , [task])
    except Exception as e:
        print(f"JSON parsing Error: {e}")
        steps = [task]

    print(f"Generated Plan : {steps}")
    return {"plan" : steps}


# ****************** setting up the RESEARCHER node *******************
def researcher_node(state):
    print("---Researching---")
    plan = state["plan"]
    content = []

    for query in plan:
        print(f"Searching : {query}")
        try :
            results = tavily.invoke(query)
            for result in results:
                content.append(result["content"])
        except Exception as e:
            print(f"Search error for {query}: {e}")

    return {"content" : content}



# **************** setting up the generator node ***********************
def generation_node(state):
    print("---Generating draft---")
    content = "\n\n".join(state["content"])
    task = state["task"]

    prompt = f"""
You are a Research Assistant.
Write a detailed response to the user's question based ONLY on the provided context.

CONTEXT : {content}

QUESTION : {task}
"""
    
    response = model.invoke([HumanMessage(content = prompt)])
    return {"draft" : response.content} 