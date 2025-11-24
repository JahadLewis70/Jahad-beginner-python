# Electronics Store Inventory Management System

electronics = ["TV", "Laptop", "Mobile", "Headphones", "Camera"]

print("Initial list:", electronics)

electronics.append("Tablet")
electronics.insert(2, "Smartwatch")

if "Camera" in electronics:
    electronics.remove("Camera")

new_items = ["Printer", "Router", "Monitor"]
electronics.extend(new_items)

print("Index of Laptop:", electronics.index("Laptop"))

electronics.reverse()

if electronics:
    del electronics[0]

print("Total items:", len(electronics))
print("Sorted list:", sorted(electronics))
print("Laptop count:", electronics.count("Laptop"))
print("Final list:", electronics)
