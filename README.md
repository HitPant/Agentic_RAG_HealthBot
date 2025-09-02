# Health_Insurance-AgenticRAG

## Introduction
Navigate care & insurance with confidence. This project is a Streamlit chat application powered by an agentic Retrieval‑Augmented Generation (RAG) workflow. The agent first searches a vectorized PDF knowledge base (your documents), and when needed falls back to web search, then composes clear, contextual answers.


## What this project does:
Provides a chat UI where users ask U.S. healthcare & health‑insurance questions.
Uses an Agent (from the phi/Agno toolkit) that:
  - Searches a PDF knowledge base backed by Postgres + pgvector with Mistral embeddings and hybrid search (semantic + keyword).
  - Falls back to Google Search when the internal knowledge base doesn’t provide a decisive answer.
  - Maintains chat history for context and is time‑aware in its reasoning.
  - Responds in Markdown with concise, high‑quality explanations.

---

## Architecture
✅ **Knowledge Base**  
PDF documents under pdf_data/ are chunked (size=1024, overlap=20) and embedded using Mistral, then stored in a Postgres table (e.g., v2_health_insurace_data) with pgvector. The agent queries this KB first (hybrid search). If confidence is low or info is missing, it queries the web.

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

## Configuration knobs (code‑level)
  - Model: Groq gemma2-9b-it (swap to another via phi.model.* if desired).
  - Knowledge search: enabled by default; agent queries the KB first.
  - Vector DB table: v2_health_insurace_data (change the name if you want separate indices).
  - Chunking: chunk_size=1024, overlap=20 for PDFs.
  - Search type: hybrid (semantic + keyword).
  - Tools: GoogleSearch() is enabled; you can add others (e.g., DuckDuckGo) using the phi.tools suite.
  - Chat memory: enabled; the agent can read prior chat messages for context.

---

## Future Roadmap
- **More tools**: Add claims calculators, provider directory lookups, benefits comparisons.
- **Alternate embeddings**: Swap to another embedder (e.g., OpenAI, Cohere) if preferred.
- **Alternate LLMs**: Use Gemini, OpenAI, or local models via `phi.model.*` providers.
- **Multi‑tenant KBs**: Change table names or schemas to isolate per‑tenant data.

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/HitPant/Health_Insurance-ChatBot.git

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
