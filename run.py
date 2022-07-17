from app import create_app
from app.config import DEBUG

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8005, debug=DEBUG)