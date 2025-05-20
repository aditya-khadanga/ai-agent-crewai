from crewai import Agent

class FailureDetectionAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Failure Detection Agent",
            goal="Detect points of failure from correlated log messages.",
            backstory="A seasoned troubleshooter with deep expertise in finding root causes from logs.",
            verbose=True
        )

    def detect_failures(self, correlated_events):
        failure_report = []
        for ts, logs in correlated_events.items():
            for log in logs:
                if "ERROR" in log or "Exception" in log:
                    failure_report.append(f"[{ts}] {log}")
        if not failure_report:
            return "No failures detected."
        summary = "Failures detected:\n" + "\n".join(failure_report)
        return summary