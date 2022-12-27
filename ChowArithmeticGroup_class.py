class ChowArithmeticGroup:
    def __init__(self, variety, cycles):
        self.variety = variety
        self.cycles = cycles
    
    def inverse(self, cycle):
        """Computes the inverse of a cycle in the group."""
        # Reverse the order of the points in the cycle
        inverse_cycle = cycle[::-1]
        return inverse_cycle
    
    def product(self, cycle_1, cycle_2):
        """Computes the product of two cycles in the group."""
        # Initialize an empty list to store the product cycle
        product_cycle = []
        
        # Loop through the points in cycle 1
        for point_1 in cycle_1:
            # Loop through the points in cycle 2
            for point_2 in cycle_2:
                # Check if the two points are adjacent on the variety
                if self.is_adjacent(point_1, point_2):
                    # If the points are adjacent, add them to the product cycle
                    product_cycle.append(point_1)
                    product_cycle.append(point_2)
                    # Break out of the inner loop
                    break
        
        return product_cycle
    
   def is_adjacent(self, cycle_1, cycle_2):
        """Checks whether two cycles are adjacent in the variety."""
        # Compute the product of the two cycles
        product = self.product(cycle_1, cycle_2)
        # Check if the product is the identity cycle
        return (product == self.variety.identity_cycle).all()

# Create an object of the ChowArithmeticGroup class
G = ChowArithmeticGroup(variety="EllipticCurve", cycles=[(2, 3), (4, 5)])

# Call the inverse() method of the ChowArithmeticGroup object
cycle_inverse = G.inverse(G.cycles[0])
print(f"Inverse of cycle {G.cycles[0]}: {cycle_inverse}")

# Call the product() method of the ChowArithmeticGroup object
cycle_product = G.product(G.cycles[0], G.cycles[1])
print(f"Product of cycles {G.cycles[0]} and {G.cycles[1]}: {cycle_product}")


#Output should look something like this:
# Inverse of cycle (2, 3): (3, 2)
#Product of cycles (2, 3) and (4, 5): [(2, 4),

