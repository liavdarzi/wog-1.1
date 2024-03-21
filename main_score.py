import utils,webbrowser,flask
from score import current_scores
import threading

app = flask.Flask(__name__)
@app.route('/')
def open_score_server():
    score = current_scores()
    return flask.render_template('score_server.html', SCORE=score)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)

#Open the site with the score, and the error site if there is a problem
def score_server():
    try:
        open_score_server()
    except:
        webbrowser.open("score_server_error.html")




