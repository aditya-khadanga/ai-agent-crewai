# Log Analysis Pipeline with Python & Crew AI

A modular Python project integrated with crew ai for automated log file analysis. This tool reads log files from a directory, performs log correlation, and detects failures such as errors or exceptions.

## Features

- **Reads all `.log` files from a target directory**
- **Correlates logs by timestamp for easier analysis**
- **Detects and summarizes log failures (ERROR/Exception)**
- **Modular, extensible, and easy to integrate**
- **Bonus: Log file generator**

## Project Structure

```
.
├── log_reader_agent.py
├── correlation_agent.py
├── failure_detection_agent.py
├── main.py
├── logs/
│   └── *.log
├── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.7+
- [crewai](https://pypi.org/project/crewai/)

### Installation

1. Clone the repository or copy the files to your project directory.
2. Install dependencies:
   ```bash
   pip install crewai
   ```

### Usage

1. Place all your `.log` files in the `logs/` directory (create if it doesn't exist).
2. Run the main script:
   ```bash
   python main.py
   ```
3. The program will output a report of all detected failures.

### Customization

- **Change log directory**: Edit the `logs_dir` variable in `main.py` to point to your desired folder.
- **Extend failure detection**: Update `FailureDetectionAgent` for custom error patterns.
- **Add features**: The modular agent design allows you to easily add preprocessing, visualization, or new analysis logic.

## Example Output

```
Failures detected:
[2025-05-20 10:27:00] ERROR: Database connection failed
[2025-05-20 10:27:01] Exception: Timeout occurred in module X
...
```

## License

MIT License

## Author

Aditya Khadanga
