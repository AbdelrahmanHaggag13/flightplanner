# ✈️ Flight Planner AI — A Multi-Agent Travel Planner with LangGraph

An open-source AI travel planner that turns a natural-language trip request into a practical travel plan with flight suggestions, hotel ideas, and a day-by-day itinerary. The project uses a multi-agent workflow built with LangGraph, LangChain, and FastAPI.

## Why this project?

Planning a trip usually means jumping between multiple websites, tools, and spreadsheets. This project brings that flow into one experience by combining:

- a flight-search agent,
- a hotel-research agent,
- an itinerary-planning agent, and
- a final response agent,

all coordinated through a LangGraph workflow.

## Features

- ✈️ Flight research using AviationStack
- 🏨 Hotel suggestions using Tavily search
- 🧠 Multi-agent orchestration with LangGraph
- 📝 Structured travel itinerary generation
- 🌐 FastAPI backend with a simple web interface
- 💾 Conversation state persistence using PostgreSQL
- ⚡ LLM-powered responses with Openai or (any free provider )

## Tech Stack

- Python 3.10+
- FastAPI
- Jinja2 + HTML/CSS/JavaScript frontend
- LangGraph
- LangChain
- Openai LLMs
- PostgreSQL
- Tavily API
- AviationStack API

## Project Structure

```text
.
├── src/
│   ├── app.py            # FastAPI app entry point
│   ├── backend.py        # LangGraph travel workflow
│   ├── static/           # JS / CSS
│   ├── templates/        # Jinja2 templates
│   └── tools/            # Flight and web search integrations
├── pyproject.toml        # Dependencies (managed by uv)
├── uv.lock
└── .python-version
```

## Prerequisites

Before running the project locally, make sure you have:

- Python 3.10 or newer installed
- PostgreSQL running and accessible
- API keys for:
  - openai
  - Tavily
  - AviationStack

## Environment Variables

Create a .env file in the project root with the following variables:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/tripAgents
OPENAI_API_KEY=your_openai_api_key 
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key
DEFAULT_ORIGIN_IATA=CAI
```

## Installation

Make sure you have [uv](https://docs.astral.sh/uv/) installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # macOS / Linux / WSL
# Windows (PowerShell): powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then clone the repo and install the dependencies:

```bash
git clone https://github.com/AbdelrahmanHaggag13/flightplanner.git
cd flightplanner
uv sync
```

`uv sync` creates the `.venv` and installs everything from `pyproject.toml` / `uv.lock` automatically, so there is no need to activate the environment manually.

## Database Setup

```bash
createdb tripAgents
```

Make sure `DATABASE_URL` in your `.env` matches your PostgreSQL user and password.

## Run

```bash
uv run python src/app.py
```

Then open your browser at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

- GET /health - Health check
- POST /api/travel - Submit a travel request

Example request:

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{"message":"Plan a 3-day trip to Tokyo with a budget of $1200"}'
```

## How the Workflow Works

1. The user submits a travel request.
2. The flight agent gathers flight-related information.
3. The hotel agent searches for accommodation suggestions.
4. The itinerary agent creates a practical travel plan.
5. The final agent formats the result into a polished response.


## Acknowledgments

This project is built with the help of modern LLM tooling and travel APIs, and it is intended as a practical example of combining LangGraph agents with real-world applications.

## Limitations

- Flight data comes from AviationStack, which provides live flight status, not ticket prices or future schedules.