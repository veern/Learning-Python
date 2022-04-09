import random

"""
This program is an example of Monte Carlo simulation. Imagine a grid where you can only move in one of cardinal directions.
Constant values below represent how many steps you want to take, how many simulations you want to make (the more the better to some degree) and what is the condition.
Condition is the distance of a character that moves from the starting point. If the distance is smaller than the condition, the condition is met.
For these set values, you can see that the furthest you can go while maintaining above 50% success rate for the condition is always 22, even though the simulations are totally random. 
"""

HOW_MANY_STEPS = 31
HOW_MANY_SIMULATIONS = 20000
CONDITION = 4

def random_walk(n_steps: int) -> tuple[int]:
    """Simulation for the walk in random directions for set amount of steps"""
    x, y = 0, 0
    #Directions are cardinal directions presented in x and y values 
    directions = ((0,1), (1,0), (0, -1), (-1, 0))
    for _ in range(n_steps):
        (dx, dy) = random.choice(directions)
        x += dx
        y += dy
    return (x, y)


def main():
    for iterations in range(HOW_MANY_STEPS):
        succesful, overall = 0, 0
        for _ in range(HOW_MANY_SIMULATIONS):
            (x, y) = random_walk(iterations)
            if abs(x) + abs(y) <=  CONDITION:
                succesful += 1
            overall += 1
        print(f"For random walk of {iterations} steps, chance of being further "
        f"than {CONDITION} blocks away is {succesful/overall*100:.2f}%")


if __name__ == "__main__":
    main()