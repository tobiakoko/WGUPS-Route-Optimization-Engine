# Function that delivers packages assigned to a truck, updating their statuses and tracking distances.
def deliver_packages(trucks, truck_number):
    # Delivers packages assigned to a truck, updating their statuses and tracking distances.
    undelivered = []  # Create a list to store undelivered packages
    # Iterate over package IDs assigned to the truck and fetch corresponding Package objects
    for package_id in trucks.packages:
        p = hash_table.lookup_package(package_id)
        undelivered.append((p, truck_number))  # Add Package object and truck number to undelivered list
    # Clear the truck's package list as we'll reassign them during delivery
    trucks.packages.clear()
    # Continue delivery process until all packages are delivered
    while len(undelivered) > 0:
        next_address = 1000  # Initialize to a large value to find the shortest distance
        next_package = None  # Initialize next_package to None
        # Find the next package with the shortest distance from the truck's current address
        for p, truck_num in undelivered:
            # Check if this package has a shorter distance compared to previous packages
            if distance_between(load_address(trucks.address), load_address(p.address)) <= next_address:
                # Update next_address with the shorter distance
                next_address = distance_between(load_address(trucks.address), load_address(p.address))
                next_package = p  # Update next_package with the current package
                truck_number = truck_num  # Update truck number
        # Add the next package to the truck's delivery list
        trucks.packages.append(next_package.package_id)
        # Remove the delivered package from the undelivered list
        undelivered.remove((next_package, truck_number))
        # Update truck's mileage by adding the distance traveled for this delivery
        trucks.mileages += next_address
        # Update truck's address to the address of the delivered package
        trucks.address = next_package.address
        # Update truck's time by adding the time taken to travel to the next address
        trucks.time += timedelta(hours=next_address / 18)
        # Update delivery and departure times for the delivered package
        next_package.delivered_at = trucks.time
        next_package.departed_at = trucks.depart_time
        # Print package details including truck number
        print(f"Package ID: {next_package.package_id} || Address: {next_package.address}, {next_package.city}, {next_package.state}, {next_package.zip} || Delivery Status: Delivered || Deadline: {next_package.deadline} || Package Weight: {next_package.weight} || Departure Time: {next_package.departed_at} || Delivery Time: {next_package.delivered_at} || Truck {truck_number}")


deliver_packages(truck1, 1)   # Deliver packages for truck 1
deliver_packages(truck2, 2)   # Deliver packages for truck 2

# Set departure time for truck 3 to be the minimum of the arrival times of truck 1 and truck 2
truck3.depart_time = min(truck1.time, truck2.time)
deliver_packages(truck3, 3)  # Deliver packages for truck 3
