from flask import Flask, request,render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'not-secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def initialize():
    """ Page that gets the words needed from User"""

    prompts = story.prompts
    return render_template("initial_page.html", prompts = prompts)



@app.route('/story')
def tale():
    """ Story is presented with the chosen words."""
 
    text = story.generate(request.args)
    return render_template ('story_page.html', text = text)