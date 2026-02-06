from graph import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("Initialising Research Agent...")

    user_task = input("Enter your research question : ")

    # defining the users input
    initial_state = {
        "task" : user_task,
        "plan" : [],
        "content" : [],
        "revision_number" : 0,
        "max_revisions" : 2
    }

    # run the graph
    print(f"Starting Task: {initial_state["task"]}")

    for output in app.stream(initial_state):
        for node_name , state_update in output.items():
            print(f"\n---Finished Node : {node_name} ---")

            # print specific updates
            if node_name == "planner":
                print(f"Plan : {state_update.get("plan")}")
            elif node_name == "generator":
                print(f"Draft:\n{state_update.get("draft")}")