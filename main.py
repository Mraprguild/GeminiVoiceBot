#!/usr/bin/env python3
"""
Main entry point for the Gemini AI Text Assistant Telegram Bot.
"""

import logging
import os
from dotenv import load_dotenv
from bot import TextAssistantBot

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Main function to start the bot."""
    try:
        # Get required environment variables
        telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        
        if not telegram_token:
            raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")
        
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        # Initialize and start the bot
        bot = TextAssistantBot(telegram_token)
        logger.info("Starting Gemini AI Text Bot...")
        bot.run()
        
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise

if __name__ == "__main__":
    main()
