from django.db import models

# Create your models here.

class Message(models.Model):
    class Meta:
        app_label = "contacts"
        db_table = "Messages"
        verbose_name='Сообщениe'
        verbose_name_plural = "Сообщения"
    from_name = models.CharField(null=False, blank=False, max_length=100,  verbose_name="Имя отправителя")
    from_email = models.EmailField(max_length=500,  verbose_name="Email отправителя")
    from_phone = models.CharField(null=True, blank=True, max_length=20,  verbose_name="Телефон отправителя")
    from_message = models.CharField(null=True, blank=True, max_length=500,  verbose_name="Сообщение")
    from_date_time = models.DateTimeField(verbose_name="Время отправления",null=False, blank=False)


    def __str__(self):
        return self.from_name




