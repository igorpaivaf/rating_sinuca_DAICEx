ratingsfile = open("ratingsfile.txt", "r")
ratingstable = open("./web/data.json", "w")

nome = ""
rating = ""
id = 1;
lines = ratingsfile.readlines()
lastline = lines[-1]


ratingstable.write("[\n")
for line in lines:
    for word in  line.split():
        if word.isnumeric() == False:
            if nome == "":
                nome += word
            else:
                nome += " " + word
        else:
            rating = word
    ratingstable.write("    {\n")
    ratingstable.write("        \"id\": " + str(id) + ",\n") 
    ratingstable.write("        \"name\": \"" + nome + "\",\n")
    ratingstable.write("        \"rating\": \"" + rating + "\"\n")
    ratingstable.write("    }")
    if line != lastline:
        ratingstable.write(",\n")
    nome = ""
    id += 1
        
ratingstable.write("]\n")
