def restaurant(age:int, plate:int):

    price = plate * 100 

    if (age > 60):
        if (plate == 1):
            return print("Free")
        elif (plate > 1):
            return print(f'Pay {int(price / 2)} baht') 
        else: 
            return print("Error")
    
    return print(f'Pay {int(price)} baht') 

num_1 = int(input())
num_2 = int(input())
restaurant(num_1, num_2)
        
