print("📝 Word Counter\n")

text = []
print("Enter text (type END on a new line to finish):")

while True:
    line = input()
    if line == "END":
        break
    text.append(line)

full_text = "\n".join(text)

word_count = len(full_text.split())
char_count = len(full_text)
line_count = len(text)

print("\n📊 Text Analysis Result")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
print(f"Lines: {line_count}")
