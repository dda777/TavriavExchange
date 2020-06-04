from django.db import models


class SqlServer(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title


class Region(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.title


class Enterprise(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    cod1c7 = models.CharField(max_length=3, db_index=True)
    sql_base = models.CharField(max_length=100)
    tr5_path = models.CharField(max_length=200)
    sql_server = models.ForeignKey(SqlServer, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return 'Список объектов'

    @staticmethod
    def column_name():
        return (
            'Имя магазина',
            'Код 1с7',
            'База sql',
            'Путь к tr5',
            'Сервер SQL',
            'Регион'
        )
