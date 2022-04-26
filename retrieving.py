from main import User,Session,engine

local_session = Session(bind=engine)

users = local_session.query(User).all()

for user in users:
    print(user.username)
    
# filtering

result = local_session.query(User).filter(User.username=='saji').first()

print(result)