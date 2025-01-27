from website import create_app
import os

app = create_app()


@app.route('/')
def home():
    return "Hello, Railway!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
