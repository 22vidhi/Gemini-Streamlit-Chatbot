from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Testing gemini-flash-latest model...")
try:
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents="Say hello in one sentence"
    )
    print("✅ SUCCESS!")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ ERROR: {e}")
