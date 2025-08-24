import random
import copy

class Hat:
    def __init__(self, **balls):
        """Initialize hat with balls of different colors"""
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """Draw balls randomly without replacement"""
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn

        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Perform experiments to estimate probability of drawing expected balls"""
    success_count = 0

    for _ in range(num_experiments):
        # Make a fresh copy of the hat for this experiment
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count the balls in drawn set
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1

        # Check if drawn balls meet or exceed expected balls
        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments


# Example usage:

# Create hat with 5 blue, 4 red, 2 green
hat = Hat(blue=5, red=4, green=2)

# Estimate probability of drawing at least 1 red and 2 green in 4 draws
probability = experiment(hat=hat,
                         expected_balls={'red':1,'green':2},
                         num_balls_drawn=4,
                         num_experiments=2000)

print(probability)