from sqladmin import Admin, ModelView

from src import Item


class ItemAdmin(ModelView, model=Item):
    column_list = [Item.id, Item.name, Item.user_id, Item.created_at, Item.updated_at]
    column_details_list = [Item.id, Item.name]
    column_sortable_list = [Item.id]
    page_size = 50
    page_size_options = [25, 50, 100, 200]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    name = "Предмет"
    name_plural = "Предметы"