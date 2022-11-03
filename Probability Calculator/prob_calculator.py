import copy
import random


# Consider using the modules imported above.
from typing import Dict


class Hat:
    """A representation of a Hat filled with colored balls"""
    def __init__(self, **balls):
        """Initializes the contents of the Hat object

        :param balls: a dictionary containing one or more ball colors and the amount of those colors
        """
        self.contents = []
        for aa in balls:
            self.contents += [aa] * balls[aa]

    def draw(self, drawn: int):
        """Draws a random list of balls from the contents of the hat

        :param drawn: the amount of balls to randomly draw
        :return: a random list of balls or all the contents of the hat if 'drawn' is more than what is in the hat"""
        if drawn >= len(self.contents):
            return self.contents
        removed_balls = []
        for xx in range(drawn):
            chosen_ball = random.choice(self.contents)
            removed_balls.append(chosen_ball)
            self.contents.remove(chosen_ball)
        return removed_balls


def experiment(hat: Hat, expected_balls: Dict[str, int], num_balls_drawn: int, num_experiments: int):
    """A simulation that returns the probability of getting a specific set of balls from a specific Hat object while
    drawing a specific amount of balls

    :param hat: the Hat to draw from
    :param expected_balls: which set of balls you want to be drawn from the hat
    :param num_balls_drawn: how many balls to draw from the hat
    :param num_experiments: how many times to repeat drawing from the hat
    :return: the probability
    """
    wins = 0
    for xx in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)
        win = True
        for ee in expected_balls:
            if expected_balls[ee] > drawn_balls.count(ee):
                win = False
                break
        if win:
            wins += 1
    return wins / num_experiments


# new_hat = Hat(red=6, green=2, blue=3, yellow=1)
# drew = new_hat.draw(5)
# drew.sort()
# print(drew)
