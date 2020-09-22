movie = input("Enter the name of the movie : ")
thriller = list(("Dark", "Mindhunter", "Parasite", "Inception", "Insidious", "Interstellar", "Prison Break", "Money Heist", "War", "Jack Ryan"))
comedy = list(("Friends", "3 Idiots", "Brooklyn 99", "How I Met Your Mother", "Rick And Morty", "The Big Bang Theory","The Office", "Space Force"))

for i in range(len(thriller)):
    thriller[i] = thriller[i].lower()
for j in range(len(comedy)):
    comedy[j] = comedy[j].lower()

if movie.lower() in thriller:
    print("It is a thriller")
elif movie.lower() in comedy:
    print("It is a comedy")
else:
    print("It's neither comedy nor thriller")
