dictio = {"(":")", "{":"}", "[":"]"}

parentheses = input() # (){}[], {[()]}

stack = []

for char in parentheses:
    if char in dictio:
        stack.append(char)
    elif char in dictio.values():
        if not stack:
            print("NO")
            break
        last_open = stack.pop()
        if dictio[last_open] != char:
            print("NO")
            break
    elif char not in dictio and char not in dictio.values():
        print("NO")
        break

else:
    print("YES")