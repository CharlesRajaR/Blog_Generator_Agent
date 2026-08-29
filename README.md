# Blog Generator Agent

A FastAPI-based AI content generation service that creates blog content from a user-provided topic using LangGraph orchestration and Google Gemini models. The application follows a simple multi-step workflow: generate a blog title, then generate the final article content, and return the result as a structured JSON payload.

## Overview

This project demonstrates how to combine:

- FastAPI for HTTP API exposure
- LangGraph for workflow orchestration
- LangChain and Google Generative AI for text generation
- Pydantic models for request validation
- A modular architecture for future expansion into research, SEO optimization, and publishing workflows

The service is designed to accept a topic and produce a polished blog post draft with a title and article content.

## Features

- Topic-driven blog generation via REST API
- AI-generated SEO-friendly blog title
- AI-generated markdown blog content
- Workflow-based orchestration using LangGraph
- Easy local development with Uvicorn hot reload
- Environment-based configuration for API keys

## Architecture

The application is organized into a clean, modular structure:

- `app.py` — FastAPI application and API endpoint
- `src/blog_generator_agent/graphs/graph_builder.py` — LangGraph workflow builder
- `src/blog_generator_agent/nodes/blog_node.py` — AI generation steps
- `src/blog_generator_agent/llms/gemini_llm.py` — Gemini model initialization
- `src/blog_generator_agent/state/blog_state.py` — workflow state and schemas

### Workflow

1. The API receives a topic in a JSON payload.
2. The graph starts with a `title_creation` node.
3. The title generation step calls the Gemini model to create a blog title.
4. The workflow proceeds to `content_generation`.
5. The second model call produces markdown-formatted blog article content.
6. The final state is returned to the client.

## Tech Stack

- Python 3.12+
- FastAPI
- Uvicorn
- LangChain
- LangGraph
- Google Generative AI (`langchain-google-genai`)
- Pydantic
- Python-dotenv

## Project Structure

```text
Blog_Generator_Agent/
├── app.py
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── request.json
├── src/
│   └── blog_generator_agent/
│       ├── __init__.py
│       ├── graphs/
│       │   ├── __init__.py
│       │   └── graph_builder.py
│       ├── llms/
│       │   ├── __init__.py
│       │   └── gemini_llm.py
│       ├── nodes/
│       │   ├── __init__.py
│       │   └── blog_node.py
│       └── state/
│           ├── __init__.py
│           └── blog_state.py
└── .env.example
```

## Prerequisites

Before running the project, ensure you have:

- Python 3.12 or newer
- A valid Google Gemini API key
- Access to a terminal or IDE with a Python environment

## Environment Setup

Create a `.env` file in the project root with the following variable:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

This key is read by the application at runtime to initialize the Gemini model.

## Installation

### Option 1: Using pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Option 2: Using uv

```bash
uv sync
```

## Running the Application

Start the FastAPI service locally:

```bash
uvicorn app:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

You can also run the app directly with:

```bash
python app.py
```

## API Endpoints

### POST /blogs

Generates a blog post based on the supplied topic.

#### Request Body

```json
{
  "topic": "Artificial Intelligence in Healthcare"
}
```

#### Example Request

```bash
curl -X POST "http://localhost:8000/blogs" \
  -H "Content-Type: application/json" \
  -d '{"topic":"Artificial Intelligence in Healthcare"}'
```

#### Example Response

```json
{
  "data": {
    "topic": "Artificial Intelligence in Healthcare",
    "blog": {
      "title": "How Artificial Intelligence Is Transforming Modern Healthcare",
      "content": "# How Artificial Intelligence Is Transforming Modern Healthcare\n\nArtificial intelligence is reshaping ..."
    }
  }
}
```

## Request and Response Model

The request payload is validated by Pydantic:

```python
class Topic(BaseModel):
    topic: str
```

The generated blog state is structured as:

```python
class Blog(BaseModel):
    title: str
    content: str

class BlogState(TypedDict):
    topic: str
    blog: Blog
    current_language: str
```

## Notes on the Current Implementation

This project is a strong starting point for an AI-powered blog generation workflow, but it is still a prototype in several respects:

- It currently relies on direct console printing for debugging.
- The code does not include advanced production protections such as request throttling, rate limiting, or authentication.
- Error handling is minimal and could be expanded to return structured API errors for invalid keys, model failures, or malformed requests.
- The workflow is intentionally simple and easy to extend for SEO metadata, keyword generation, or multi-language blogging.

## Production Readiness Considerations

For a production deployment, the following improvements are recommended:

- Move secrets to a secure secret manager rather than `.env` files in local development.
- Add structured logging and request correlation IDs.
- Add retry logic and graceful error responses for LLM failures.
- Provide validation for topic length and content quality.
- Add queue-based or async job processing for large content generation workloads.
- Add monitoring, usage analytics, and cost tracking for Gemini API usage.

## License

This project is currently provided as-is for learning and experimentation. Add an explicit license file if you plan to distribute or deploy it externally.

## Contributing

Contributions are welcome. If you plan to extend this project, consider the following:

- Keep the workflow modular and easy to test.
- Add unit tests for graph nodes and state transitions.
- Improve error handling and observability.
- Document any new endpoints and configuration changes.

## Summary

The Blog Generator Agent is a practical example of combining LLM orchestration and API-driven delivery into a usable content-generation service. It is a solid foundation for building more advanced AI writing workflows, including SEO optimization, topic clustering, article planning, and automatic publishing pipelines.
