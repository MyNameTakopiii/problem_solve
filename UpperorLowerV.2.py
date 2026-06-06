def case_counter(text: str):
    case_upper = 0
    case_lower = 0
    for i in text:
        if i.isupper():
            case_upper += 1
        elif i.islower():
            case_lower += 1
        
    print(f"Uppercase: {case_upper}")
    print(f"Lowercase: {case_lower}")

case_counter(str(input()))