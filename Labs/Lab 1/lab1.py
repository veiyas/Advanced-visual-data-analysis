data = open("data.txt", "r").read()

n_computer = 0
n_person = 0

attempts = round(len(data)/60)
print("\nAttempts per person/computer: " + str(attempts))
i = 0

# Analyse the 60 attempts corresponding to each "person"
while i < len(data):
    substr = data[i:i+60]
    heads_part = substr.count("0") / 60
    tails_part = 1 - heads_part

    if 0.48 < heads_part < 0.52:
        n_person += 1
    else:
        n_computer += 1
    i += attempts

    # Debugging helper
    print("Heads: " + str(heads_part) + ", Tails: " + str(tails_part))

print("Real people: " + str(n_person))
print("Computers: " + str(n_computer))