import os

from app import create_app

app = create_app()
app.config.from_object(os.environ.get("FLASK_CONFIG"))


if __name__ == '__main__':
    app.run()