import sys


# The path of the metrics file. This could be overwritten by an argument in command execution: 
# $ python process_metrics_file.py FILE_PATH
FILE_PATH = "metrics.txt"
DEFAULT_FMT = "txt"


if __name__ == "__main__":
    line_counter = 0
    series_counter = 0
    
    metrics_set = set()

    # Right execution validator
    if len(sys.argv) > 2:
        print("ERROR: Wrong execution! Try one of the following:")
        print("ERROR: '$ python process_metrics_file.py FILE_PATH'")
        print("ERROR: '$ python process_metrics_file.py (setting the file path inside of the process_metrics_file.py file)'")
        sys.exit(1)

    # Defining the path of the metrics file
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = FILE_PATH 
    
    # Verify the file format
    fmt = file_path.split('.')[1]
    if fmt != DEFAULT_FMT:
        print(f"ERROR: input file with wrong format: '{fmt}'")
        sys.exit(1)
        
    with open(file_path, "r") as metrics_file:
        content = metrics_file.readlines()

    # Process the metrics file content
    for line in content:
        line_counter += 1
        if '#' not in line and len(line) > 1:
            series_counter += 1
            serie, value = line.split(' ')

            if '{' in serie:
                metric, labels = serie.split('{')
                labels = labels.replace('}', '').split(',')
            else:
                metric = serie

            metrics_set.add(metric)

    # Show the Results
    print(f"INFO: There are {line_counter} lines in the file.")
    print(f"INFO: There are {series_counter} series in the file.")
    print(f"INFO: There are {len(metrics_set)} unique metrics.")
    print(f"INFO: The unique metrics are: {sorted(metrics_set)}")
