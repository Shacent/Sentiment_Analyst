# Sentiment Analysis API

![Python](https://img.shields.io/badge/python-3.12.2-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.17.0-orange)
![Keras](https://img.shields.io/badge/Keras-3.3.3-red)
![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Overview

This is a simple Sentiment Analysis API built with Flask, TensorFlow, and Keras. The API allows users to send a sentence via a POST request and returns the predicted sentiment (either **positive** or **negative**). The prediction model is based on a neural network trained on text data.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the API](#running-the-api)
- [API Usage](#api-usage)
  - [Request Format](#request-format)
  - [Response Format](#response-format)
- [Example](#example)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12.2 or higher
- Flask 3.0.3 or higher
- TensorFlow 2.17.0 or higher
- Keras 3.3.3 or higher
- A trained sentiment analysis model (`Sentiment_Model.h5`)
- A tokenizer (`tokenizer.pkl`)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-api.git
   cd sentiment-analysis-api

2. **Create a Virtual Environment**
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**
   ```bash
   conda env create -f requirements.yaml

4. **Add Model and Tokenizer**
   
   Place your trained Sentiment_Model.h5 and tokenizer.pkl files in the project root directory.

### Running the API

To start the Flask server, run:
  ```bash
  python app.py
  ```
The API will be accessible at http://127.0.0.1:5000.

## API Usage

### Request Format

- URL: /predict
- Method: POST
- Content-Type: application/json
- Body:
```json
{
    "sentence": "Your sentence here"
}
```

### Response Format
- Content-Type: application/json
- Body:
```json
{
    "sentence": "Your sentence here",
    "sentiment": "positive"  // or "negative"
}
```
## Example

### cURL Example
```python
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"sentence": "I love this product!"}'
```
### Python Example
```python
import requests

url = "http://127.0.0.1:5000/predict"
data = {"sentence": "I love this product!"}
response = requests.post(url, json=data)
print(response.json())
```
#### Sample Output
```json
{
    "sentence": "We Must Suport Mr Anies To Become President !",
    "sentiment": "positive"
}
```
