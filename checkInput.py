import sys


# check argument requirements from command line input
def check_input(program):
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("Usage: python " + program + " file_name puzzle_height puzzle_width")
        sys.exit(0)
    if len(sys.argv) != 4:
        print("Wrong usage. Enter 'python " + program + " -h' for help.")
        sys.exit(1)
