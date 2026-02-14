class Crop:
    def __init__(self):
        # Ortak özellik: Tüm ekinler 0 grain ile başlar
        self.grains = 0

    def ripe(self):
        # Ortak özellik: Olgunlaşma sınırı 15'tir
        return self.grains >= 15
