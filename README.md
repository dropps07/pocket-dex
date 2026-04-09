# PocketDex (研究)

**PocketDex** is an autonomous AI-powered research agent built using **LangGraph**, **LangChain**, and **Ollama**.  
It streamlines the entire research workflow—planning queries, collecting information from the web, and generating structured insights.

---

## Features

- **Agent-Based Workflow**  
  Uses a stateful graph architecture to coordinate multiple research stages  

- **Intelligent Query Planning**  
  Breaks down complex topics into focused, high-quality search queries  

- **Real-Time Web Research**  
  Integrates with Tavily to fetch relevant and up-to-date information  

- **Local AI Execution**  
  Powered by Ollama (Llama 3) for privacy-first, offline-capable inference  

- **Context Retention**  
  Preserves state across the pipeline for coherent and consistent outputs  

---

## Architecture

PocketDex operates through a three-step pipeline:

1. **Planner**  
   Understands the input query and generates a structured research plan  

2. **Researcher**  
   Executes the generated queries using Tavily and gathers relevant data  

3. **Generator**  
   Synthesizes all collected information into a detailed and readable report  

---

## Installation

### 1) Clone the Repository
```bash
git clone <repository-url>
cd "Research Agent Project"
