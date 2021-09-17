from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pokemons", null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(default=0, blank=True)
    health = models.IntegerField(default=0, blank=True)
    strength = models.IntegerField(default=0, blank=True)
    defence = models.IntegerField(default=0, blank=True)
    stamina = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.latitude, self.longitude
