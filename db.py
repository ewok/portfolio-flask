from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import DATABASE

engine = create_engine(DATABASE, pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=False,
    autoflush=False,
    bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Category1 = models.Category('Python/Django')

    db_session.add(Category1)
    db_session.commit()

    Project1 = models.Project('ewok.ru', 'My blog', 'photos/project_ru.png',
        'http://ewok.ru')

    Project1.category_id = Category1.id
    Skill1 = models.Skill('python', 70)
    Skill2 = models.Skill('django', 55)
    Skill3 = models.Skill('flask', 40)
    Info1 = models.Info('title', 'Portfolio - Arthur')
    Info2 = models.Info('about', "Arthur Taranchiev")

    Client = models.Client('Facebook','','clients/facebook.png','http://fb.com')

    db_session.add(Project1)
    db_session.add(Skill1)
    db_session.add(Skill2)
    db_session.add(Skill3)
    db_session.add(Info1)
    db_session.add(Info2)
    db_session.add(Client)
    db_session.commit()


def shutdown_session(exception=None):
    db_session.remove()


def provide_db(app):
    app.teardown_request(shutdown_session)
