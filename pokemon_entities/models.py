from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField("Название (рус.)", max_length=200)
    title_en = models.CharField(
        "Название (англ.)", max_length=200, blank=True
    )
    title_jp = models.CharField(
        "Название (яп.)", max_length=200, blank=True
    )
    previous_evolution = models.ForeignKey(
        "Pokemon", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="next_evolution", verbose_name="Предыдущая эволюция",
    )
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(
        "Изображение", upload_to="pokemons", null=True, blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name="Покемон"
    )
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    appeared_at = models.DateTimeField(
        "Дата и время появления", null=True, blank=True
    )
    disappeared_at = models.DateTimeField(
        "Дата и время исчезновения", null=True, blank=True
    )
    level = models.IntegerField("Уровень", default=0, blank=True)
    health = models.IntegerField("Здоровье", default=0, blank=True)
    strength = models.IntegerField("Сила", default=0, blank=True)
    defence = models.IntegerField("Защита", default=0, blank=True)
    stamina = models.IntegerField("Выносливость", default=0, blank=True)

    def __str__(self):
        return f"{self.pokemon}: {self.latitude}, {self.longitude}"
