from flask import Blueprint, render_template, url_for, redirect, current_app, flash
from flask_login import login_required, current_user
from sqlalchemy import exc

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from .models import Snap
from application import db

snaps = Blueprint('snaps', __name__, template_folder='templates')


class SnapForm(FlaskForm):
    """Form for creating new snaps."""

    name = StringField('name', validators=[DataRequired()])
    extension = StringField('extension', validators=[DataRequired()])
    content = StringField('content', widget=TextArea(),
            validators=[DataRequired()])


@snaps.route('/', methods=['GET'])
def listing():
    """
    List all snaps; most recent first.

    """
    snaps = Snap.query.order_by(Snap.created_on.desc()).limit(20).all()
    return render_template('snaps/index.html', snaps=snaps)


@snaps.route('/add', methods=['GET', 'POST'])
# @login_required
def add():
    """Add a new snap."""
    
    if not current_user.is_authenticated:
        flash("login in first to use, redirected to login")
        return redirect(url_for('users.login'))

    form = SnapForm()

    if form.validate_on_submit():
        user_id = current_user.id

        snap = Snap(user_id=user_id, name=form.name.data,
                content=form.content.data, extension=form.extension.data)
        db.session.add(snap)

        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            current_app.exception("Could not save new snap!")
            flash("Something went wrong while posting your snap!")
    else:
        return render_template('snaps/add.html', form=form)

    return redirect(url_for('snaps.listing'))
