# Quentum Grade

A grading tool that utilizes the Model Context Protocol (MCP) for intelligent assessment and feedback.

## Features

- MCP-based grading system
- RESTful API interface
- Configurable grading parameters
- Detailed feedback generation

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your configuration:
```bash
cp .env.example .env
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, visit `http://localhost:8000/docs` for the interactive API documentation.

## License

MIT