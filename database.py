from application import db,app
app.app_context().push()
db.create_all()
# from application.users.models import User
# user = User(username='cosssdsd', email='rororor@example.com', password='foobar', phone_number= '973-990-8888', homePage_number=None)
# db.session.add(user)
# db.session.commit()



