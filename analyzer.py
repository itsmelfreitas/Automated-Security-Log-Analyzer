def read_log_file(filepath):
    """Opens a log file and prints each line."""
    try:
        # 'r' stands for read mode
        with open(filepath, 'r') as file:
            for line in file:
                # .strip() removes hidden newline characters at the end of each line
                print(line.strip())
                
    except FileNotFoundError:
        print(f"Error: Could not find the file at {filepath}")