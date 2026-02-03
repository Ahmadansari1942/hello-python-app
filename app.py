from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Hello Python App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                h1 { font-size: 48px; margin-bottom: 20px; }
                p { font-size: 20px; }
                .container {
                    background: rgba(255,255,255,0.1);
                    padding: 40px;
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎉 Hello World from Python!</h1>
                <p>Welcome to Flask App on EC2</p>
                <p>✅ App is running on Gunicorn + Nginx</p>
            </div>
        </body>
    </html>
    '''

@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This is a simple Flask application deployed on AWS EC2!</p>'

@app.route('/api/hello')
def api_hello():
    return {'message': 'Hello from Flask API!', 'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


