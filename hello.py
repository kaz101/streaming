from flask import Flask
import main
from random import randint

app = Flask(__name__)

@app.route("/")
def hello_world():
    show_details = main.start()
    episode = show_details[randint(0, len(show_details)-1)]
    return f'<p>{episode[0]}  {episode[1]}</p><iframe src={episode[2]} title={episode[1]} allowfullscreen="true" frameborder="o" marginheight="0" marginwidth="0" width="100%" height="100%" scrolling="auto" allow="autoplay"></iframe>'