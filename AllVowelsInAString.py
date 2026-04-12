s = input().strip()

lower_vowels = "aeiou"
upper_vowels = "AEIOU"

# Check lowercase vowels
all_lower = True
for ch in lower_vowels:
    if ch not in s:
        all_lower = False
        break

# Check uppercase vowels
all_upper = True
for ch in upper_vowels:
    if ch not in s:
        all_upper = False
        break

print(all_lower or all_upper)