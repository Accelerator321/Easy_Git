import os
def execute(command):
  
    output_file = os.popen(command)

    output = output_file.read()

    output_file.close()

    # Display the output
    
    return output