from django.contrib import admin
from .models import Category, Goods, Client, Order

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount']
    ordering = ['price', 'amount']
    list_filter = ['create_at']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Наименование товара (name)'



class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'goods_id', 'price']
    ordering = ['price']
    list_filter = ['create_at']
    search_fields = ['client_id']
    search_help_text = ('Поиск по полю Заказ клиента (client_id)')


admin.site.register(Category)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)



