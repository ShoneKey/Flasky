from datetime import datetime
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask import current_app

from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_mail


@main.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['know'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_mail(current_app.config['FLASKY_ADMIN'], 'new user', 'mail/new_user', user=user)
        else:
            session['know'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           know=session.get('know', False),
                           current_time=datetime.utcnow())


@main.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)
