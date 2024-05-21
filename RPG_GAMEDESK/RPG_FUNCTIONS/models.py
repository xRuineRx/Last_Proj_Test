from django.contrib.auth.models import User
from django.db import models

# Create your models here.


#Для индификации юзера при отправке откликов
class GameUser(models.Model):
    user_link = models.OneToOneField(User, on_delete=models.CASCADE)


# class GameCategory(models.Model):
#     text = models.CharField(max_length=100)

class GamePost(models.Model):
    header = models.CharField(max_length=100)
    text = models.TextField()

    #Опишем ограниченный выбор категорий
    class GameCategory(models.TextChoices):
        Cat_1 ='Танки'
        Cat_2 ='Хилы'
        Cat_3 ='ДД'
        Cat_4 ='Торговцы'
        Cat_5 ='Гилдмастеры'
        Cat_6 ='Квестгиверы'
        Cat_7 ='Кузнецы'
        Cat_8 ='Кожевники'
        Cat_9 ='Зельевары'
        Cat_10 ='Мастера заклинаний'

    CategoryCheck = models.CharField(blank=True, choices=GameCategory.choices, max_length = 100)

    #связи MtM
    link_GameUser = models.ForeignKey(GameUser, on_delete=models.CASCADE)



#Сообщения пользователей
class GameMessage(models.Model):
    text = models.TextField()
    user_link = models.OneToOneField(User, on_delete=models.CASCADE)


class PostCategory(models.Model):
    #otm = OneToMany
    link_otm_Post = models.ForeignKey(GamePost, on_delete=models.CASCADE)