# AI-Powered Study Buddy

## Description

An AI-powered study buddy that uses OpenAI's GPT model to answer questions across a wide range of subjects. This tool can help students learn and understand various topics by asking questions and getting real-time, AI-generated responses.

## Features

- Ask questions on any topic and get answers.
- Easy setup and usage.
- Utilizes OpenAI’s GPT model to generate answers.

## Prerequisites

Before running the project, make sure you have:

- Python 3.x installed.
- A virtual environment tool (like `venv`).
- OpenAI API Key (sign up at [OpenAI](https://platform.openai.com/) if you don't have one).

## Installation

Follow these steps to set up the project:

### 1. Clone the Repository

```
git clone https://github.com/your-username/ai-study-buddy.git
cd ai-study-buddy
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment:

```
python3 -m venv venv
```
On macOS/Linux:
```
source venv/bin/activate
```
On Windows:
```
venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages:

```
pip install -r requirements.txt
```
If you don’t have a requirements.txt file yet, you can generate it by running:

```
pip freeze > requirements.txt
```

### 4. Set Up Your OpenAI API Key
Create a .env file in the root of your project and add the following:

OPENAI_API_KEY=your-api-key-here

Replace your-api-key-here with your actual OpenAI API key. If you don’t have an API key, you can get one from OpenAI’s platform.


### 5. Run the Project
Now you’re ready to use the AI-powered study buddy!

```
python study_buddy.py
```

### 6. Example Interaction  

Ask me anything: What is an atom?
AI Study Buddy: An atom is the smallest unit of ordinary matter that forms a chemical element. It consists of a nucleus containing protons and neutrons, surrounded by electrons.
