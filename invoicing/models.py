from django.db import models
from authentication.models import User
from core.models import Branch, Customer, Seller
from inventory.models import Warehouse


class GoldInvoice(models.Model):  # No soft delete
    TRANSACTION_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Visa', 'Visa'),
    ]
    
    INVOICE_TYPE_CHOICES = [
        ('Sale', 'Sale'),
        ('Return Packing', 'Return Packing'),
        ('Return Unpacking', 'Return Unpacking'),
    ]
    
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='gold_invoices')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='gold_invoices')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='gold_invoices')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='gold_invoices')
    gold_price_21 = models.DecimalField(max_digits=10, decimal_places=2)
    gold_price_24 = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE_CHOICES, default='Cash')
    invoice_type = models.CharField(max_length=50, choices=INVOICE_TYPE_CHOICES)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_gold_invoices')
    
    def __str__(self):
        return f"Gold Invoice #{self.id} - {self.customer.name} - {self.total_price}"


class GoldInvoiceItem(models.Model):  # No soft delete
    invoice = models.ForeignKey(GoldInvoice, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=255)
    item_weight = models.DecimalField(max_digits=10, decimal_places=2)
    item_carat = models.DecimalField(max_digits=10, decimal_places=2)
    item_stamp_enduser = models.DecimalField(max_digits=10, decimal_places=2)
    item_num1 = models.DecimalField(max_digits=10, decimal_places=2)
    item_num2 = models.DecimalField(max_digits=10, decimal_places=2)
    item_quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_total_price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.item_name} - Qty: {self.item_quantity}"


class SilverInvoice(models.Model):  # No soft delete
    TRANSACTION_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Visa', 'Visa'),
    ]
    
    INVOICE_TYPE_CHOICES = [
        ('Sale', 'Sale'),
        ('Return Packing', 'Return Packing'),
        ('Return Unpacking', 'Return Unpacking'),
    ]
    
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='silver_invoices')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='silver_invoices')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='silver_invoices')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='silver_invoices')
    silver_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE_CHOICES, default='Cash')
    invoice_type = models.CharField(max_length=50, choices=INVOICE_TYPE_CHOICES)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_silver_invoices')
    
    def __str__(self):
        return f"Silver Invoice #{self.id} - {self.customer.name} - {self.total_price}"


class SilverInvoiceItem(models.Model):  # No soft delete
    invoice = models.ForeignKey(SilverInvoice, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=255)
    item_weight = models.DecimalField(max_digits=10, decimal_places=2)
    item_carat = models.DecimalField(max_digits=10, decimal_places=2)
    item_stamp_enduser = models.DecimalField(max_digits=10, decimal_places=2)
    item_num1 = models.DecimalField(max_digits=10, decimal_places=2)
    item_num2 = models.DecimalField(max_digits=10, decimal_places=2)
    item_quantity = models.BigIntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_total_price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.item_name} - Qty: {self.item_quantity}"