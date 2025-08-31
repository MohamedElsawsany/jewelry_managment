from django.contrib import admin
from .models import Warehouse, GoldProduct, SilverProduct, GoldWarehouseStock, SilverWarehouseStock, WarehouseTransaction
from core.admin import SoftDeleteAdminMixin


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin, SoftDeleteAdminMixin):
    list_display = ['code', 'branch', 'cash', 'created_by', 'created_date', 'is_deleted']
    list_filter = ['branch', 'is_deleted']
    search_fields = ['code']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(GoldProduct)
class GoldProductAdmin(admin.ModelAdmin, SoftDeleteAdminMixin):
    list_display = ['name', 'vendor', 'weight', 'carat', 'created_by', 'is_deleted']
    list_filter = ['vendor', 'carat', 'is_deleted']
    search_fields = ['name']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(SilverProduct)
class SilverProductAdmin(admin.ModelAdmin, SoftDeleteAdminMixin):
    list_display = ['name', 'vendor', 'weight', 'carat', 'created_by', 'is_deleted']
    list_filter = ['vendor', 'carat', 'is_deleted']
    search_fields = ['name']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(GoldWarehouseStock)
class GoldWarehouseStockAdmin(admin.ModelAdmin, SoftDeleteAdminMixin):
    list_display = ['product', 'warehouse', 'quantity', 'created_by', 'is_deleted']
    list_filter = ['warehouse', 'is_deleted']
    search_fields = ['product__name']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(SilverWarehouseStock)
class SilverWarehouseStockAdmin(admin.ModelAdmin, SoftDeleteAdminMixin):
    list_display = ['product', 'warehouse', 'quantity', 'created_by', 'is_deleted']
    list_filter = ['warehouse', 'is_deleted']
    search_fields = ['product__name']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(WarehouseTransaction)
class WarehouseTransactionAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'from_warehouse', 'to_warehouse', 'quantity', 'status', 'created_by']
    list_filter = ['status', 'from_warehouse', 'to_warehouse']
    search_fields = ['item_name']
    readonly_fields = ['created_at', 'action_at']
