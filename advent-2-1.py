# 1. Start by generating the list of reports

with open('advent-2-0-input.txt') as f:
    reports = f.read().splitlines()

print(reports) # check the format of reports
print(len(reports))


# reports = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"] # should return 2 

# 2. Check if the different reports are safe i.e
    # (a) The levels are either all increasing or all decreasing. -> report_status_direction 
    # (b) Any two adjacent levels differ by at least one and at most three. -> report_interval
# Increment nb_reports_safe every time a safe report is found
nb_reports_safe = 0

for report in reports:
    # print(f"\n taille reports: {len(reports)}")
    # print(f"\n report: {report}")
    elements = report.split() # get the numbers of each report in a list of strings
    # print(f"\n elements à analyser: {elements}")
    report_symbol_list = []
    # print(f"\n nb_reports_safe en début de report!: {nb_reports_safe}")
    # print(report_symbol_list)
    for i in range(0, len(elements)-1):
        if int(elements[i+1]) > int(elements[i]):
            report_symbol_list.append('+')
        elif int(elements[i+1]) < int(elements[i]):
            report_symbol_list.append('-')
        # print(f"for i = {i}: {report_symbol_list}")
    if ('+' in report_symbol_list) and ('-' in report_symbol_list) : # did not pass (a), break & go to next report
        print(f"did NOT pass (a), go to next report")
        # break => when reached, breaks out of the FOR report in reports loop!!!
    else: # passed (a) so check (b)
        # print(f"passed (a), check (b)")
        report_test_b = 0
        for i in range(0, len(elements)-1):
            # print(f"for i = {i}")
            if abs(int(elements[i+1]) - int(elements[i])) < 1 or abs(int(elements[i+1]) - int(elements[i])) > 3:
                # print(f"failed (b) - for i = {i} before break, nb_reports_safe = {nb_reports_safe}")
                # print(f"distance is NOT compliant = {abs(int(elements[i+1]) - int(elements[i]))}")
                break # did not pass (b), break & go to next report
            else:
                report_test_b += 1
                # print(f"report_test_b = {report_test_b}")
                # print(f"distance is compliant = {abs(int(elements[i+1]) - int(elements[i]))}")
        if report_test_b == len(elements) - 1:    
            nb_reports_safe += 1
            # print(f"nb_reports_safe incrémentée!: {nb_reports_safe}")
            
print(f"\n >>>>> Nombre de reports safe = {nb_reports_safe} <<<<<<<<<")  # 2310 is too high
            