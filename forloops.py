penguins = ["Gentoo", "Chinstrap", "King", "Emperor", "Adelie", "Little", "Australian Little", "White-flippered", "Magellanic", "Humboldt", "Galapagos", "African", "Yellow-eyed", "Fiordland", "Snares", "Erect-crested", "S. Rockhopper", "E. Rockhopper", "N. Rockhopper", "Royal", "Macaroni"]
scientific = ["Aptenodytes patagonicus", "Aptenodytes forsteri", "Pygoscelis adeliae", "Pygoscelis antarcticus", "Pygoscelis papua", "Eudyptula minor", "Eudyptula minor albosignata", "Spheniscus magellanicus", "Spheniscus humboldti", "Spheniscus mendiculus", "Spheniscus demersus", "Megadyptes antipodes", "Eudyptes pachyrhynchus", "Eudyptes robustus", "Eudyptes sclateri", "Eudyptes chrysocome", "Eudyptes chrysocome filholi", "Eudyptes moseleyi", "Eudyptes schlegeli", "Eudyptes chrysolophus"]
locale = ["South Atlantic", "Antarctic", "Southern Pacific", "New Zealand", "Southern Australia", "South America", "Africa", "Southern Africa", "Subantarctic"]
conservation = ["Least Concern", "Extinct", "Near Threatened", "Threatened", "Vulnerable", "Endangered", "Critically Endangered", "Extinct in Wild"]
fun = ["King penguin chicks look like kiwi birds.", "Mumble, a character from the 2006 film Happy Feet, is an emperor penguin.", "Adélie penguins get all their food from the sea.", "The main predator of a chinstrap are leopard seals.", "Gentoos are the fastest swimming penguin.", "A mass mortality happened to a group of little penguins in 1935.", "White-flippered penguins are nocturnal.", "Magellanic penguins can live up to 25 years in the wild.", "The humboldt penguin was named after Alexander von Humboldt.", ""]

p = input("Name a species of penguin, but don't write penguin afterwards (must be living)\n>")
n = 0

for i in range(0, len(penguins), 1):
    if p == penguins[i]:
        print("Ah yes, the " + p + " penguin.")
        n = i

#1 more for, 1 more if, 4 more lists

