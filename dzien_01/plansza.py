
x, y = 50, 50


# PGR

if x > 100 or x < 0 or y > 100 or y < 0:
    print("Jesteś poza planszą")
elif x <= 10 and y <= 10:
    print("LDR")
elif x <= 10 and y >= 90:
    print("LGR")
elif x >= 90 and y >= 90:
    print("PGR")
elif x >= 90 and y <= 10:
    print("PDR")
elif x <= 10:
    print("LK")
elif x >= 90:
    print("PK")
elif y <= 10:
    print("DK")
elif y >= 90:
    print("GK")
else:
    print("Centrum")
  
    
    
     