"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")



state_order = ["red", "red_amber", "green", "amber"]
current_index = 0
state_time = 0

for _ in range(maxtime):
    state_time += 1
    if state_time == states[state]:
        current_index = (current_index + 1) % len(state_order)
        state = state_order[current_index]
        state_time = 0
    systime += 1
    print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14