from sqlalchemy import create_engine

from sqlalchemy import orm, MetaData
from config import Config


class SQLAConfig:
    session = None

    @classmethod
    def initialize(cls):
        sql_alc_url = f'mysql+pymysql://{Config.db_user}:{Config.db_pass}@{Config.db_host}:3306/{Config.db_name}'
        engine = create_engine(sql_alc_url)
        conn = engine.connect()
        metadata = MetaData()
        Session = orm.sessionmaker(bind=engine)
        cls.session = Session()
        from app.models.models import base
        base.metadata.create_all(bind=engine)
