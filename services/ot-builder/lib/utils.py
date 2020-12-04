import itertools
import re


# Helper function for flattening a list of lists
def flatten(outer):
    return list(itertools.chain.from_iterable(outer))


def to_camelcase(string):
    camel = string.title().replace(" ", "")
    return camel[0].lower() + camel[1:]
