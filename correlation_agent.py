from crewai import Agent
from collections import defaultdict
import re

class CorrelationAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Correlation Agent",
            goal="Link log messages by timestamp and other properties.",
            backstory="An expert in correlating log messages across distributed systems.",
            verbose=True
        )

    def correlate(self, logs):
        events = defaultdict(list)
        for log in logs:
            match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', log)
            if match:
                ts = match.group(1)
                events[ts].append(log)
            else:
                events["NO_TIMESTAMP"].append(log)
        return dict(events)