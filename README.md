# 🎯 AI Career Advisor Chatbot

A conversational AI-powered career guidance chatbot built with **Streamlit** and **Google's Gemini API**. Get personalized career advice, resume tips, interview preparation strategies, and skill development recommendations.

## ✨ Features

- 🤖 **AI-Powered Guidance**: Uses Google's Gemini 2.5 Flash model for intelligent responses
- 💬 **Conversational Interface**: Real-time chat with context-aware responses
- 📚 **Comprehensive Career Topics**:
  - Career guidance & planning
  - Resume review advice
  - Interview preparation
  - Skill development & certifications
  - Project recommendations
  - Career switching strategies
  - Higher education guidance
  - Domain-specific careers (Data Analytics, Software Engineering, AI/ML, Cloud Computing, etc.)

- 📝 **Chat History**: Maintains conversation context for better recommendations
- 🎨 **Clean UI**: Modern, user-friendly Streamlit interface
- 📊 **Structured Responses**: Organized, practical advice

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jashwanthreddi/career_advisor_chatbot.git
   cd career_advisor_chatbot
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
career_advisor_chatbot/
├── app.py              # Main Streamlit application
├── chatbot.py          # Gemini API integration & response logic
├── config.py           # Configuration & environment setup
├── logger.py           # Logging configuration
├── prompts.py          # System prompts & instructions
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not in repo)
├── .gitignore          # Git ignore rules
└── logs/               # Application logs
```

## 📋 Requirements

- `streamlit==1.58.0` - Web UI framework
- `google-generativeai==0.8.6` - Gemini API client
- `python-dotenv==1.2.2` - Environment variable management

Install all with:
```bash
pip install -r requirements.txt
```

## 💡 Usage

1. **Start the application**: `streamlit run app.py`
2. **Enter your career question** in the chat input
3. **Get AI-powered advice** with structured recommendations
4. **Continue the conversation** with follow-up questions

### Example Questions

- "I want to switch from finance to data science. What skills do I need?"
- "How should I prepare for a senior software engineer interview?"
- "Which certifications are most valuable for cloud computing careers?"
- "I'm a fresher. How do I build my first portfolio project?"
- "What's the best path to become an AI/ML engineer?"

## 🔐 Security

- API key is stored in `.env` file (not committed to git)
- `.gitignore` protects sensitive files
- Never share your API key

## 📝 Configuration

### Supported Career Areas

1. Career Guidance
2. Resume Review Advice
3. Interview Preparation
4. Skill Development
5. Certifications
6. Project Recommendations
7. Career Switching
8. Higher Education Guidance
9. Data Analytics Careers
10. Software Engineering Careers
11. AI and Machine Learning Careers
12. Full Stack Development Careers
13. Cloud Computing Careers
14. Cyber Security Careers

### Response Format

The chatbot provides structured responses including:
- Career Overview
- Required Skills
- Recommended Certifications
- Project Ideas
- Learning Path
- Interview Tips (when applicable)

## 🛠️ Development

### Project Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Model**: Google Gemini 2.5 Flash
- **Environment**: Python 3.14
- **Version Control**: Git & GitHub

### Logs

Application logs are stored in `logs/chatbot.log` with:
- Timestamp
- Log level (INFO, ERROR, WARNING)
- User queries
- API responses
- Error messages

## 🐛 Troubleshooting

### "ImportError: cannot import name 'GEMINI_API_KEY'"
- Ensure `.env` file exists with `GEMINI_API_KEY=your_key`
- API key should NOT have quotes

### "Connection refused"
- Streamlit server isn't running
- Run `streamlit run app.py` from project directory

### "Rate limit exceeded"
- Wait before making another API call
- Check Gemini API quota at [Google AI Studio](https://makersuite.google.com/)

## 📞 Support

For issues or questions:
1. Check the [Issues](https://github.com/Jashwanthreddi/career_advisor_chatbot/issues) page
2. Review the logs in `logs/chatbot.log`
3. Ensure API key is valid and has quota

## 🔄 Future Enhancements

- [ ] Save conversation history to database
- [ ] User profiles with personalized recommendations
- [ ] Resume upload and AI analysis
- [ ] Interview mock practice
- [ ] Salary & market insights
- [ ] Job recommendation engine
- [ ] Multi-language support

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Jashwanth Reddy**
- GitHub: [@Jashwanthreddi](https://github.com/Jashwanthreddi)

## 🙏 Acknowledgments

- [Google Gemini API](https://ai.google.dev/) for the AI model
- [Streamlit](https://streamlit.io/) for the web framework
- [python-dotenv](https://github.com/theskumar/python-dotenv) for environment management

---

**Built with ❤️ | Made with AI**
