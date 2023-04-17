import random 

from unified_planning.shortcuts import *
from unified_planning.io import PDDLWriter


def main():

    # Types
    Drone = UserType('Drone')
    Location = UserType("Location")
    Good = UserType("Good")
    Sugar = UserType("Sugar", father=Good)
    Milk = UserType("Milk", father=Good)
    House = UserType('House', father=Location)
    Shop = UserType("Shop", father=Location)

    # Agents
    At = Fluent("At", BoolType(), drone=Drone, locaiton=Location)
    Holds = Fluent("Holds", BoolType(), drone=Drone, good=Good)
    Free = Fluent("Free", BoolType(), drone=Drone)
    Requires = Fluent("Requires", BoolType(), house = House, good = Good)
    Adj = Fluent("Adjacent", BoolType(), l1 = Location, l2 = Location)
    Sells = Fluent("Sells", BoolType(), shop=Shop, good=Good)

    # Fly from - to
    fly = InstantaneousAction("fly", d=Drone, li=Location, lf=Location)
    d = fly.parameter("d")
    li = fly.parameter("li")
    lf = fly.parameter("lf")
    fly.add_precondition(At(d, li))
    fly.add_precondition(Not(At(d, lf)))
    fly.add_precondition(Adj(li, lf))
    fly.add_effect(At(d, lf), True)
    fly.add_effect(At(d, li), False)

    # Take good from the shop
    take = InstantaneousAction("take", d=Drone, g=Good, s=Shop)
    d = take.parameter("d")
    g = take.parameter("g")
    s = take.parameter("s")
    take.add_precondition(At(d, s))
    take.add_precondition(Free(d))
    take.add_precondition(Not(Holds(d, g)))
    take.add_precondition(Sells(s, g))
    take.add_effect(Holds(d, g), True)
    take.add_effect(Free(d), False)

    # Leave good
    leave = InstantaneousAction("leave", d=Drone, g=Good, h=House)
    d = leave.parameter("d")
    g = leave.parameter("g")
    h = leave.parameter("h")
    leave.add_precondition(At(d, h))
    leave.add_precondition(Not(Free(d)))
    leave.add_precondition(Holds(d, g))
    leave.add_precondition(Requires(h, g))
    leave.add_effect(Holds(d, g), False)
    leave.add_effect(Requires(h, g), False)
    leave.add_effect(Free(d), True)


    # Objects
    drones = [Object(f"D{i}", Drone) for i in range(1,4)]
    houses = [Object(f"H{i}", House) for i in range(1,10)]
    shops = [Object(f"S{i}", Shop) for i in range(1,3)]
    sugar = Object("sugar", Sugar)
    milk = Object("milk", Milk)


    # Problem Constants
    NUM_HOUSES = 9
    NUM_DRONES = 3
    NUM_SHOPS = 2

    # Problem
    drones_problem = Problem("drones")
    drones_problem.add_objects(drones)
    drones_problem.add_objects(houses)
    drones_problem.add_objects(shops)
    drones_problem.add_objects([sugar, milk])
    drones_problem.add_fluent(At, default_initial_value=False)
    drones_problem.add_fluent(Holds, default_initial_value=False)
    drones_problem.add_fluent(Free, default_initial_value=True)
    drones_problem.add_fluent(Requires, default_initial_value=False)
    drones_problem.add_fluent(Adj, default_initial_value=False)
    drones_problem.add_fluent(Sells, default_initial_value=False)
    drones_problem.add_action(fly)
    drones_problem.add_action(take)
    drones_problem.add_action(leave)

    # Random Drones Initial Position
    print('\n\n-------------------------------\n')
    print('DRONES INITIAL POSITIONS')
    for i in range(NUM_DRONES):
        if random.randint(0,1) == 0:
            rand_idx = random.randint(0, NUM_HOUSES-1)
            loc = 'House'
            drones_problem.set_initial_value(At(drones[i], houses[rand_idx]), True)
        else: 
            rand_idx = random.randint(0, NUM_SHOPS-1)
            loc = 'Shop'
            drones_problem.set_initial_value(At(drones[i], shops[rand_idx]), True)
        
        print('Drone {}: {} {}'.format(i, loc, rand_idx))
    print('\n-------------------------------\n\n')

    # Requests
    drones_problem.set_initial_value(Requires(houses[2], milk), True)
    drones_problem.set_initial_value(Requires(houses[7], sugar), True)
    drones_problem.set_initial_value(Requires(houses[6], milk), True)
    drones_problem.set_initial_value(Requires(houses[6], sugar), True)

    # Sells
    drones_problem.set_initial_value(Sells(shops[0], sugar), True)
    drones_problem.set_initial_value(Sells(shops[1], milk), True)

    # Adjacences
    adjs = {'H1': ['S1'], 'H2': ['S1'], 'H3': ['H5'], 'H4': ['H5', 'H7'], 'H5': ['S1', 'H3', 'H4', 'H8'], 'H6': ['H8'], 'H7': ['H4', 'S2'], 'H8': ['H5', 'H6', 'H9', 'W2'], 'H9': ['H9'], 'S1':['H1', 'H2', 'H5'], 'S2': ['H8', 'H7']}
    locs = [i for i in houses]
    locs.extend(shops)
    for l1 in locs: 
        for l2 in locs:
            if l2.name in adjs[l1.name]:
                drones_problem.set_initial_value(Adj(l1, l2), True)

    # Goal - All houses without requests
    for house in houses: 
        for good in [milk, sugar]:
            drones_problem.add_goal(Not(Requires(house, good)))
    
    # Generating PDDL files
    w = PDDLWriter(drones_problem)
    w.write_domain('drones_problem/domain.pddl')
    w.write_problem('drones_problem/problem.pddl')

    # Solving the problem
    up.shortcuts.get_env().credits_stream = None
    with OneshotPlanner(name='fast-downward-opt') as planner: 
        result = planner.solve(drones_problem)
        plan = result.plan
        if plan is not None:
            print("SOLUTION:")
            for a in plan.actions: 
                print('\t{}'.format(a))
        else: 
            print("COULDN'T FIND A PLAN FOR THE PROBLEM\n\n")
        
        print('\n-------------------------------\n\n')
    
    return

            

if __name__ == '__main__': 
    main()











