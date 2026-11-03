# Define the main function
# The code for the entire program goes in the main

global_variable = "Hi"

def get_area_cost(area, cost):
    total_cost = area * cost
    return total_cost


# Define a function that calculates the area
# It must accept 2 parameters - length & width
def get_area(length, width):
    area = length * width
    return area
    

def main():
    print("The program is running :)")
    # Call the function to get area
    area = get_area(7, 3)
    print(f"The area is {area} from inside the main")
    
    cost = float(input("Enter cost per unit: "))
    total_cost = get_area_cost(area,cost)
    
    print(f"The total cost is ${total_cost:.2f}")
    
    
    
# Call the main function
if __name__ == "__main__":
    main()
    
    