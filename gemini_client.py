"""
Google Gemini AI client for generating intelligent responses.
"""

import logging
import os
from typing import Optional

from google import genai
from google.genai import types

logger = logging.getLogger(__name__)

class GeminiClient:
    """Client for interacting with Google's Gemini AI."""
    
    def __init__(self):
        """Initialize the Gemini client."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.5-flash"  # Using the newest Gemini model
        
        # System instruction for the voice assistant
        self.system_instruction = (
            "You are a helpful voice assistant. Provide clear, concise, and friendly responses. "
            "Keep your answers conversational and natural since they will be converted to speech. "
            "Avoid using special characters, markdown, or formatting that doesn't work well in speech. "
            "If asked about your capabilities, mention that you're a voice assistant powered by Gemini AI "
            "that can help with questions, conversations, and various tasks."
        )
    
    async def get_response(self, user_input: str) -> Optional[str]:
        """
        Get AI response from Gemini for user input.
        
        Args:
            user_input: User's message or question
            
        Returns:
            AI response text or None if failed
        """
        try:
            logger.info(f"Sending request to Gemini: {user_input}")
            
            # Generate response using Gemini
            response = self.client.models.generate_content(
                model=self.model,
                contents=[
                    types.Content(
                        role="user", 
                        parts=[types.Part(text=user_input)]
                    )
                ],
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction,
                    temperature=0.7,  # Balanced creativity and consistency
                    max_output_tokens=500,  # Reasonable length for voice responses
                )
            )
            
            if response.text:
                logger.info(f"Received response from Gemini: {response.text[:100]}...")
                return response.text.strip()
            else:
                logger.warning("Empty response received from Gemini")
                return None
                
        except Exception as e:
            logger.error(f"Error getting response from Gemini: {e}")
            return None
    
    async def get_conversation_response(self, conversation_history: list) -> Optional[str]:
        """
        Get AI response considering conversation history.
        
        Args:
            conversation_history: List of previous messages
            
        Returns:
            AI response text or None if failed
        """
        try:
            # Convert conversation history to Gemini format
            contents = []
            for message in conversation_history:
                role = "user" if message["role"] == "user" else "model"
                contents.append(
                    types.Content(
                        role=role,
                        parts=[types.Part(text=message["content"])]
                    )
                )
            
            # Generate response with conversation context
            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction,
                    temperature=0.7,
                    max_output_tokens=500,
                )
            )
            
            if response.text:
                return response.text.strip()
            else:
                return None
                
        except Exception as e:
            logger.error(f"Error getting conversation response from Gemini: {e}")
            return None
