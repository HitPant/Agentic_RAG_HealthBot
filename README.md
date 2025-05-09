# Health_Insurance-AgenticRAG

## Introduction
This project presents the second version of the Health Insurance ChatBot, redesigned as an **Agentic RAG system** to deliver advanced, context-aware, and tool-empowered healthcare and insurance insights.

Unlike traditional chatbots limited by static workflows, this AI agent dynamically reasons, interacts, and invokes external tools or APIs on demand to generate precise and actionable responses for complex healthcare-related queries.

---

## Objective
Build an agentic Retrieval-Augmented Generation (RAG) system capable of:
- Handling complex, multi-step healthcare and insurance queries.
- Dynamically integrating external tools and APIs to enrich responses.
- Providing an enhanced, interactive user experience for residents and international students navigating the U.S. healthcare system.

---

## Key Features
✅ **Agentic RAG Architecture**  
Moves beyond simple retrieval setups by using agent-based planning and decision-making.

✅ **Tool & API Integration**  
Dynamically calls external services and tools to fetch real-time or enriched information.

✅ **Improved Context Understanding**  
Better handles multi-turn, context-rich interactions to deliver relevant insights.

✅ **Modular & Extensible Design**  
Allows future integration of specialized agents and expanded functionality.

---

## Tech Stack

| Component            | Technology                                  |
|----------------------|-------------------------------------------|
| **Agents & Tooling** | Agno (for building dynamic AI agents)      |
| **LLMs**             | Groq (for scalable, fast language inference)|
| **Frontend**         | Streamlit (for interactive web interface)   |

---

## How It Works

1️⃣ **Query Input**  
User submits a healthcare or insurance-related question.

2️⃣ **Agent Reasoning**  
Agent plans steps: decides whether to retrieve, reason, or call tools/APIs.

3️⃣ **Action Execution**  
Agent uses Groq LLM for reasoning and Agno-integrated tools or APIs for enriched answers.

4️⃣ **Response Delivery**  
Final, contextually relevant answer is displayed on the Streamlit frontend.

---

## Future Roadmap
- Add specialized agents (e.g., claims assistant, provider lookup).
- Integrate more real-time healthcare data sources.
- Expand to handle multi-modal inputs (e.g., forms, documents).
- Improve memory handling for longer conversations.

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/HitPant/Health_Insurance-ChatBot.git

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
