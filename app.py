from flask import Flask
from werkzeug.exceptions import HTTPException
from api.views import api_blueprint
from main.views import main_page_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_page_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    return f" Error code: {response.status_code}"


if __name__ == "__main__":
    app.run()

