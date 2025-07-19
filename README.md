 # 🔍 AI Resume Analyzer

An intelligent resume analysis tool built with Streamlit and Ollama that provides comprehensive feedback on resumes using local AI models. Analyze your resume for ATS compatibility, skill gaps, and get personalized improvement suggestions - all while keeping your data completely private.

## ✨ Features

- 📄 **PDF Resume Upload** - Extract and analyze text from PDF resumes
- 🎯 **Job Description Matching** - Compare your resume against specific job postings
- 🤖 **Local AI Analysis** - Uses Ollama for private, offline AI processing
- 📊 **Comprehensive Feedback** - Get insights on skills, experience, and ATS optimization
- 🔒 **Privacy-First** - All processing happens locally, no data sent to external servers
- 💾 **Export Results** - Download analysis reports as text files
- 🎨 **User-Friendly Interface** - Clean, modern web interface built with Streamlit

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Ollama (llama3.2:1b)
- **PDF Processing**: PyPDF2
- **Language**: Python 3.8+

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- Ollama installed on your system
- At least 4GB RAM (for the AI model)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Hajer45/ai-resume-analyzer
cd ai-resume-analyzer
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

#### Windows/macOS:
1. Download Ollama from [https://ollama.ai/download](https://ollama.ai/download)
2. Run the installer

#### Linux:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### 5. Download AI Model

```bash
# Pull the required model (this may take a few minutes)
ollama pull llama3.2:1b
```

### 6. Verify Installation

```bash
# Check if model is installed
ollama list

# Test the model
ollama run llama3.2:1b
# Type a test message and /bye to exit
```

## 🎯 Usage

### 1. Start the Application

```bash
# Make sure your virtual environment is activated
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### 2. Using the Resume Analyzer

1. **Upload Resume**: Click "Choose your resume (PDF)" and select your PDF file
2. **Add Job Description** (Optional): Paste a job posting for targeted analysis
3. **Analyze**: Click "🔍 Analyze Resume" button
4. **Review Results**: Get detailed feedback on your resume
5. **Download Report**: Save the analysis as a text file

## 📁 Project Structure

```
ai-resume-analyzer/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
└── .venv/                # Virtual environment (not tracked)
```

## 🔧 Configuration

The application uses the `llama3.2:1b` model by default. To use a different model:

1. Pull the desired model: `ollama pull model-name`
2. Update the model name in `app.py`:
   ```python
   response = ollama.chat(
       model='your-model-name',  # Change this line
       messages=[{'role': 'user', 'content': prompt}]
   )
   ```

## 📊 Analysis Features

The AI provides feedback on:

- **Skills Analysis** - Identifies key technical and soft skills
- **Experience Evaluation** - Assesses relevant work experience
- **ATS Compatibility** - Tips for passing Applicant Tracking Systems
- **Job Match Scoring** - How well your resume matches job requirements
- **Improvement Suggestions** - Specific recommendations for enhancement
- **Professional Formatting** - Layout and presentation feedback

## 🚧 Troubleshooting

### Common Issues

**PDF Text Extraction Issues:**
- Ensure your PDF contains selectable text (not scanned images)
- Try saving your resume as a new PDF from a word processor
- Check if text can be selected/copied in your PDF viewer

**Ollama Connection Issues:**
- Make sure Ollama service is running
- Verify the model is installed: `ollama list`
- Try restarting Ollama service

**Performance Issues:**
- The 1B model is optimized for speed, but analysis may take 30-60 seconds
- Ensure you have sufficient RAM available
- Close other resource-intensive applications

## 🛡️ Privacy & Security

This application is designed with privacy in mind:
- All processing happens locally on your machine
- No resume data is sent to external servers
- AI model runs offline through Ollama
- No data is stored permanently (unless you choose to download results)

## 🚀 Future Enhancements

Planned features for future versions:
- [ ] Support for DOCX files
- [ ] OCR support for scanned PDFs
- [ ] Multiple resume comparison
- [ ] Industry-specific analysis
- [ ] Skills gap visualization
- [ ] Resume template suggestions
- [ ] Batch processing multiple resumes

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Your Name**
- LinkedIn: [Hajer Talbi](https://www.linkedin.com/in/hajer-talbi/)
- Email: hagartalbi@gmail.com

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for providing local AI model capabilities
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [PyPDF2](https://pypdf2.readthedocs.io/) for PDF processing
- Meta for the Llama model family

## ⭐ Support

If you found this project helpful, please consider giving it a star on GitHub!

---

**Built with ❤️  Hajer Talbi**
