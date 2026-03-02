"""
priyakorn pichitmarn
683040494-9
P7 
"""

input_filename = "animals.txt"
output_filename = "upper.txt"

with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:

        animal_name = line.strip()
        
        uppercase_name = animal_name.upper()
        
        print(f"{animal_name} upgraded to {uppercase_name}")
        
        outfile.write(uppercase_name + "\n")