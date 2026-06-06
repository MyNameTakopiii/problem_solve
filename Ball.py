def ball(height_meter: float):

    count = -1

    if (height_meter <= 0.01):
        count = 0

    while height_meter > 0.01:
        height_meter *= (3/5)
        count += 1

    print(count)
  

height = float(input())
ball(height)
        
