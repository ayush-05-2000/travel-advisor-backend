import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure API key is available
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key is missing! Set it in your .env file.")

client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Use the new client-based approach

def generate_itinerary(budget: int, num_people: int, places: list = None):
    """
    Generate an AI-based itinerary based on budget, number of people, and optional places.
    """
    prompt = f"""
    Generate a travel itinerary within a budget of ${budget} for {num_people} people.
    {f"Include these places: {', '.join(places)}." if places else ""}
    Provide a day-wise plan with estimated costs and activities.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating itinerary: {str(e)}"
