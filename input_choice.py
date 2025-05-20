def get_log_source():
    print("Select log source:")
    print("1. Log file(s) in a directory")
    print("2. Zip file containing log files")
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            log_dir = input("Enter the path to the directory containing log files: ").strip()
            return {"type": "directory", "path": log_dir}
        elif choice == "2":
            zip_path = input("Enter the path to the zip file: ").strip()
            return {"type": "zip", "path": zip_path}
        else:
            print("Invalid choice. Please enter 1 or 2.")