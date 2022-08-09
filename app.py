"""This is the main file called to run the flask application"""
from dotenv import load_dotenv  # load the environment variables that we set in our .env file
from flask import flash, render_template
from root.factory import create_app

if __name__ == "__main__":
    load_dotenv()
    # load the environment variables that we set in our .env file.
    app = create_app()
    app.run()
