from app.models.models import User, AdminUser
from app.models import SQLAConfig as sqla
import pandas as pd


class ORMQueries:

    @classmethod
    def user_admin_orm(cls, pid):
        query = sqla.session.query(User)
        query = query.join(AdminUser, AdminUser.user_id == User.id)
        query = query.filter(User.id == pid)
        query = query.with_entities(AdminUser, User)
        query = query.all()
        return query

    @classmethod
    def pandas_df_sql(cls, name_list):
        '''using pandas to load data into df and straight to sql'''
        data = {
            User.name:name_list
        }
        df = pd.DataFrame(data)
        df.to_sql('User', sqla.engine, if_exists='append')

