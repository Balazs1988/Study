import random
import json
from datetime import datetime as dt


class Issue:
    def __init__(self, issue_id, author, description, date, state):
        self.issue_id = issue_id
        self.author = author
        self.description = description
        self.date = date
        self.state = state


class IssueTracker:
    issue_list = []


def collect_issue_by_state():
    issue_by_status = {}
    for i in IssueTracker.issue_list:
        if i.state in issue_by_status:
            values_list = list(issue_by_status[i.state])
            values_list.append(i.issue_id)
            issue_by_status[i.state] = values_list
        else:
            issue_by_status[i.state] = i.issue_id
    return issue_by_status


def register_issue(reg_id, reg_author, reg_description):
    curr_date = dt.today().strftime('%Y-%m-%d')
    state = 'open'
    curr_issue = Issue(reg_id, reg_author, reg_description, curr_date, state)
    IssueTracker.issue_list.append(curr_issue)


def reject_issue():
    for i in IssueTracker.issue_list:
        if i.state == 'open':
            print(f'Issue id: {i.issue_id}, Author: {i.author}, Description: {i.description}, Date: {i.date}')
            new_status = input('Reject this issue? (type "y" or "n") ')
            if new_status == 'y':
                i.state = 'rejected'


def solve_issue(solved_id):
    for i in IssueTracker.issue_list:
        if i.issue_id == solved_id:
            i.state = 'solved'


def select_random_issue():
    i = random.choice(IssueTracker.issue_list)
    print(f'Random issue id: {i.issue_id}, author: {i.author}, description: {i.description}, date: {i.date}, status: '
          f'{i.state}.')


def issues_report():
    open_status = 0
    rejected_status = 0
    solved_status = 0
    for i in IssueTracker.issue_list:
        if i.state == 'open':
            open_status += 1
        elif i.state == "rejected":
            rejected_status += 1
        elif i.state == 'solved':
            solved_status += 1
    print(f'Open: {open_status} issue(s), Rejected: {rejected_status} issue(s), Solved: {solved_status} issue(s).')


def save_data():
    issues_dict = {}
    for i in IssueTracker.issue_list:
        issues_dict['Id'] = i.issue_id
        issues_dict['Author'] = i.author
        issues_dict['Description'] = i.description
        issues_dict['Created date'] = i.date
        issues_dict["Status"] = i.state
        with open('issues_list.json', 'a') as json_file:
            json_file.write(json.dumps(issues_dict))
            json_file.write('\n')


def load_data():
    with open('issues_list.json') as json_file:
        issues_loaded_list = json_file.read().splitlines()
    print(issues_loaded_list)


register_issue('1', 'Peter', 'cant connect to the internet')
register_issue('2', 'Pete', 'google.com 404 code')
register_issue('3', 'Pet', 'cant find main.py on local machine')
register_issue('4', 'Pe', 'something big issue')

solve_issue('1')
print(collect_issue_by_state())
reject_issue()
print(collect_issue_by_state())
select_random_issue()
issues_report()
save_data()
load_data()
