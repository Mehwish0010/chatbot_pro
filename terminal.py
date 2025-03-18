import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Chat loop
while True:
    user_input = input("\nEnter your question (or type 'exit' to quit): ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break

    # Generate response
    response = model.generate_content(user_input)

    # Print the response
    print("\nGemini's Response:")
    print(response.text)



