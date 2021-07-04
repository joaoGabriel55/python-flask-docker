from flask import Flask
from src.database import db_session
from src.models import UserModel
from flask_redis import FlaskRedis

app = Flask(__name__)

app.config["REDIS_URL"] = "redis://redis:6379/0"

redis_client = FlaskRedis(app)
redis_client.init_app(app)


def test_database():
    has_row = bool(UserModel.query.filter(UserModel.name == "john").first())
    return has_row


def test_redis():
    redis_client.set("test", "hello")
    key = redis_client.get("test").decode("UTF-8")
    redis_client.delete("test")

    if key == "hello":
        return True
    else:
        return False


def test_rabbitmq():
    return False


@app.route("/health_check")
def health_check():
    return {
        "redis": test_redis(),
        "postgres": test_database(),
        "rabbit-mq": test_rabbitmq()
    }


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
