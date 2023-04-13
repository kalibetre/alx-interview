#!/usr/bin/python3
"""
0-stats module
"""
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0
file_size = 0
count = 0


def parse_line(line):
    """
    pareses a line of with the format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
    <file size>
    if the line is not with the above format returns None
    """
    if len(line.split()) < 2:
        return None
    try:
        file_size = int(line.split()[-1])
        status_code = int(line.split()[-2])

        if status_code not in status_codes:
            status_code = None
    except Exception:
        status_code = None
        file_size = 0

    return {
        "status_code": status_code,
        "file_size": file_size,
    }


def print_stats():
    """
    prints the stats
    """
    print("File size: {}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            if count == 10:
                print_stats()
                count = 0

            stat = parse_line(line)
            if stat is not None:
                if stat["status_code"] is not None:
                    status_codes[stat["status_code"]] += 1
                file_size += stat["file_size"]
                count += 1

        if count > 0:
            print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
