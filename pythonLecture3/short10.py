results = [
    "Mario",
    "Luigi",
]
results.append("Princess") #addint to a list
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."]) # it will result list in list
results.remove(["Bowser", "Donkey Kong Jr."]) 
results.extend(["Bowser", "Donkey Kong Jr."]) # this can help extend our list with other list


print(results)