from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///test.db", echo=True)


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    qty = Column(Integer)

#
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    age = Column(Integer)

class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    playername = Column(String)



from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
var = sessionmaker(bind=engine)
session = var()


# for ele in session.query(Book):
#     print(ele.name)


#
# b1 = Book(name="book2", qty=100)
# session.add(b1)
#
# session.commit()

# user1 = User(id=1, username="devesh", age=21)
# user2 = User(id=2, username="jahan", age=20)
#
# session.add(user1)
# session.add(user2)
# session.commit()
#
# for res in session.query(User).all():
#     print(res.username)

# p1 = Player(id=3,playername="player3")
# session.add(p1)
# session.commit()

class AfterPlayer(Base):
    __tablename__ = "AfterPlayer"
    id = Column(Integer, primary_key=True)
#
# for res in session.query(Player).all():
#     print(res.playername)

class tabletocheckfilename(Base):
    __tablename__ = "table1"
    id = Column(Integer, primary_key=True)
    name = Column(String)