def ucs(start_state,goal_state):
    frontier = PriorityQueue()
    node = Node(start_state,None,None,0)
    frontier.push(node,0)
    reached = dict()
    reached[start_state] = node
    num_generated = 0
    while not frontier.is_empty():
        node = frontier.pop()
        if node.state == goal_state:
            return solution(node),num_generated
        for successor,action,step_cost in node.state.successors():
            num_generated+=1
            path_cost = node.cost+step_cost
            if successor not in reached or path_cost < reached[successor].cost:
                child_node= Node(successor,node,action,path_cost)
                reached[successor]=child_node
                frointer.push(child_node,path_cost)
    return None,num_generated
solution_path,N = ucs(start_state,goal_state)
print(f'number of generated node : {N}')
show_solution(start_state,solution_path,ncols=6)
