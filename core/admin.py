from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Branch, Vendor, Customer, Seller


class SoftDeleteAdminMixin:
    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()
    
    list_filter = ['is_deleted']
    
    def delete_model(self, request, obj):
        obj.soft_delete()
    
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.soft_delete()


@admin.register(User)
class UserAdmin(BaseUserAdmin, SoftDeleteAdminMixin):
    list_display = ['username', 'email', 'role', 'branch', 'is_active', 'is_deleted']
    list_filter = ['role', 'is_active', 'is_deleted', 'branch']
    search_fields = ['username', 'email']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'branch', 'is_deleted', 'deleted_at')}),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email', 'role', 'branch')}),
    )


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin, SoftDeleteAdminMixin):
    list_display = ['name', 'created_by', 'created_date', 'is_deleted']
    search_fields = ['name']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin, SoftDeleteAdminMixin):
    list_display = ['name', 'created_by', 'created_date', 'is_deleted']
    search_fields = ['name']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin, SoftDeleteAdminMixin):
    list_display = ['name', 'phone', 'created_by', 'created_date', 'is_deleted']
    search_fields = ['name', 'phone']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin, SoftDeleteAdminMixin):
    list_display = ['name', 'branch', 'created_by', 'created_date', 'is_deleted']
    list_filter = ['branch', 'is_deleted']
    search_fields = ['name']
    readonly_fields = ['created_date', 'updated_date']
