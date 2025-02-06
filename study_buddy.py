import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure your API key is set

def ask_study_buddy(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[{"role": "system", "content": "You are a helpful AI study buddy."},
                  {"role": "user", "content": question}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    question = input("Ask me anything: ")
    answer = ask_study_buddy(question)
    print("📘 Study Buddy:", answer)