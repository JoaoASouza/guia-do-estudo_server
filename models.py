from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Events(Base):
    __tablename__ = 'events'
    name = Column(String(50), primary_key=True)
    date = Column(String(15))

    def __repr__(self):
        return '<Evento {}>'.format(self.name)
    
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Subjects(Base):
    __tablename__ = 'subjects'
    name = Column(String(50), primary_key=True)
    period = Column(Integer)
    professor = Column(String(100))
    credits = Column(Integer)
    workload = Column(Integer)
    url = Column(String(300))

    def __repr__(self):
        return '<Subject {}>'.format(self.name)
    
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()