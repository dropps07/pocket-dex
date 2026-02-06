# kenkyū (研究)

**kenkyū** is an autonomous AI Research Agent built using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and [Ollama](https://ollama.com/). It automates the process of planning research queries, gathering information from the web, and synthesizing a comprehensive report.

## 🚀 Features

- **Multi-Agent Workflow**: Uses a stateful graph to manage research phases.
- **Automated Planning**: Breaks down complex research tasks into targeted search queries.
- **Web Research**: Integrates with [Tavily](https://tavily.com/) for high-quality, real-time web search results.
- **Local LLM Support**: Leverages Ollama (Llama 3) for privacy-conscious, local text generation and planning.
- **State Management**: Maintains context throughout the research process.

## 🏗️ Architecture

The agent follows a three-step sequential workflow:

1.  **Planner**: Analyzes the user's task and generates a structured research plan consisting of multiple search queries.
2.  **Researcher**: Executes the search queries using the Tavily API and collects relevant content.
3.  **Generator**: Synthesizes the collected information into a detailed final response.

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd "Research Agent Project"
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your Tavily API key:
```env
TAVILY_API_KEY=your_tavily_api_key_here
```

### 5. Ensure Ollama is Running
Make sure you have [Ollama](https://ollama.com/) installed and the `llama3` model pulled:
```bash
ollama pull llama3
```

## 🖥️ Usage

Run the main script to start the research agent:
```bash
python main.py
```

Follow the prompt to enter your research question.

## 🧰 Tech Stack

- **Framework**: LangGraph
- **LLM Orchestration**: LangChain
- **LLM**: Ollama (Llama 3)
- **Search Engine**: Tavily Search
- **Language**: Python
