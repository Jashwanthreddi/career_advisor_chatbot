import google.generativeai as genai

from config import GEMINI_API_KEY
from prompts import SYSTEM_PROMPT
from logger import logger

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def get_response(
    user_input,
    conversation_history
):

    try:

        recent_history = conversation_history[-5:]

        prompt = f"""
        {SYSTEM_PROMPT}

        Previous Conversation:

        {recent_history}

        User Question:

        {user_input}
        """

        response = model.generate_content(
            prompt
        )

        logger.info(
            f"User Question: {user_input}"
        )

        logger.info(
            "Response generated successfully."
        )

        return response.text

    except Exception as e:

        logger.error(
            f"Error: {str(e)}"
        )

        return """
Sorry, I am unable to process your request right now.

Please try again later.
"""