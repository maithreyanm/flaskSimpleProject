from app.models.models import User, AdminUser
from app.models import SQLAConfig as sqla


class ORMQueries:

    @classmethod
    def user_admin_orm(cls, pid):
        query = sqla.session.query(User)
        query = query.join(AdminUser, AdminUser.user_id == User.id)
        query = query.filter(User.id == pid)
        query = query.with_entities(AdminUser, User)
        query = query.all()
        return query
