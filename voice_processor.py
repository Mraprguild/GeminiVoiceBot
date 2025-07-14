"""
Voice processing module for speech-to-text and text-to-speech conversion.
"""

import asyncio
import logging
import os
import tempfile
from typing import Optional

import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS

logger = logging.getLogger(__name__)

class VoiceProcessor:
    """Handles voice message processing including STT and TTS."""
    
    def __init__(self):
        """Initialize the voice processor."""
        self.recognizer = sr.Recognizer()
        # Adjust for ambient noise
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
    
    async def voice_to_text(self, voice_file_path: str) -> Optional[str]:
        """
        Convert voice message to text.
        
        Args:
            voice_file_path: Path to the voice file
            
        Returns:
            Transcribed text or None if failed
        """
        try:
            # Convert to WAV format for speech recognition
            wav_path = await self._convert_to_wav(voice_file_path)
            
            if not wav_path:
                logger.error("Failed to convert voice file to WAV format")
                return None
            
            try:
                # Perform speech recognition
                with sr.AudioFile(wav_path) as source:
                    # Adjust for ambient noise
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    
                    # Record the audio
                    audio_data = self.recognizer.record(source)
                
                # Recognize speech using Google's service
                text = self.recognizer.recognize_google(audio_data)
                logger.info(f"Successfully transcribed voice to text: {text}")
                return text
                
            finally:
                # Clean up WAV file
                if os.path.exists(wav_path):
                    os.unlink(wav_path)
        
        except sr.UnknownValueError:
            logger.warning("Could not understand the audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Speech recognition service error: {e}")
            return None
        except Exception as e:
            logger.error(f"Error in voice to text conversion: {e}")
            return None
    
    async def _convert_to_wav(self, input_path: str) -> Optional[str]:
        """
        Convert audio file to WAV format.
        
        Args:
            input_path: Path to input audio file
            
        Returns:
            Path to converted WAV file or None if failed
        """
        try:
            # Load audio file
            audio = AudioSegment.from_file(input_path)
            
            # Create temporary WAV file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
                wav_path = temp_wav.name
            
            # Export as WAV
            audio.export(wav_path, format="wav")
            logger.info(f"Successfully converted audio to WAV: {wav_path}")
            return wav_path
            
        except Exception as e:
            logger.error(f"Error converting audio to WAV: {e}")
            return None
    
    async def text_to_voice(self, text: str, language: str = "en") -> Optional[str]:
        """
        Convert text to voice using Google Text-to-Speech.
        
        Args:
            text: Text to convert to speech
            language: Language code (default: "en")
            
        Returns:
            Path to generated voice file or None if failed
        """
        try:
            # Create TTS object
            tts = gTTS(text=text, lang=language, slow=False)
            
            # Create temporary file for the voice
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_voice:
                voice_path = temp_voice.name
            
            # Save the voice file
            tts.save(voice_path)
            logger.info(f"Successfully generated voice file: {voice_path}")
            return voice_path
            
        except Exception as e:
            logger.error(f"Error in text to voice conversion: {e}")
            return None
    
    def cleanup_file(self, file_path: str):
        """
        Clean up temporary files.
        
        Args:
            file_path: Path to file to delete
        """
        try:
            if os.path.exists(file_path):
                os.unlink(file_path)
                logger.info(f"Cleaned up file: {file_path}")
        except Exception as e:
            logger.warning(f"Failed to clean up file {file_path}: {e}")
