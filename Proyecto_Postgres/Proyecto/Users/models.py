from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=30)
    lastname_user = models.CharField(max_length=30)
    number_user = models.IntegerField()
    age_user = models.IntegerField()

    class Meta:
        managed = True
        db_table = '_users_5'