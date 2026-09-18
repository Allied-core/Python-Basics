numbers = [1, 2, 2, 3, 4, 4, 5, 1]
final = []
for selected in numbers:
    for i in final:
        if selected == i:
            break
    else:
        final.append(selected)
print(final)            
