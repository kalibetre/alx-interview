#!/usr/bin/python3
"""
0-stats module
"""
import re
import signal
import sys

regex = r"^(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s-\s\[(\d{4}-\d{2}-\d{2} \d{2}"
regex += r":\d{2}:\d{2}.\d{6})\]\s(\"GET \/projects\/260 HTTP\/1.1\")\s(\d{3})"
regex += r"\s(\d{3})$"

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0
file_size = 0


def signal_handler(signal, frame):
    print_stats()


signal.signal(signal.SIGINT, signal_handler)

count = 0


def parse_line(line):
    """
    pareses a line of with the format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
    <file size>
    if the line is not with the above format returns None
    """
    match = re.match(regex, line)
    if not match:
        return None

    status_code = match.group(4)
    if status_code.isnumeric() and int(status_code) in status_codes:
        status_code = int(status_code)
    else:
        status_code = None
    return {
        "status_code": status_code,
        "file_size": int(match.group(5)),
    }


def print_stats():
    """
    prints the stats
    """
    print("File size:", file_size)
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    for line in sys.stdin:
        if count % 10 == 0 and count != 0:
            print_stats()

        stat = parse_line(line)
        if stat is not None and stat["status_code"] is not None:
            status_codes[stat["status_code"]] += 1
            file_size += stat["file_size"]
            count += 1
