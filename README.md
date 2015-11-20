# Roster-matching-project
Scope of project: a web application wherein ...
* employees input their schedules
* can query DOs (day off) of their colleagues 

Current state:
* prototyping

functions.py (goal: a working parser):
* program stucture and data flow 
 1) a dictionary is created wherein keys represent all dates in a month
 2) parser() returns a list of dates when this particular employee has off days
 3) all dictionary value the key of which matches dates from that list are appended with employee id
