from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqlconnector://root:rootroot@localhost:3306", echo=True)

Base = declarative_base()

class Flashcard(Base):
	__tablename__ = 'flashcards'
	__table_args__ = {'schema': 'onespace'}

	id = Column(Integer, primary_key=True)
	category = Column(String(length=45))
	front = Column(String(length=255))
	back = Column(String(length=255))

	def __repr__(self):
		return "<Project(front'{0}', back='{1}')>".format(self.front, self.back)

Base.metadata.create_all(engine)

session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()
flashcard = Flashcard(category='ccc', front='fff', back='bbb')
session.add(flashcard)
session.commit()
# theProject = session.query(Flashcard).filter_by(category='ccc').first()
theProject = session.query(Flashcard).filter_by(category='ccc').all()
print(theProject)