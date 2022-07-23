from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from bot import bot
from bot_settings import chat_id


class Order(models.Model):
    ANSWER_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    porter = models.CharField(max_length=3, choices=ANSWER_CHOICES)
    movers = models.CharField(max_length=3, choices=ANSWER_CHOICES)
    dispersal = models.CharField(max_length=3, choices=ANSWER_CHOICES)
    trash = models.CharField(max_length=3, choices=ANSWER_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


@receiver(post_save, sender=Order)
def send_message_to_telegram(sender, instance, *args, **kwargs):
    prepared_data = f'''
Client\'s name: {instance.name}
Phone number: {instance.phone_number}

Porter: {instance.porter}
Movers: {instance.movers}
Assembling/disassembling of furniture: {instance.dispersal}
Trash removal: {instance.trash}
Descroption: {instance.description}        
            '''

    bot.send_message(chat_id, prepared_data)
