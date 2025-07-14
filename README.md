# **GeminiVoiceBot** 🎙️🤖  

A voice-enabled chatbot powered by **Google's Gemini AI**, allowing seamless voice interactions via terminal or supported platforms (Telegram/Discord/Slack).  

![Demo](demo.gif) *(Replace with actual demo GIF link)*  

## **Features** ✨  
✅ **Voice Recognition (STT)** – Speak, and the bot understands.  
✅ **Gemini AI Responses** – Smart, context-aware replies.  
✅ **Text-to-Speech (TTS)** – The bot speaks back to you.  
✅ **Multi-Platform Support** – Works on CLI, Telegram, Discord (configurable).  
✅ **Easy Setup** – Simple installation with `pip`.  

---

## **Installation** ⚙️  

### **Prerequisites**  
- Python 3.8+  
- Google Gemini API Key ([Get it here](https://ai.google.dev/))  
- FFmpeg (for voice processing, [install guide](https://ffmpeg.org/))  

### **Steps**  
1. **Clone the repository:**  
   ```sh
   git clone https://github.com/Mraprguild/GeminiVoiceBot.git
   cd GeminiVoiceBot
   ```

2. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your API key:**  
   Rename `.env.example` to `.env` and add your Gemini API key:  
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the bot:**  
   ```sh
   python main.py
   ```

---

## **Usage** 🚀  

### **1. Terminal Mode**  
Run in voice mode:  
```sh
python main.py --voice
```
- Speak when prompted, and the bot will respond via text & voice.  

### **2. Telegram Bot Mode** *(Optional)*  
1. Get a Telegram Bot Token from [@BotFather](https://t.me/BotFather).  
2. Add it to `.env`:  
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   ```
3. Run:  
   ```sh
   python telegram_bot.py
   ```

---

## **Configuration** ⚙️  

Edit `config.json` to customize:  
```json
{
  "voice_enabled": true,
  "tts_engine": "gTTS",  // or "pyttsx3"
  "language": "en",
  "max_response_length": 200
}
```

---

## **Dependencies** 📦  
- `google-generativeai` (Gemini AI)  
- `speech_recognition` (Voice input)  
- `gTTS` or `pyttsx3` (Text-to-speech)  
- `python-dotenv` (Environment variables)  

Full list in [`requirements.txt`](requirements.txt).  

---

## **Contributing** 🤝  
Feel free to open **issues** or **PRs**!  
1. Fork the repo.  
2. Create a branch (`git checkout -b feature/awesome-feature`).  
3. Commit changes (`git commit -m "Add feature"`).  
4. Push (`git push origin feature/awesome-feature`).  
5. Open a **Pull Request**.  

---

## **License** 📜  
MIT License. See [LICENSE](LICENSE).  

---

## **Support** 💬  
For help, open an **issue** or contact:  
📧 Email: *your-email@example.com*  
💬 Telegram: *@yourusername*  

---

**Enjoy the bot? Give it a ⭐ on GitHub!** 🎉  

---  

### **Demo**  
![Terminal Demo](terminal_demo.png) *(Replace with an actual screenshot)*  

*(Adjust this template based on your actual project structure.)* 🛠️
