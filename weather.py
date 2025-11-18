weather=(1,0,0,0,1,1,0)
rainy=0
sunny=0
for i in weather:
    if i==1:
        rainy=rainy+1
    else:
        sunny=sunny+1
if sunny>rainy:
    print("GOOD WEATHER")
else:
    print("BAD WEATHER")