import tortoise


class Music(tortoise.Model):
    name = tortoise.fields.CharField(max_length=63, unique=True)
    duration = tortoise.fields.FloatField()
    path = tortoise.fields.CharField(max_length=127, unique=True)
    genre = tortoise.fields.ForeignKeyField("app.Genre", null=True,
                                            on_delete=tortoise.fields.SET_NULL)


class Genre(tortoise.Model):
    name = tortoise.fields.CharField(max_length=200)
