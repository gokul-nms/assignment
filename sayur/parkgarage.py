from datetime import datetime,timedelta
parking_lot = [0] * 10  
def calculate_parking_fee(entry_time, exit_time):
    entry_time = datetime.strptime(entry_time, '%H:%M')
    exit_time = datetime.strptime(exit_time, '%H:%M')
    total_minutes = (exit_time - entry_time).seconds // 60

    if total_minutes < 0:
        print("Invalid entry or exit time. Exiting program.")
        return
    if total_minutes <= 15:
        fee = 0
    elif total_minutes <= 60:
        fee = 100
    else:
        additional_fee = 0
        if total_minutes > 25:
            additional_fee += 50
        if total_minutes > 35:
            additional_fee += 50 * ((total_minutes - 35) // 30)
        fee = 100 + additional_fee
        print(f"Total parking fee: Rs {fee}")
def get_available_space():
    for i in range(len(parking_lot)):
        if parking_lot[i] == 0:
            parking_lot[i] = 1  
            return i + 1  
    return None  
def free_up_space(space_number):
    parking_lot[space_number - 1] = 0  
entry_time = input("Enter parking entry time (HH:MM): ")
space_number = get_available_space()
if space_number is not None:
    print(f"Allocated parking space: {space_number}")
    exit_time = input("Enter parking exit time (HH:MM): ")
    calculate_parking_fee(entry_time, exit_time)
    free_up_space(space_number)
else:
    print("Parking lot is full. Exiting program.")
print("Thank YOu")