import json

def handler(event, context):
    """
    Netlify function that explains why Streamlit apps can't run directly on Netlify
    and provides alternative deployment options.
    """
    response_body = {
        "message": "Streamlit Application Information",
        "description": "This is a Streamlit application that cannot run directly on Netlify's serverless functions.",
        "reason": "Streamlit applications require a persistent server process and WebSocket connections which are not supported in Netlify's serverless function environment.",
        "recommended_solutions": [
            {
                "platform": "Streamlit Sharing",
                "url": "https://share.streamlit.io",
                "description": "The official and easiest way to deploy Streamlit applications"
            },
            {
                "platform": "Heroku",
                "description": "Supports Python web applications with proper server configurations"
            },
            {
                "platform": "Docker",
                "description": "Containerized deployment option using the provided Dockerfile"
            }
        ],
        "local_development": {
            "steps": [
                "Clone the repository",
                "Install dependencies with pip install -r requirements.txt",
                "Download NLTK data with python -m nltk.downloader stopwords punkt",
                "Run with streamlit run app.py"
            ]
        }
    }
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS"
        },
        "body": json.dumps(response_body)
    }