import random
from datetime import datetime, timedelta

messages = [
    "initialized",
    "started",
    "Processing request {}",
    "finished task",
    "ERROR Failed to connect to database",
    "Exception: Timeout while calling service X",
    "Request {} processed",
    "WARNING: High memory usage detected",
    "INFO: Health check passed"
]

def random_message(idx):
    # Occasionally insert request numbers
    if "{}" in messages[idx]:
        return messages[idx].format(random.randint(100, 999))
    return messages[idx]

start_time = datetime(2025, 5, 20, 6, 20, 0)
module = "Module2"

with open("aditya_logs.log", "w") as f:
    for i in range(1000):
        # Increment time: 1–5 seconds randomly
        current_time = start_time + timedelta(seconds=i * random.randint(1, 5))
        msg_idx = random.choices(
            range(len(messages)),
            weights=[4, 4, 8, 5, 3, 3, 6, 2, 2],  # More normal, fewer errors
            k=1
        )[0]
        log_msg = f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} {module} {random_message(msg_idx)}"
        f.write(log_msg + "\n")