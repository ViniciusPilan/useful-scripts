import sys


# The path of the metrics file. This could be overwritten by an argument in command execution: 
# $ python process_dashboard_json_file.py FILE_PATH
FILE_PATH = "dashboard.json"
DEFAULT_FMT = "json"


if __name__ == "__main__":
    charts_counter = 0
    unique_metrics_counter = 0

    # Right execution validator
    if len(sys.argv) > 2:
        print("ERROR: Wrong execution! Try one of the following:")
        print("ERROR: '$ python process_dashboard_json_file.py FILE_PATH'")
        print("ERROR: '$ python process_dashboard_json_file.py (setting the file path inside of the process_dashboard_json_file.py file)'")
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

    with open(file_path, "r") as dashboard_json_file:
        content = dashboard_json_file.readlines()

    # Process the dashboard json file content
    for line in content:
        # TO DO ...
        continue

    # Show the Results
    print(f"INFO: There are {charts_counter} charts in the dashboard.")
    print(f"INFO: There are {unique_metrics_counter} metrics been used by the dashboard.")
