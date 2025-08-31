from django.db import models
from authentication.models import User, SoftDeleteMixin
from core.models import Branch, Vendor


class Warehouse(SoftDeleteMixin):
    code = models.CharField(max_length=255, unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='warehouses')
    cash = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_warehouses')
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.code} - {self.branch.name}"


class GoldProduct(SoftDeleteMixin):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='gold_products')
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    carat = models.DecimalField(max_digits=10, decimal_places=2)
    stamp_enduser = models.DecimalField(max_digits=10, decimal_places=2)
    cashback = models.DecimalField(max_digits=10, decimal_places=2)
    cashback_unpacking = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_gold_products')
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.carat}K - {self.weight}g"


class SilverProduct(SoftDeleteMixin):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='silver_products')
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    carat = models.DecimalField(max_digits=10, decimal_places=2)
    stamp_enduser = models.DecimalField(max_digits=10, decimal_places=2)
    cashback = models.DecimalField(max_digits=10, decimal_places=2)
    cashback_unpacking = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_silver_products')
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.carat}K - {self.weight}g"


class GoldWarehouseStock(SoftDeleteMixin):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='gold_stock')
    product = models.ForeignKey(GoldProduct, on_delete=models.CASCADE, related_name='warehouse_stock')
    quantity = models.BigIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_gold_stock')
    updated_date = models.DateField(auto_now=True)
    
    class Meta:
        unique_together = ['warehouse', 'product']
    
    def __str__(self):
        return f"{self.product.name} - {self.warehouse.code} - Qty: {self.quantity}"


class SilverWarehouseStock(SoftDeleteMixin):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='silver_stock')
    product = models.ForeignKey(SilverProduct, on_delete=models.CASCADE, related_name='warehouse_stock')
    quantity = models.BigIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_silver_stock')
    updated_date = models.DateField(auto_now=True)
    
    class Meta:
        unique_together = ['warehouse', 'product']
    
    def __str__(self):
        return f"{self.product.name} - {self.warehouse.code} - Qty: {self.quantity}"


class WarehouseTransaction(models.Model):  # No soft delete
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    item_name = models.CharField(max_length=255)
    from_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='outgoing_transactions')
    to_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='incoming_transactions')
    quantity = models.BigIntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_transactions')
    action_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actioned_transactions')
    action_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.item_name} - {self.from_warehouse.code} -> {self.to_warehouse.code}"
