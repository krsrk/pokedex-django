from django.db import models


class Pokemon(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=256)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    ability = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def to_dict(data):
        data_dict = []
        for item in data:
            data_dict.append({
                'id': item.id,
                'code': item.code,
                'name': item.name,
                'description': item.description,
                'height': str(item.height),
                'weight': str(item.weight),
                'ability': item.ability,
                'image_url': item.image_url,
                'more_info_url': item.more_info_url,
            })
        return data_dict

    @property
    def more_info_url(self):
        name = str(self.name).lower()
        return "https://www.pokemon.com/el/pokedex/" + name

    @property
    def image_url(self):
        image = str(self.code).lstrip('0') + '.png'
        return 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/' + image
