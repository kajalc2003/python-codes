def water_jug_problem(capacity_jug1, capacity_jug2, target):
    jug1 = 0  # Initial amount of water in jug 1
    jug2 = 0  # Initial amount of water in jug 2

    while jug1 != target and jug2 != target:
        # Fill jug 1 to its full capacity
        jug1 = capacity_jug1

        # Pour water from jug 1 to jug 2 until jug 2 is full or jug 1 is empty
        while jug2 != capacity_jug2 and jug1 != 0:
            pour = min(jug1, capacity_jug2 - jug2)
            jug1 -= pour
            jug2 += pour

        # Empty jug 2
        jug2 = 0

    print("Steps to measure {} gallons of water:".format(target))
    print("Fill jug 1 to its full capacity.")
    print("Pour water from jug 1 to jug 2 until jug 2 is full.")
    print("Empty jug 2.")

# Given capacities and target
capacity_jug1 = 5
capacity_jug2 = 7
target = 4

# Solve the water jug problem
water_jug_problem(capacity_jug1, capacity_jug2, target)
