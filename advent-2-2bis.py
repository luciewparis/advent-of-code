# 1. Start by generating the list of reports

with open('advent-2-reports.txt') as f:
    reports = f.read().splitlines()

print(reports) # check the format of reports
print(len(reports))
'''

# reports = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]
reports = ["2 1 2 3", "1 2 4 6 9", "9 6 4 2 1", "1 2 1 4 6", "3 2 4 6 9", "1 2 4 6 5", "6 4 1 2 1", "6 6 4 2 2", "6 6 7 3 1", "1 2 10 4 6", "1 5 2 10 4", "1 2 1 6 7", "3 2 4 10 11"]
# reports = ["1 2 1 4 6", "1 2 4 6 5", "1 2 1 6 7"]
'''
# 2. Define functions checkA() and checkB() that will be used later 

    # CheckA -> (a) The levels are either all increasing or all decreasing. -> report_status_direction 
    # CheckB -> (b) Any two adjacent levels differ by at least one and at most three. -> report_interval

def checkA(liste_):
    status = None
    diff = 0
    report_symbol_list = []

    for i in range(0, len(liste_)-1):
        if int(liste_[i+1]) > int(liste_[i]):
            diff += 1
            report_symbol_list.append('+')
        elif int(liste_[i+1]) < int(liste_[i]):
            diff -= 1
            report_symbol_list.append('-')
        else :
            report_symbol_list.append('=')
        print(f"for i = {i}: {report_symbol_list}")
    
    if abs(diff) == len(liste_)-1:
        status = 'Passed A'
    else:
        status = 'Failed A'

    return [status, diff, report_symbol_list]

# print(reports[0].split())
# print(checkA(reports[0].split()))

def checkB(liste_):
    print(liste_)
    status = None
    index_ = 0
    for i in range(0, len(liste_)-1):
        calc = int(liste_[i+1]) - int(liste_[i])
        if abs(calc) >= 1 and abs(calc) <= 3:
            status = 'Passed B'
            index_ = -1
            # print(status)
        else :
            status = 'Failed B'
            index_ = i
            # print(status)
            break
    return [status, index_]

# print(checkB(reports[0].split()))

# 3. Check if the different reports are safe i.e
# Increment nb_reports_safe every time a safe report is found
nb_reports_safe = 0

for k, report in enumerate(reports):
    report_list = report.split()
    dampener = False
    print(f"report {k} : {report_list}")

    # print("go checkA")
    a_ = checkA(report_list) 
    # print(f"result for a: {a_}")

    status_a = a_[0] # renvoie le status
    status_a_final = None

    # print(f"count(set): {len(set(a_[2]))}")
    if status_a == 'Failed A': 
        if len(set(a_[2])) > 2 : # compare les symboles et continue si on a +, - et =
            continue # KO complet
        else:
            if a_[1] > 0: # there is a majority of +
            # if max(a_[2].count('+'), a_[2].count('-')) == a_[2].count('+'): 
                minority_count = max(a_[2].count('-'), a_[2].count('='))
            else: # there is a majority of -
                minority_count = max(a_[2].count('+'), a_[2].count('='))
            
            if minority_count > 1:
                continue # KO A car trop d'éléments différents
            else:
                dampener = True
                print("CAS : minority_count = 1") # branche où il y a tous les pb!!!
                if '=' in a_[2]:
                    status_a_final = 'Passed A' # cas A31
                    report_list.pop(a_[2].index('='))
                else: # il a juste un - ou + de différence
                    if a_[1] > 0: # il y a plus de + et donc il faut chercher le - intrus
                        index_a = a_[2].index('-')
                        print(f"index_a (-) = {index_a}")
                    else:
                        index_a = a_[2].index('+')
                        print(f"index_a (+) = {index_a}")
                        

                    if index_a == len(a_[2])-1 or index_a == 0 : # le - est en première ou dernière position
                        status_a_final = 'Passed A' # cas A32
                        if index_a == 0:
                            report_list.pop(0) # update report that will be checked by b
                        else:
                            report_list = report_list[:-1] # update report that will be checked by b
                    else : # on check si ça marche en enlevant un des 2 élements
                        report_dampened = report_list[:index_a] + report_list[index_a+1:]
                        if checkA(report_dampened)[0] == 'Failed A': # enlever l'autre élement autour du -
                            report_dampened_bis = report_list[:index_a+1] + report_list[index_a+2:]
                            status_a_final = checkA(report_dampened_bis)[0] # peut être cas A32 suite ou A33 KO
                            if status_a_final == 'Passed A':
                                report_list = report_dampened_bis
                            else:
                                continue # go to next report
                        else:
                            status_a_final = 'Passed A' # cas A32 suite
                            report_list = report_dampened
            
    else:
        status_a_final = 'Passed A'
    
    if status_a_final == 'Failed A':
        continue # go to next report
    else: # let's run the test for criteria B: cas A1 & A2 passent direct ici
        print(f"go checkB for : {report_list}")
        b_ = checkB(report_list)
        print(f"result for b: {b_}")

        status_b = b_[0] # renvoie le status
        status_b_final = None
        if status_b == 'Passed B': # report is SAFE!!!
            nb_reports_safe += 1
            print(f"report is SAFE!!! => nb_reports_safe = {nb_reports_safe}")
            continue # go to next report
        else: # checkB has returned 'Failed B"
            if dampener == True:
                status_b_final = 'Failed B'
                continue # cannot use dampener twice, go to next report
            else:
                if b_[1] == 0 or b_[1] == len(report_list) - 2:
                    status_b_final = 'Passed B'
                    nb_reports_safe += 1
                    print(f"report is SAFE!!! => nb_reports_safe = {nb_reports_safe}")
                    dampener = True
                else: # même si dampener pas utilisé, dans une liste strictement (dé)croissante, la distance sera trop élevée
                    continue # go to next report

print(nb_reports_safe)