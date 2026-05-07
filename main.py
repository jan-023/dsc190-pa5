def main():
    print("Hello from dsc190-pa5!")
    
    if len("lint violation 1"): # lint violation: len({expression}) used as condition w/o comparison
        print("Passed lint violation 1 conditional")
    
    línt_violation_2 = 2 # lint violation: non-ASCII char used in variable name

import numpy # lint violation: all import statements at top of file

if __name__ == "__main__":
    main()
