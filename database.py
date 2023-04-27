from application import db,app
app.app_context().push()
db.create_all()
# from application.users.models import User
# user = User(username='c', email='c@example.com', password='foobar')
# db.session.add(user)
# db.session.commit()
