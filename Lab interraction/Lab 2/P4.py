def calculate_average_temp():
    try:
        input_str = input("Enter 5 temps in Celcius: ")
        parts = input_str.split()
        
        if len(parts) != 5:
            print("Please input exactly 5 numbers")
        else:
            temps = [float(x) for x in parts]
            average = sum(temps) / len(temps)
            print(f"Average temperature = {average:.2f} Celsius")

    except ValueError as e:
        print(f"Catch ValueError: {e}")

if __name__ == "__main__":
    calculate_average_temp()