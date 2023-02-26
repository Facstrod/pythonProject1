text = 'Я! Есть. Грут?! Я, Грут и Есть.'

symbol_set = set(".,;:!?")
counter = 0
for i in text:
    if i in symbol_set:
        counter +=1

print(counter)