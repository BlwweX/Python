from logging import Logger

def main():
    log = Logger("Demo")
    
    print("=== Showing all log levels with prefix 'Demo' ===")
    log("Debug", "This is a Debug message")
    log("Info", "This is an Info message")
    log("Warning", "This is a Warning message")
    log("Error", "This is an Error message")
    log("Critical", "This is a Critical message")
    
    # Change prefix to None, fallback to log type
    log_no_prefix = Logger(None)
    print("\n=== Showing fallback prefix (uses log type) ===")
    log_no_prefix("Info", "Info message uses log type as prefix")
    
    # Demonstrate MinimumLevel filtering
    log_filtered = Logger("Filtered")
    log_filtered.set_minimum_level("Warning")
    print("\n=== Demonstrating MinimumLevel filtering ===")
    log_filtered("Debug", "This Debug message should NOT appear")
    log_filtered("Info", "This Info message should NOT appear")
    log_filtered("Warning", "This Warning message should appear")
    log_filtered("Error", "This Error message should appear")

main()