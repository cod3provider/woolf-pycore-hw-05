import sys
import os
import re
from collections import defaultdict
from typing import List, Dict


def parse_log_line(line: str) -> Dict[str, str]:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }


def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return [log for log in logs if log['level'].upper() == level.upper()]


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts


def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in sorted(counts.items()):
        print(f"{level:<16} | {count:<8}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python 03.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]

    # Ensure file_path is relative to the script's directory if not an absolute path
    if not os.path.isabs(file_path):
        file_path = os.path.join(os.path.dirname(__file__), file_path)

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
