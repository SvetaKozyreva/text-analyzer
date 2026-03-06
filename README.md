# Project Description

Text Analyzer is a simple web application that analyzes a user-provided text and returns useful statistics.

The application allows a user to enter text into a textarea and click the Analyze button. The backend processes the text and returns:

    Word count
    Character count (with spaces)
    Character count (without spaces)
    Sentence count
    Top 5 most frequent words (excluding stop words)

The backend is implemented using Python and FastAPI, and the frontend is a simple HTML + JavaScript interface that communicates with the API.

**The project was created as part of a Full-Stack Python Developer test assignment**

# Project Structure
text-analyzer
│
├── backend
│   ├── main.py          # FastAPI application and endpoint
│   ├── analyzer.py      # Core text analysis logic
│   └── models.py        # Request and response models
│
├── tests
│   └── test_analyzer.py # Unit tests for analysis logic
│
├── frontend
│   └── index.html       # Simple UI
│
├── requirements.txt
└── README.md

# Technologies Used

Backend:
    Python
    FastAPI
    Pydantic

Frontend:
    HTML
    CSS
    JavaScript

Python standard libraries used:
    re 
    collections

# Running the Project
1. Clone the repository
    git clone https://github.com/SvetaKozyreva/text-analyzer.git
    cd text-analyzer
2. Install dependencies
    pip install -r requirements.txt
3. Start the server
    uvicorn backend.main:app --reload

The server will run at: http://127.0.0.1:8000

Swagger API documentation: http://127.0.0.1:8000/docs

4. Run the frontend
    Open the file: frontend/index.html 
    in a browser.
    
Enter text and click Analyze. The page will send a request to the API and display the results.

# API Endpoint
POST /analyze

**Request**
{
  "text": "The quick brown fox jumps over the lazy dog. The dog barked, but the fox kept running! Fox and dog... they're actually friends. The fox visits the dog every day, and the dog always welcomes the fox. It's a beautiful friendship. Don't you love stories about animals? Animals bring joy and happiness. The fox and the dog are proof that friendship has no boundaries!"
}
**Response**
{
  "word_count": 64,
  "char_count_with_spaces": 363,
  "char_count_without_spaces": 300,
  "sentence_count": 9,
  "top_words": [
    {
      "word": "fox",
      "count": 6
    },
    {
      "word": "dog",
      "count": 6
    },
    {
      "word": "friendship",
      "count": 2
    },
    {
      "word": "animals",
      "count": 2
    },
    {
      "word": "quick",
      "count": 1
    }
  ]
}

# Edge Cases
The app handles the following cases:
    Empty text → returns zeros and an empty top_words list.
    Single-word text → word_count = 1, sentence_count = 1.
    Text with line breaks (\n) → handled correctly.
    Invalid JSON or missing text field → FastAPI returns a validation error.

# Unit Tests
Run tests:
    $env:PYTHONPATH = "$PWD"
    pytest

Tests check:
  Word count
  Sentence count
  Stop words filtering

# Answers to Questions
1. What would you improve with more time?
    Add more unit tests for different edge cases
    Improve the user interface
    Implement more detailed error handling
    Optimize processing for large texts

2. What problems could arise when processing a 1,000,000-character text? How to handle them?
    Memory usage: Large text and intermediate lists can use a lot of memory
    Performance: Inefficient algorithms can be slow
    Request size limits: Some servers limit HTTP request size

3. How would you scale the application to handle 1,000 concurrent users?
    Run multiple worker processes
    Use a production server
    Load balance multiple backend instances
    Cache frequently analyzed texts

> `I confirm that I completed this task independently.`
