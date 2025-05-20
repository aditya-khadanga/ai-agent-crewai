from log_reader_agent import LogReaderAgent
from correlation_agent import CorrelationAgent
from failure_detection_agent import FailureDetectionAgent

if __name__ == "__main__":
    logs_dir = "logs"  # Change this if your logs are elsewhere

    reader = LogReaderAgent()
    logs = reader.read_logs(logs_dir)

    if not logs:
        print("No logs found.")
        exit()

    correlator = CorrelationAgent()
    correlated = correlator.correlate(logs)

    detector = FailureDetectionAgent()
    report = detector.detect_failures(correlated)

    print(report)