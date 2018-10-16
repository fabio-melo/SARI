from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///users.db', echo=True)

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'
  def __init__(self, id_, details, role):
    
    self.id_ = Column('id',Integer, primary_key=True)
    self.details = details
    self.role = self._set_role(role)

  def _set_role(self, role):
    if role == 'admin': return 'admin'
    elif role == 'user': return 'user'


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()
for user in users:
  print(user.id_)