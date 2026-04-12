s = input().strip()

words = s.split()

result = []

for word in words:
    min_char = min(word)
    max_char = max(word)
    
    diff = abs(ord(max_char) - ord(min_char))
    result.append(str(diff))

print(" ".join(result))