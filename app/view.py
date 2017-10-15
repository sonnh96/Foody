from app import my_app
from flask import render_template
from app.forms import EventSearch
from app.ticket_scraper import get_posts

@my_app.route('/')
@my_app.route('/index')

def index():
	return render_template('index.html')

@my_app.route('/search', methods=['GET', 'POST'])
def search():
	posts = []
	form = EventSearch()
	if form.validate_on_submit():
		event = form.event_name.data
		location = form.location.data
		position = form.position.data
		posts = get_posts(event, position, location)
	return render_template('search.html', title='Search for a food', form=form, posts=posts)