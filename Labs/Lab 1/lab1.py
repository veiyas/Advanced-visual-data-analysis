file = open("data.txt", "r")
data = file.read()
print("Attempts per person/computer: " + str(round(len(data)/60)))

n_computer = 0
n_person = 0

for i in range(0,round(len(data)/60)):
    substr = data[i*60:i*60+60]
    heads_part = substr.count("0") / 60
    tails_part = substr.count("1") / 60

    if 0.49 < heads_part < 0.51 and 0.49 < tails_part < 0.51:
        n_person += 1
    else:
        n_computer += 1

print("Real people: " + str(n_person))
print("Computers: " + str(n_computer))