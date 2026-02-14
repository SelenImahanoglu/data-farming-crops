from farm.crop import Crop

class Corn(Crop):
    # Artık __init__ ve ripe metodlarına gerek yok,
    # çünkü onları Crop sınıfından miras alıyoruz!
    def water(self):
        self.grains += 10
