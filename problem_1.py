from unified_planning.shortcuts import *
from unified_planning.io import PDDLWriter

# Types
Apple = UserType("Apple")
Robot = UserType("Robot")
Location = UserType("Location")

# Fluents
At = Fluent("At", BoolType(), robot=Robot, locaiton=Location)
On = Fluent("On", BoolType(), apple=Apple, location=Location)
Holding = Fluent("Holding", BoolType(), robot=Robot, apple=Apple)

# Move Action
move = InstantaneousAction("move", r=Robot, l_from=Location, l_to=Location)
l_from = move.parameter("l_from")
l_to = move.parameter("l_to")
r = move.parameter("r")
move.add_precondition(At(r, l_from))
move.add_precondition(Not(At(r, l_to)))
move.add_effect(At(r, l_from), False)
move.add_effect(At(r, l_to), True)

# Pick Action
pick = InstantaneousAction("pick", a=Apple, r=Robot, loc=Location)
loc = pick.parameter("loc")
a = pick.parameter("a")
r = pick.parameter("r")
pick.add_precondition(At(r, loc))
pick.add_precondition(On(a, loc))
pick.add_precondition(Not(Holding(r, a)))
pick.add_effect(Holding(r, a), True)
pick.add_effect(On(a, loc), False)

# Place Action
place = InstantaneousAction("place", a=Apple, r=Robot, l=Location)
a = place.parameter("a")
r = place.parameter("r")
l = place.parameter("l")
place.add_precondition(Holding(r, a))
place.add_precondition(At(r, l))
place.add_precondition(Not(On(a, l)))
place.add_effect(On(a, l), True)
place.add_effect(Holding(r, a), False)


# Defining the Problem
problem_1 = Problem("problem_1")

robot0 = Object("robot0", Robot)
apple0 = Object("apple0", Apple)
shelf = Object("shelf", Location)
table = Object("table", Location)

problem_1.add_objects([robot0, apple0, shelf, table])
problem_1.add_fluent(At, default_initial_value=False)
problem_1.add_fluent(On, default_initial_value=False)
problem_1.add_fluent(Holding, default_initial_value=False)
problem_1.add_action(move)
problem_1.add_action(pick)
problem_1.add_action(place)

# Initial State
problem_1.set_initial_value(At(robot0, table), True)
problem_1.set_initial_value(On(apple0, shelf), True)

# Goal
problem_1.add_goal(On(apple0, table))

# Generate PDDL Files
w = PDDLWriter(problem_1)
w.write_domain('problem_1/domain.pddl')
w.write_problem('problem_1/problem.pddl')


# Solver
up.shortcuts.get_env().credits_stream = None
FD_Planner = OneshotPlanner(name='fast-downward')
result_1 = FD_Planner.solve(problem_1)
plan_1 = result_1.plan

for a in plan_1.actions:
    print(a)
