from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

        self.adresses = {}

        for country in self.__data:
            self.adresses[country.id] = f"{country.name}"
            for area in country.areas:
                self.adresses[area.id] = f"{country.name} {area.name}"
                for сity in area.areas:
                    self.adresses[сity.id] = f"{country.name} {area.name} {сity.name}"



    def _apply_geocoding(self, area_id: str) -> str:
        return self.adresses.get(area_id)
