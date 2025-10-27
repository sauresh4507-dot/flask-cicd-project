from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>DevOps CI/CD Project</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                .container {
                    text-align: center;
                    padding: 40px;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 10px;
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                }
                h1 { font-size: 3em; margin: 0; }
                p { font-size: 1.2em; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 CI/CD Pipeline Success!</h1>
                <p>Flask app deployed via GitHub Actions & Docker</p>
                <p>Version: 1.0</p>
            </div>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'version': '1.0'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)