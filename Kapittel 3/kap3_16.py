from pylab import pi, floor

totalt_volum = 3  #liter
radius = 2.5 / 10  #dm

volum_kule = pi * radius**3 * 4 / 3  #dm**3 = liter
kuler = floor(totalt_volum / volum_kule)

print(f"{totalt_volum} liter is gir {kuler:.0f} kuler med radius {radius*10} cm.")