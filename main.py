import analyzer

def main():
    print("Starting Automated Security Log Analyzer...\n")
    print("-" * 40)
    
    # Define where our log file is located
    log_file_path = "sample_log.txt"
    
    # Call the function we built in analyzer.py
    analyzer.read_log_file(log_file_path)
    
    print("-" * 40)
    print("\nAnalysis complete.")

# This ensures main() only runs if this specific file is executed directly
if __name__ == "__main__":
    main()