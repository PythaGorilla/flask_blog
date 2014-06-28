from app.models import User, Post
from app import db
import datetime
p=Post.query.whoosh_search('hello').all()
for i in p:
	print i.author.email