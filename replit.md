# Gemini AI Text Assistant Telegram Bot

## Overview

This project is a Telegram bot that provides AI-powered text conversation capabilities using Google's Gemini AI. The bot processes text messages and generates intelligent responses, offering a streamlined text-only chat experience without voice processing complexity.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a modular architecture with clear separation of concerns:

- **Bot Layer**: Handles Telegram interactions and message routing
- **Voice Processing Layer**: Manages speech-to-text and text-to-speech conversions
- **AI Integration Layer**: Interfaces with Google Gemini AI for response generation
- **Configuration Layer**: Manages environment variables and bot initialization

## Key Components

### 1. TextAssistantBot (bot.py)
- **Purpose**: Main bot orchestrator that handles Telegram text message events
- **Responsibilities**: Message routing, command handling, text-based user interaction management
- **Architecture Decision**: Uses python-telegram-bot library for robust Telegram API integration
- **Rationale**: Provides async support and comprehensive message handling capabilities with simplified text-only processing

### 2. GeminiClient (gemini_client.py)
- **Purpose**: Interface with Google's Gemini AI
- **Responsibilities**: Generate intelligent responses based on user input
- **Architecture Decision**: Uses Google's official genai library with Gemini 2.5 Flash model
- **Rationale**: Latest model provides best performance and capabilities for conversational AI

### 4. Main Application (main.py)
- **Purpose**: Entry point and configuration management
- **Responsibilities**: Environment setup, logging configuration, bot initialization
- **Architecture Decision**: Uses python-dotenv for environment variable management
- **Rationale**: Separates configuration from code for better security and deployment flexibility

## Data Flow

1. **Text Message Flow**:
   - User sends text message to Telegram bot
   - Text is directly sent to GeminiClient for processing
   - AI response is sent back as text to user

## External Dependencies

### Core Libraries
- **python-telegram-bot**: Telegram Bot API integration
- **google-genai**: Official Google Gemini AI client
- **python-dotenv**: Environment variable management

### Cloud Services
- **Telegram Bot API**: Message delivery and user interaction
- **Google Gemini AI**: Natural language processing and response generation

## Deployment Strategy

### Environment Configuration
- **Required Environment Variables**:
  - `TELEGRAM_BOT_TOKEN`: Bot authentication token from BotFather
  - `GEMINI_API_KEY`: Google AI API key for Gemini access

### Runtime Requirements
- Python 3.7+ with async support
- Internet connectivity for external API calls

### Deployment Options
- **Development**: Local execution with environment file
- **Production**: Cloud deployment (Heroku, Railway, etc.) with environment variables
- **Containerization**: Docker deployment with proper audio dependencies

### Scalability Considerations
- Stateless design allows horizontal scaling
- API rate limiting may need queuing mechanism for high usage

### Security Measures
- API keys stored as environment variables
- No persistent storage of user data