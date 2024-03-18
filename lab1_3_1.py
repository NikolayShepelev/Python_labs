text = "Lorem ipsum 10 dolor sit 7 amet, consectetur adipisicing 3 elit, sed do eiusmod 8 tempor incididunt ut labore et dolore magna aliqua."

count = 0
for word in text.split():
    if word.isdigit() and int(word) > 5:
        count += 1

print(count)
