#!/usr/bin/env python3

import sys

if __name__ == "__main__" :
    # Rename these variables to something meaningful
    oneLine = sys.argv[1]
    multiPipe = sys.argv[2]
    multiGreater = sys.argv[2]

    print("ONE LINE VERSION")
    x = oneLine.split()
    print(x)
    
    print("MULTILINE VERSION: |")
    x = multiPipe.split()
    print(x)
    
    print("MULTILINE VERSION: >")
    x = multiGreater.split()
    print(x)
    
    print("END OUTPUT")
    
    # Fake example outputs
    output1 = "Hello"
    output2 = "World"

    # This is how you produce outputs.
    # Make sure corresponds to output variable names in action.yml
    print("::set-output name=output-one::" + output1)
    print("::set-output name=output-two::" + output2)
