from django.contrib import admin
from .models import GoldInvoice, GoldInvoiceItem, SilverInvoice, SilverInvoiceItem


class GoldInvoiceItemInline(admin.TabularInline):
    model = GoldInvoiceItem
    extra = 1


@admin.register(GoldInvoice)
class GoldInvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'seller', 'branch', 'total_price', 'invoice_type', 'created_date']
    list_filter = ['invoice_type', 'transaction_type', 'branch', 'created_date']
    search_fields = ['customer__name', 'seller__name']
    readonly_fields = ['created_date']
    inlines = [GoldInvoiceItemInline]


@admin.register(GoldInvoiceItem)
class GoldInvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'item_name', 'item_weight', 'item_carat', 'item_quantity', 'item_total_price']
    list_filter = ['item_carat', 'vendor_name']
    search_fields = ['item_name', 'vendor_name']


class SilverInvoiceItemInline(admin.TabularInline):
    model = SilverInvoiceItem
    extra = 1


@admin.register(SilverInvoice)
class SilverInvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'seller', 'branch', 'total_price', 'invoice_type', 'created_date']
    list_filter = ['invoice_type', 'transaction_type', 'branch', 'created_date']
    search_fields = ['customer__name', 'seller__name']
    readonly_fields = ['created_date']
    inlines = [SilverInvoiceItemInline]


@admin.register(SilverInvoiceItem)
class SilverInvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'item_name', 'item_weight', 'item_carat', 'item_quantity', 'item_total_price']
    list_filter = ['item_carat', 'vendor_name']
    search_fields = ['item_name', 'vendor_name']