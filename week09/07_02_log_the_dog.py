"""
Look up how to use the argv module in python
Run this program as command line and use the argv module to indicate the logging level
Write your logging code to have all the levels of severity
Practice using the different levels of severity on your dog code below. be creative!

"""

import sys
import logging

class Dog:
    def __init__(self, limbs=None, eyes=None, color=None, kindness=None):
        self.limbs = limbs
        self.eyes = eyes
        self.color = color
        self.kindness = kindness

        # Log based on properties
        logging.debug(f"Created Dog: limbs={limbs}, eyes={eyes}, color={color}, kindness={kindness}")

        if limbs is not None and limbs < 4:
            logging.warning(f"Dog has {limbs} limbs — this is fewer than 4! Might need help!")

        if kindness in ("sad", "lonely"):
            logging.warning(f"Dog appears {kindness} — might need extra care!")

        if kindness in ("mean", "angry"):
            logging.critical(f"Dog is {kindness} — be cautious!")

        # General info
        logging.info(f"Dog summary: {color} dog with {eyes} eyes.")

if __name__ == "__main__":
    # Default level
    log_level = logging.WARNING

    if len(sys.argv) > 1:
        arg_level = sys.argv[1].upper()
        if arg_level in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
            log_level = getattr(logging, arg_level)

    # Configure logger
    logging.basicConfig(
        level=log_level,
        format="%(levelname)s: %(message)s"
    )

    # Create some test dogs
    Dog(limbs=3, eyes=1, color="red", kindness="nice")
    Dog(limbs=4, eyes=2, color="brown", kindness="sad")
    Dog(limbs=4, eyes=2, color="black", kindness="angry")
    Dog(limbs=2, eyes=2, color="white", kindness="mean")
    Dog(limbs=4, eyes=2, color="golden", kindness="happy")