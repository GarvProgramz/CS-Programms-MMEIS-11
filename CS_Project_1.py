# Program to create a Hotel Room Booking Management System
hotel_records = {}

print()
print("***************************************")
print("  HOTEL ROOM BOOKING MANAGEMENT SYSTEM ")
print("***************************************")

while True:
    print("\n1. Add Room Details")
    print("2. Search Room Availability")
    print("3. Display All Room Records")
    print("4. Update Room Status / Price")
    print("5. Delete Room Record")
    print("6. Exit")
    
    try:
        choice = int(input("\nEnter your choice (1-6): "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue
        
    print()
    
    # 1. ADD ROOM DETAILS
    if choice == 1:
        room_no = int(input("Enter the Room Number: "))
        if room_no in hotel_records:
            print("Room already exists in the system!")
        else:
            room_type = input("Enter Room Type (AC / Non-AC): ")
            price = float(input("Enter Price per Night: "))
            status = "Vacant"  # Default status when a room is added
            
            # Storing values as a list inside the dictionary key
            hotel_records[room_no] = [room_type, price, status]
            print(f"Room {room_no} added successfully!")
            
    # 2. SEARCH ROOM AVAILABILITY
    elif choice == 2:
        room_no = int(input("Enter the room number to be searched: "))
        if room_no in hotel_records:
            details = hotel_records[room_no]
            print(f"--- Room {room_no} Details ---")
            print("Room Type :", details[0])
            print("Price     :", details[1])
            print("Status    :", details[2])
            print("-------------------------")
        else:
            print("Room Not Found!")
            print("-----------------")
            
    # 3. DISPLAY ALL ROOM RECORDS
    elif choice == 3:
        if not hotel_records:
            print("No records available in the system.")
        else:
            print("Current Hotel Records:")
            print(hotel_records)
        print("-----------------")
        
    # 4. UPDATE ROOM STATUS / PRICE
    elif choice == 4:
        room_no = int(input("Enter the room number to be updated: "))
        if room_no in hotel_records:
            print("1. Update Booking Status (Vacant / Occupied)")
            print("2. Update Room Price")
            opt = int(input("Enter your choice: "))
            
            if opt == 1:
                new_status = input("Enter new status (Vacant/Occupied): ")
                hotel_records[room_no][2] = new_status
                print(f"The Updated status for Room {room_no} is: {hotel_records[room_no][2]}")
            elif opt == 2:
                new_price = float(input("Enter the new price: "))
                hotel_records[room_no][1] = new_price
                print(f"The Updated price for Room {room_no} is: {hotel_records[room_no][1]}")
            else:
                print("Invalid update option selection.")
        else:
            print("Room number not found!")
        print("------")
        
    # 5. DELETE ROOM RECORD
    elif choice == 5:
        room_no = int(input("Enter the room number to be deleted: "))
        if room_no in hotel_records:
            del hotel_records[room_no]
            print(f"Room {room_no} deleted successfully.")
            print("Updated Records:", hotel_records)
        else:
            print("Room number not found!")
        print("--------")
        
    # 6. EXIT
    elif choice == 6:
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")

print("You have completed your task successfully!")
print("Thank You!")
