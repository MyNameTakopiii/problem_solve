def main(component_1: int, side: int):
    component_2 = (side**2) - (component_1**2) 
    size = ((component_2 ** 0.5) * component_1) / 2
    return print(size)

num_1 = int(input())   
num_2 = int(input()) 

main(num_1, num_2)  