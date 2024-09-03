
report = [{'name': '1', 'code': 1}, {'name': 'adc', 'code': 3} , {'name': 'ac', 'code': 3}, {'name': 'yht', 'code': 1}, {'name': 'ry', 'code': 2}, {'name': 'b', 'code': 1}]

malware_count = sum(1 for item in report if item['code'] == 3)
sus_count = sum(1 for item in report if item['code'] == 2)
harmless_count = sum(1 for item in report if item['code'] == 1)

print(str(malware_count) + ' MALWARE Files')
print(str(sus_count) + ' Sus Files')
print(str(harmless_count) + ' Harmless Files')