from flask import g, jsonify
from flask import request

from app import db
from app.api_1_0 import api
from app.models import Post


@api.route('/posts/', methods=['POST'])
def new_post():
    post = Post.from_json(request.json)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json())
