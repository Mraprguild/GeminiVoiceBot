"""
Telegram Bot implementation for the Gemini AI Text Assistant.
"""

import logging
from typing import Optional

from telegram import Update
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    ContextTypes,
    filters
)

from gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class TextAssistantBot:
    """Main bot class that handles Telegram text interactions."""
    
    def __init__(self, token: str):
        """Initialize the bot with the given token."""
        self.token = token
        self.gemini_client = GeminiClient()
        self.application = Application.builder().token(token).build()
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Set up message and command handlers."""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        
        # Message handlers
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text_message))
        self.application.add_handler(MessageHandler(~filters.TEXT, self.handle_unsupported_message))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /start command."""
        welcome_message = (
            "🤖 Welcome to Gemini AI Text Bot!\n\n"
            "I can help you with:\n"
            "• Ask me questions and get AI-powered responses\n"
            "• Have conversations about any topic\n"
            "• Get help with various tasks\n"
            "• Use /help for more information\n\n"
            "Just send me a text message to get started!"
        )
        await update.message.reply_text(welcome_message)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /help command."""
        help_message = (
            "🤖 Gemini AI Text Bot Help\n\n"
            "Commands:\n"
            "• /start - Start the bot and see welcome message\n"
            "• /help - Show this help message\n\n"
            "How to use:\n"
            "• Send text messages - I'll respond with AI-generated answers\n"
            "• Ask questions about any topic\n"
            "• Have conversations or get help with tasks\n\n"
            "Features:\n"
            "• Powered by Google's Gemini AI\n"
            "• Intelligent conversational responses\n"
            "• Multi-language support\n\n"
            "Just type your message and I'll respond!"
        )
        await update.message.reply_text(help_message)
    

    
    async def handle_text_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming text messages."""
        try:
            # Send typing indicator
            await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
            
            user_text = update.message.text
            logger.info(f"Received text message: {user_text}")
            
            # Get AI response
            ai_response = await self.gemini_client.get_response(user_text)
            
            if not ai_response:
                await update.message.reply_text("❌ Sorry, I couldn't generate a response. Please try again.")
                return
            
            # Send text response
            await update.message.reply_text(f"🤖 {ai_response}")
            
        except Exception as e:
            logger.error(f"Error processing text message: {e}")
            await update.message.reply_text("❌ Sorry, there was an error processing your message. Please try again.")
    
    async def handle_unsupported_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle unsupported message types."""
        await update.message.reply_text(
            "❌ Sorry, I only support text messages.\n"
            "Please send me a text message to get started!"
        )
    
    def run(self):
        """Start the bot."""
        logger.info("Bot is starting...")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)
