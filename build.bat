@echo off
REM Build script for Netlify deployment on Windows

REM Install Python dependencies
pip install -r requirements.txt

REM Download required NLTK data
python -m nltk.downloader stopwords punkt

REM Install Streamlit
pip install streamlit

echo Build completed successfully!