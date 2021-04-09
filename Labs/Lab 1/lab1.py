file = open("data.txt", "r")
data = file.read()


n_computer = 0
n_person = 0

attempts = round(len(data)/60)
print("Attempts per person/computer: " + str(attempts))
i = 0
while i < len(data):
    substr = data[i:i+60]
    heads_part = substr.count("0") / 60
    tails_part = 1 - heads_part

    if 0.48 < heads_part < 0.52:
        n_person += 1
    else:
        n_computer += 1
    i += attempts

print("\nReal people: " + str(n_person))
print("Computers: " + str(n_computer))