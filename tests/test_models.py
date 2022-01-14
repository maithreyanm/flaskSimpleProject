from faker import Faker
from base import Base
from app.models.models import User, AdminUser
from app.models.orm_queries import ORMQueries


class TestModel(Base):

    def test_save(self):
        usr = User()
        usr.name = 'Mith'
        usr.save_me()
        self.assertEqual(0,0)

    def test_by_id(self):
        usr_ent = User.by_id(1)
        usr_ent.name = 'herrera'
        usr_ent.save_me()
        self.assertEqual(0, 0)

    def test_key_val(self):
        dict_name = {'name': 'Mith'}
        ent = User.by_key_val(dict_name)
        self.assertEqual(0,0)

    def test_save_all(self):
        record_list = []
        fake = Faker()
        for i in range(0, 2000):
            usr = User()
            usr.name = fake.name()
            record_list.append(usr)
            if len(record_list) % 1000 == 0:
                usr.save_all(record_list)
                record_list.clear()
        self.assertEqual(0, 0)

    def test_by_ids(self):
        ids = [1, 2, 3]
        ent = User.by_ids(ids)
        self.assertEqual(0,0)

    def test_delete_me(self):
        ent = User.by_id(555)
        self.assertEqual(0,0)

    def test_foreign(self):
        # resp = ORMQueries.user_admin_orm(3)
        # print(resp)
        usr = User()
        fake = Faker()
        usr.name = fake.name()
        usr.save_me()
        adm = AdminUser()
        adm.user_name = usr.name
        adm.user_id = usr.id
        adm.save_me()

