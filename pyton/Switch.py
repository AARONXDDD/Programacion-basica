def switch_example(option):
    switcher = {
        1: "Option 1 selected",
        2: "Option 2 selected",
        3: "Option 3 selected",
    }
    return switcher.get(option, "Invalid option")

# Example usage
option = int(input("Enter an option (1-3): "))
print(switch_example(option))