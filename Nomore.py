def NoMore():
    n = int(input())
    
    words = []
    for _ in range(n):
        words.append(input())
    
    target = input()  # อ่านตัวลบ "หลังสุด"
    
    result = [w for w in words if w != target]
    print(result)

NoMore()