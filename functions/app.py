import os
import sys
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handler(event, context):
    """
    Netlify function handler that serves the Streamlit app
    """
    try:
        # Log the event for debugging
        logger.info(f"Received event: {event}")
        
        # For now, return a simple response with instructions
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS"
            },
            "body": """
            <!DOCTYPE html>
            <html>
            <head>
                <title>SpamGuard Pro</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                        line-height: 1.6;
                        color: #333;
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                        background-color: #f8f9fa;
                    }
                    .container {
                        background: white;
                        border-radius: 10px;
                        padding: 30px;
                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        margin-top: 30px;
                        text-align: center;
                    }
                    h1 {
                        color: #2c3e50;
                        margin-bottom: 10px;
                    }
                    .logo {
                        font-size: 3em;
                        margin-bottom: 20px;
                    }
                    .instructions {
                        background: #e3f2fd;
                        padding: 20px;
                        border-radius: 8px;
                        margin: 25px 0;
                        text-align: left;
                    }
                    code {
                        background: #f1f3f4;
                        padding: 2px 6px;
                        border-radius: 4px;
                        font-family: 'Courier New', monospace;
                    }
                    .footer {
                        text-align: center;
                        margin-top: 30px;
                        color: #7f8c8d;
                        font-size: 0.9em;
                    }
                    a {
                        color: #3498db;
                        text-decoration: none;
                        font-weight: 500;
                    }
                    a:hover {
                        text-decoration: underline;
                    }
                </style>
            </head>
            <body>
                <div class="logo">🛡️</div>
                <h1>SpamGuard Pro</h1>
                <p style="text-align: center; color: #7f8c8d; font-size: 1.1em;">
                    Advanced AI-powered spam detection for emails and SMS messages
                </p>
                
                <div class="container">
                    <h2>🚀 Access the Application</h2>
                    
                    <div class="instructions">
                        <h3>Local Development:</h3>
                        <ol>
                            <li>Clone the repository: <code>git clone https://github.com/RaviShekharrepo/Email-SMS-Spam-Classifier.git</code></li>
                            <li>Navigate to the project directory: <code>cd Email-SMS-Spam-Classifier</code></li>
                            <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
                            <li>Run the application: <code>streamlit run app.py</code></li>
                        </ol>
                        
                        <h3>Deployment:</h3>
                        <p>This application is configured for deployment on Netlify. For the best experience with Streamlit applications, we recommend:</p>
                        <ul>
                            <li>Deploying on platforms like Heroku, Streamlit Sharing, or Render</li>
                            <li>Using Docker for containerized deployment</li>
                        </ul>
                    </div>
                    
                    <p>
                        <a href="https://github.com/RaviShekharrepo/Email-SMS-Spam-Classifier" target="_blank">
                            View Source Code on GitHub
                        </a>
                    </p>
                </div>
                
                <div class="footer">
                    <p>Built with ❤️ using Python, Streamlit, NLTK, and Scikit-learn</p>
                    <p>© 2025 SpamGuard Pro - All rights reserved</p>
                </div>
            </body>
            </html>
            """
        }
    except Exception as e:
        logger.error(f"Error in handler: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Internal server error: {str(e)}"
        }