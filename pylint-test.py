import os
import sys
from pylint.lint import Run

def main():
    check_rate_code()


def check_rate_code():
    results = Run([sys.argv[1]], do_exit=False)
    if (results.linter.stats['global_note'] <= 5):
        raise Exception("Code rate smaller than standard")
        return 1
    else:
        print(results.linter.stats['global_note'])
        return 0


if __name__=='__main__':
    main()
