parking_lot = [[None] * 5 for _ in range(5)]  
def enter_parking():
    for i in range(len(parking_lot)):
        for j in range(len(parking_lot[i])):
            if parking_lot[i][j] is None:
                parking_lot[i][j] = True  
                print(f"Car parked at spot ({i+1}, {j+1})")
                return
    print("Parking lot is full. Cannot park.")
def leave_parking():
    spot = input("Enter the spot to leave (e.g., 1,2): ")
    i, j = map(int, spot.split(','))
    if parking_lot[i-1][j-1] is not None:
        parking_lot[i-1][j-1] = None  
        print(f"Car left from spot ({i}, {j})")
    else:
        print("No car parked at the specified spot.")

def get_toll_collection():
    total_toll = sum(1 for row in parking_lot for spot in row if spot is not None)
    print(f"Total toll collection: ${total_toll}")
while True:
    print("\n1. Enter Parking\n2. Leave Parking\n3. Get Toll Collection\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        enter_parking()
    elif choice == '2':
        leave_parking()
    elif choice == '3':
        get_toll_collection()
    elif choice == '4':
        print("THANK YOU")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
