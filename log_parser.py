import re
import argparse


def parse_ip(s):
    res = re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)
    if res:
        return res.group(0)
    return ''


def test_parse_ip():
    assert parse_ip('115.42.150.37') == '115.42.150.37'
    assert parse_ip('asd 115.42.150.37') == ''
    assert parse_ip('83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET ') == '83.149.9.216'
    assert parse_ip('255.255.255.255') == '255.255.255.255'
    assert parse_ip('1.1.1.1') == '1.1.1.1'
    assert parse_ip('111.1.1') == ''


def parse(logs):
    ips = [parse_ip(line) for line in logs]
    d = {x: ips.count(x) for x in ips}
    ip_count_tuples = [(k, v) for k, v in d.items()]
    ip_count_tuples.sort(key=lambda t: t[1], reverse=True)
    return ip_count_tuples


def test_parse():
    assert parse([]) == []
    assert parse(['83.149.9.216 - - [17/May/2015:10:05:03 +0000] ']) == [('83.149.9.216', 1)]
    logs = [
        '83.149.9.216 - - [17/May/2015:10:05:03 +0000] ',
        '83.149.9.216 - - [17/May/2015:10:05:43 +0000] '
    ]
    assert parse(logs) == [('83.149.9.216', 2)]
    logs = [
        '83.149.9.216 - - [17/May/2015:10:05:03 +0000] ',
        '83.149.9.216 - - [17/May/2015:10:05:03 +0000] ',
        '11.149.9.216 - - [17/May/2015:10:05:43 +0000] '
    ]
    assert parse(logs) == [('83.149.9.216', 2), ('11.149.9.216', 1)]


def parse_file(log_name):
    with open(log_name) as file:
        return parse(file.readlines())


def test_parse_file():
    assert parse_file('apache_logs_small.txt') == [('83.149.9.216', 3), ('93.114.45.13', 2), ('24.236.252.67', 1)]


parser = argparse.ArgumentParser(description='This script finds area of triangle')
parser.add_argument("log_name", help="log file name")
if __name__ == '__main__':
    args = parser.parse_args()
    for ip, count in parse_file(args.log_name):
        print(ip, count)
