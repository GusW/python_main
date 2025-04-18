# from functools import reduce

employees = [
    {"name": "Jane", "salary": 90000, "job_title": "developer"},
    {"name": "Bill", "salary": 50000, "job_title": "writer"},
    {"name": "Kathy", "salary": 120000, "job_title": "executive"},
    {"name": "Anna", "salary": 100000, "job_title": "developer"},
    {"name": "Dennis", "salary": 95000, "job_title": "developer"},
    {"name": "Albert", "salary": 70000, "job_title": "marketing specialist"},
]


def is_developer(employee):
    return employee.get("job_title") == "developer"


def is_not_developer(employee):
    return employee.get("job_title") != "developer"


# developers = list(filter(is_developer, employees))
# non_developers = list(filter(is_not_developer, employees))
developers = [e for e in employees if e.get("job_title") == "developer"]
non_developers = [e for e in employees if e.get("job_title") != "developer"]


def get_salary(employee):
    return employee.get("salary")


# developer_salaries = list(map(get_salary, developers))
# non_developer_salaries = list(map(get_salary, non_developers))
developer_salaries = [e.get("salary") for e in developers]
non_developer_salaries = [e.get("salary") for e in non_developers]


def get_sum(acc, x):
    return acc + x


# average_developer_salary = reduce(get_sum, developer_salaries) / len(developer_salaries)
# average_non_developer_salary = reduce(get_sum, non_developer_salaries) / len(
#     non_developer_salaries
# )
average_developer_salary = sum(developer_salaries) / len(developer_salaries)
average_non_developer_salary = sum(non_developer_salaries) / len(non_developer_salaries)


print(average_developer_salary)
print(average_non_developer_salary)
