from unified_planning.shortcuts import *
from unified_planning.io import PDDLWriter

# Objects
Apple = UserType("Apple")
Robot = UserType("Robot")
Location = UserType("Location")

# Agents
At = Fluent("At", BoolType(), robot=Robot, locaiton=Location)
On = Fluent("On", BoolType(), apple=Apple, location=Location)
Holding = Fluent("Holding", BoolType(), robot=Robot, apple=Apple)

# Move Action
move = InstantaneousAction("move", r=Robot, fl=Location, tl=Location)
fl = move.parameter("fl")
tl = move.parameter("tl")
r = move.parameter("r")
move.add_precondition(At(r, fl))
move.add_precondition(Not(At(r, fl)))
move.add_effect(At(r, fl), True)
move.add_effect(At(r, tl), False)

# Pick Action
pick = InstantaneousAction("pick", r=Robot, a=Apple, loc=Location)
loc = pick.parameter("loc")
a = pick.parameter("a")
r = pick.parameter("r")
pick.add_precondition(At(r, loc))
pick.add_precondition(On(a, loc))
pick.add_precondition(Not(Holding(r, a)))
pick.add_effect(Holding(r, a), True)
pick.add_effect(On(a, loc), False)

# Place Action
place = InstantaneousAction("place", r=Robot, a=Apple, loc=Location)
loc = place.parameter("loc")
a = place.parameter("a")
r = place.parameter("r")
place.add_precondition(Holding(r, a))
place.add_precondition(At(r, loc))
place.add_effect(Holding(r, a), False)
place.add_effect(On(a, loc), True)


# Defining the Problem
problem_1 = Problem("1")

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







