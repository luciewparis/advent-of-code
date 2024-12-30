# 1. Start by generating the list of reports


with open('advent-2-0-inputs.txt') as f:
    reports = f.read().splitlines()

print(reports) # check the format of reports
print(len(reports))
'''

reports = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]
'''
# 2. Check if the different reports are safe i.e
    # (a) The levels are either all increasing or all decreasing. -> report_status_direction 
    # (b) Any two adjacent levels differ by at least one and at most three. -> report_interval
# Increment nb_reports_safe every time a safe report is found
nb_reports_safe = 0

for report in reports:
    print(f"\n report: {report}")
    elements = report.split() # get the numbers of each report in a list of strings
    print(f"\n elements à analyser: {elements}")
    report_symbol_list = []
    print(f"\n nb_reports_safe en début de report!: {nb_reports_safe}")
    print(report_symbol_list)
    
    # (a - 1) calcul des symboles (added the = condition)
    for i in range(0, len(elements)-1):
        if int(elements[i+1]) > int(elements[i]):
            report_symbol_list.append('+')
        elif int(elements[i+1]) < int(elements[i]):
            report_symbol_list.append('-')
        else :
            report_symbol_list.append('=')
        print(f"for i = {i}: {report_symbol_list}")
    
    # (a - 2) check règle a
    if (('+' in report_symbol_list) and ('-' in report_symbol_list)) or (('+' in report_symbol_list) and ('=' in report_symbol_list)) or (('-' in report_symbol_list) and ('=' in report_symbol_list)) :
        print(f"did NOT pass (a), check dampener because double symbols")

        print(f"nb of - : {report_symbol_list.count('-')} and b of + : {report_symbol_list.count('+')}")
        if report_symbol_list.count('-') == 1 or report_symbol_list.count('+') == 1 or report_symbol_list.count('=') == 1: # only 1 element is the issue for (a)
            print(f"in IF loop to check dampener in detail")
            if '+' in report_symbol_list and '-' in report_symbol_list and '=' in report_symbol_list: # 3 symbols => UNSAFE
                print("has 3 symbols => UNSAFE")
                continue
            else :
                if report_symbol_list[0] == '+':
                    print(f"symbol starts with +")
                    if '=' in report_symbol_list : # we have both + and = 
                        index_change = report_symbol_list.index('=')+1
                    else:
                        index_change = report_symbol_list.index('-')+1
                elif report_symbol_list[0] == '-':
                    print(f"symbol starts with -")
                    if '=' in report_symbol_list : # we have both + and = 
                        index_change = report_symbol_list.index('=')+1
                    else:
                        index_change = report_symbol_list.index('+')+1
                else:
                    print(f"symbol starts with = (else)")
                    index_change = report_symbol_list.index('=')+1
            print(f"index change at position : {index_change}")

            if index_change >= len(report_symbol_list) - 1 or index_change == 1 : # remove the first or last element is enough
                print(f" =============>> pass (a) with dampener, go to (b)")
                elements.pop(index_change)
                report_test_b = 0
                for i in range(0, len(elements)-1):
                    print(f"for i = {i}")
                    if abs(int(elements[i+1]) - int(elements[i])) < 1 or abs(int(elements[i+1]) - int(elements[i])) > 3:
                        print(f"failed (b) - for i = {i} before break, nb_reports_safe = {nb_reports_safe}")
                        print(f"distance is NOT compliant = {abs(int(elements[i+1]) - int(elements[i]))}")
                        break # did not pass (b), break & go to next report
                    else:
                        report_test_b += 1
                        print(f"report_test_b = {report_test_b}")
                        print(f"distance is compliant = {abs(int(elements[i+1]) - int(elements[i]))}")
                if report_test_b == len(elements) - 1:    
                    nb_reports_safe += 1
                    print(f"nb_reports_safe incrémentée!: {nb_reports_safe}")
                else:
                    print(f"did NOT pass (a) nor dampener, report UNSAFE")

            else: # element to remove is not last in the list, need to calculate the new symbol
                report_symbol_list.pop(index_change-1)
                print(f"new symbol list after pop: {report_symbol_list}")
                if int(elements[index_change+1]) > int(elements[index_change-1]):
                    print(f"new symbol is + since diff is: {int(elements[index_change+1]) - int(elements[index_change-1])}")
                    report_symbol_list.append('+')
                elif int(elements[index_change+1]) < int(elements[index_change-1]):
                    print(f"new symbol is - since diff is: {int(elements[index_change+1]) - int(elements[index_change-1])}")
                    report_symbol_list.append('-')

                if ('+' in report_symbol_list) and ('-' in report_symbol_list) : # did not pass (a) even with dampener, break & go to next report
                    print(f"did NOT pass (a) after dampener")
                else:
                    print(" =============>> go to (b) thanks to dampener")
                    elements.pop(index_change)
                    report_test_b = 0
                    for i in range(0, len(elements)-1):
                        print(f"for i = {i}")
                        if abs(int(elements[i+1]) - int(elements[i])) < 1 or abs(int(elements[i+1]) - int(elements[i])) > 3:
                            print(f"failed (b) - for i = {i} before break, nb_reports_safe = {nb_reports_safe}")
                            print(f"distance is NOT compliant = {abs(int(elements[i+1]) - int(elements[i]))}")
                            break # did not pass (b), break & go to next report
                        else:
                            report_test_b += 1
                            print(f"report_test_b = {report_test_b}")
                            print(f"distance is compliant = {abs(int(elements[i+1]) - int(elements[i]))}")
                    if report_test_b == len(elements) - 1:    
                        nb_reports_safe += 1
                        print(f"nb_reports_safe incrémentée!: {nb_reports_safe}")
                    else:
                        print(f"did NOT pass (a) nor dampener, report UNSAFE")
    
    # passed (a) so check (b)
    else: 
        print(f"passed (a), check (b)")
        report_test_b = 0
        dampener_used = False
        for i in range(0, len(elements)-1):
            print(f"for i = {i} while list is of size {len(elements)}")
            print(f"elements = {elements}")
            print(f"element at i = {elements[i]}")
            if abs(int(elements[i+1]) - int(elements[i])) < 1 or abs(int(elements[i+1]) - int(elements[i])) > 3:
                print(f"failed (b) - for i = {i} before break, nb_reports_safe = {nb_reports_safe}")
                print(f"distance is NOT compliant = {abs(int(elements[i+1]) - int(elements[i]))}")
                print("will check dampener since it has not been used in (a)")
                if dampener_used == False:
                    elements.pop(i+1)
                    dampener_used == True
                    print("dampener used in (b)")
                    print(f"i = {i} while len(elements) = {len(elements)}")
                    if i >= len(elements) - 1:
                        print("dampener on last number => PASS ")
                    else:
                        if abs(int(elements[i+1]) - int(elements[i-1])) < 1 or abs(int(elements[i+1]) - int(elements[i-1])) > 3:
                            print(f"after pop, it is okay, continue to next i")
                        else: 
                            print(f"after pop, not okay => failed (b)")
                        break
                else:
                    break # did not pass (b), break & go to next report
            else:
                report_test_b += 1
                print(f"report_test_b = {report_test_b}")
                print(f"distance is compliant = {abs(int(elements[i+1]) - int(elements[i]))}")
        if report_test_b == len(elements) - 1:    
            nb_reports_safe += 1
            print(f"nb_reports_safe incrémentée!: {nb_reports_safe}")
            
print(f"\n >>>>> Nombre de reports safe après problem dampener = {nb_reports_safe} <<<<<<<<<")  
            