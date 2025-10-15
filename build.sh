#!/bin/bash
# Build script for Netlify deployment

# Install Python dependencies
pip install -r requirements.txt

# Download required NLTK data
python -m nltk.downloader stopwords punkt

# Install Streamlit
pip install streamlit

echo "Build completed successfully!"