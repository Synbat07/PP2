def V(R):
    return (4/3) * 3.14 * (R**3)  #формула: V = 4/3 * π * R^3. (π = 3.14)

R = float(input("Enter the Radius of the sphere: "))

print ("Sphere volume: ", V(R))