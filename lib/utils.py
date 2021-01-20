import itertools
import re


# Helper function for flattening a list of lists
def flatten(outer):
    return list(itertools.chain.from_iterable(outer))


# Helper function for converting a string to camel case
def str_to_camelcase(string):
    camel = string.title().replace(" ", "")
    return camel[0].lower() + camel[1:]


# Helper function for converting a string to snake case
def str_to_snakecase(string):
    snake = string.replace(" ", "_")
    return snake
