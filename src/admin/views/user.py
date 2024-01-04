from sqladmin import Admin, ModelView

from src import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.login]
    column_details_list = [User.id, User.login, User.created_at, User.updated_at]
    column_sortable_list = [User.id]
    page_size = 50
    page_size_options = [25, 50, 100, 200]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    name = "Пользователь"
    name_plural = "Пользователи"
