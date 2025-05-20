from crewai import Agent
import glob
import os

class LogReaderAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Log Reader",
            goal="Read and extract log entries from specified files.",
            backstory="A highly efficient agent specialized in reading and parsing log files from any module.",
            verbose=True
        )

    def read_logs(self, logs_dir):
        logs = []
        log_files = glob.glob(os.path.join(logs_dir, "*.log"))
        for path in log_files:
            with open(path, encoding="utf-8") as f:
                logs.extend([line.strip() for line in f if line.strip()])
        return logs