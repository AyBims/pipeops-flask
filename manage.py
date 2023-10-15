from flask import Flask
import os

app = Flask(__name__)


if __name__ == '__main__':
    app.run("0.0.0.0", port=os.getenv('PORT', 6969))