from flask import Flask, render_template, request
from stories import story
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
# debug = DebugToolbarExtension(app)


@app.route('/')
def questions_form():
    """get promts from the story in stories.py"""
    prompts = story.prompts
    # render the html while allowing to use prompts 
    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def show_story():
    """show the  generated story with what is imputted into form"""
    # get the valoes of what is inputted with request.args
    text = story.generate(request.args)
    return render_template('story.html', text=text)