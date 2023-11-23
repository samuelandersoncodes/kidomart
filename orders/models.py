from django.db import models


class Payment(models.Model):
    # Payment model
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.Charfield(max_length=100)
    payment_method = models.Charfield(max_length=100)
    amount_paid = models.Charfield(max_length=100)
    status = models.Charfield(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(slef):
        # Payment id string representation
        return self.payment_id
