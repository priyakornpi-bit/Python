"""
priyakorn pichitmarn
683040494-9
P8
"""

def main():
    input_filename = 'equations.txt'
    output_filename = 'results.txt'

    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        
            for line in infile:
                text_line = line.strip()
                
                if not text_line:
                    continue

                print(text_line)

                
                parts = text_line.split()
                
                if len(parts) != 5:
                    continue

                
                num1 = int(parts[0])
                operator = parts[1]
                num2 = int(parts[2])
                given_result = int(parts[4])

                calculated_result = 0
                if operator == '+':
                    calculated_result = num1 + num2
                elif operator == '-':
                    calculated_result = num1 - num2
                elif operator == '*':
                    calculated_result = num1 * num2

                if calculated_result == given_result:
                    print("Correct")
                else:
                    print("Wrong")
                    outfile.write(f"{num1} {operator} {num2} = {calculated_result}\n")

    except FileNotFoundError:
        print(f"Error: Could not find {input_filename}. Please create it first.")

if __name__ == "__main__":
    main() 