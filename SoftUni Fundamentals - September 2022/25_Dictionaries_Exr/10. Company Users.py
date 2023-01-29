companies = {}
while True:
    list_of_info = input()
    if list_of_info == "End":
        break
    company_name, employee = list_of_info.split(" -> ")
    if company_name not in companies:
        companies[company_name] = []
        if employee not in companies[company_name]:
            companies[company_name].append(employee)
    else:
        if employee not in companies[company_name]:
            companies[company_name].append(employee)
for c_name, employees in companies.items():
    print(c_name)
    for empl in employees:
        print(f"-- {empl}")

