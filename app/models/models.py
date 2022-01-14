import datetime

import sqlalchemy
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base

# from app.models import SQLAConfig as sqla

base = declarative_base()


class BaseModel(base):
    __abstract__ = True
    id = Column('id', Integer, primary_key=True)
    created_on = Column('created_on', sqlalchemy.DateTime, default=datetime.datetime.now())
    updated_on = Column('updated_on', sqlalchemy.DateTime, default=datetime.datetime.now(),
                        onupdate=datetime.datetime.now())

    def __init__(self):
        self.new_records = []

    def save_me(self):
        from app.models import SQLAConfig as sqla
        try:
            sqla.session.add(self)
            sqla.session.commit()
        except Exception as e:
            sqla.session.rollback()
            raise e

    def save_all(self, record_list):
        from app.models import SQLAConfig as sqla
        try:
            sqla.session.add_all(record_list)
            sqla.session.commit()
        except Exception as e:
            sqla.session.rollback()
            raise e

    def bulk_save(self, record_list):
        from app.models import SQLAConfig as sqla
        try:
            if len(record_list) % 1000 == 0:
                sqla.session.flush()
            else:
                sqla.session.commit()
            sqla.session.commit()
        except Exception as e:
            sqla.session.rollback()
            raise e

    def delete_me(self):
        from app.models import SQLAConfig as sqla
        try:
            sqla.session.delete(self)
            sqla.session.commit()
        except Exception as e:
            sqla.session.rollback()
            raise e

    @classmethod
    def by_id(cls, id):
        from app.models import SQLAConfig as sqla
        try:
            q = sqla.session.query(cls)
            q = q.filter(cls.id == id)
            record = q.scalar()
            return record
        except Exception as e:
            sqla.session.rollback()
            raise e

    @classmethod
    def by_key_val(cls, key_val):
        from app.models import SQLAConfig as sqla
        try:
            query = sqla.session.query(cls)
            for key, val in key_val.items():
                attrib = getattr(cls, key)
                query = query.filter(attrib == val)
            entities = query.all()
            return entities
            # if len(entities) > 1:
            #     return entities
            # else:
            #     return entities[0]
        except Exception as e:
            sqla.session.rollback()
            raise e

    @classmethod
    def ultimtae_query_runner(cls, ultimate_query):
        from app.models import SQLAConfig as sqla
        try:
            entities = ultimate_query.all()
            return entities
            # if len(entities) > 1:
            #     return entities
            # else:
            #     return entities[0]
        except Exception as e:
            sqla.session.rollback()
            raise e

    @classmethod
    def by_ids(cls, ids):
        from app.models import SQLAConfig as sqla
        try:
            query = sqla.session.query(cls)
            entities = query.filter(cls.id.in_(ids)).all()
            return entities
        except Exception as e:
            sqla.session.rollback()
            raise e


class User(BaseModel):
    __tablename__ = 'User'
    name = Column('name', String(100))

    def __repr__(self):
        return "<User %s>" % self.id

    @classmethod
    def by_name(cls, name_string):
        key_val_dict = {'name': name_string}
        records = cls.by_key_val(key_val_dict)
        return records


class AdminUser(BaseModel):
    __tablename__ = 'AdminUser'
    admin_name = Column('AdminName', String(100))
    user_name = Column('user_name', String(100))
    user_id = Column(Integer, sqlalchemy.ForeignKey('User.id'))

    def __repr__(self):
        return "<AdminUser %s>" % self.id
