# Testing the CBSE Question Generator API

This guide explains how to set up, run, and test the backend API.

## 1. Prerequisites

- **Python 3.9+** installed.
- **Google AI Studio API Key**: Ensure you have a valid key in `app/.env`.

## 2. Setup

First, install the required dependencies:

```bash
pip install -r app/requirements.txt
```

## 3. Running the Server

Start the FastAPI server by running `main.py`:

```bash
python app/main.py
```

The server will start at `http://localhost:8000` (or the port specified in your `.env`).

## 4. Testing Methods

### A. Interactive API Documentation (Swagger)
The easiest way to test is using the built-in Swagger UI:
1. Open your browser and go to: [http://localhost:8000/docs](http://localhost:8000/docs)
2. You will see all available endpoints.
3. Click on **`POST /api/v1/questions/generate`** -> **Try it out**.
4. Use the following sample payload:

```json
{
  "class": 10,
  "subject": "mathematics",
  "chapter": 1,
  "total_questions": 5,
  "difficulty": "medium"
}
```
5. Click **Execute**.

### B. Testing via CURL
You can also test the API from your terminal:

```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/questions/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "class": 10,
  "subject": "mathematics",
  "chapter": 1,
  "total_questions": 3,
  "difficulty": "mixed"
}'
```

### C. Health Check
To verify the server and AI model configuration are working:
- Visit: [http://localhost:8000/health](http://localhost:8000/health)

## 5. Troubleshooting

- **422 Unprocessable Entity**: Check if your request body matches the schema (e.g., class must be 9 or 10).
- **502 Bad Gateway**: This usually means the Gemini API returned an invalid response or failed to parse. Check the server logs.
- **503 Service Unavailable**: Likely an issue with the Gemini API key or quota.
