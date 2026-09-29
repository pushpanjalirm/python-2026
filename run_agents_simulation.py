"""
Agent Simulation Runner - Extract data without visualization delays
"""

import random
from collections import deque

# Grid environment for our vacuum cleaner
class Environment:
    def __init__(self, width=4, height=4, dirt_prob=0.3):
        self.width = width
        self.height = height
        self.grid = [[1 if random.random() < dirt_prob else 0 
                      for _ in range(width)] for _ in range(height)]
        self.agent_pos = (0, 0)

    def is_dirty(self, x, y):
        return self.grid[y][x] == 1

    def clean(self, x, y):
        self.grid[y][x] = 0


# Vacuum cleaner movement function
def move(action, env):
    x, y = env.agent_pos

    if action == "UP" and y > 0:
        env.agent_pos = (x, y - 1)
    elif action == "DOWN" and y < env.height - 1:
        env.agent_pos = (x, y + 1)
    elif action == "LEFT" and x > 0:
        env.agent_pos = (x - 1, y)
    elif action == "RIGHT" and x < env.width - 1:
        env.agent_pos = (x + 1, y)
    elif action == "CLEAN":
        env.clean(x, y)


# Simulation function (without visualization)
def run_simulation(agent_class, steps=30):
    env = Environment()
    agent = (
        agent_class(env.width, env.height)
        if agent_class in [ModelBasedAgent, GoalBasedAgent, UtilityBasedAgent]
        else agent_class()
    )

    score = 0

    for step in range(steps):
        x, y = env.agent_pos
        action = agent.choose_action((x, y), env)

        if action == "CLEAN" and env.is_dirty(x, y):
            score += 1

        move(action, env)

    return score


# Simple Reflex Agent
class SimpleReflexAgent:
    def choose_action(self, percept, env):
        x, y = percept
        if env.is_dirty(x, y):
            return "CLEAN"
        return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])


# Model-Based Reflex Agent
class ModelBasedAgent:
    def __init__(self, width, height):
        self.memory = [[None for _ in range(width)] for _ in range(height)]

    def choose_action(self, percept, env):
        x, y = percept
        # Update memory
        self.memory[y][x] = 1 if env.is_dirty(x, y) else 0

        if env.is_dirty(x, y):
            return "CLEAN"

        # Look for known dirty cells
        for j in range(env.height):
            for i in range(env.width):
                if self.memory[j][i] == 1:
                    if i > x: return "RIGHT"
                    if i < x: return "LEFT"
                    if j > y: return "DOWN"
                    if j < y: return "UP"

        return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])


# Goal-Based Agent (uses BFS)
class GoalBasedAgent:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.path = []

    def choose_action(self, percept, env):
        x, y = percept

        if env.is_dirty(x, y):
            return "CLEAN"

        # Follow planned path
        if self.path:
            return self.path.pop(0)

        # Find nearest dirty cell
        target = self.find_nearest_dirty(env, x, y)
        if target:
            self.path = self.plan_path((x, y), target)
            if self.path:
                return self.path.pop(0)

        return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def find_nearest_dirty(self, env, x, y):
        best = None
        best_dist = float('inf')

        for j in range(self.height):
            for i in range(self.width):
                if env.is_dirty(i, j):
                    d = abs(x - i) + abs(y - j)
                    if d < best_dist:
                        best_dist = d
                        best = (i, j)
        return best

    def plan_path(self, start, goal):
        queue = deque([(start, [])])
        visited = {start}

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == goal:
                return path

            for move, (dx, dy) in zip(
                ["UP", "DOWN", "LEFT", "RIGHT"],
                [(0, -1), (0, 1), (-1, 0), (1, 0)]
            ):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + [move]))

        return []


# Utility-Based Agent
class UtilityBasedAgent:
    def __init__(self, width, height, move_cost=0.01, clean_reward=1.0):
        self.width = width
        self.height = height
        self.move_cost = move_cost
        self.clean_reward = clean_reward

    def choose_action(self, percept, env):
        x, y = percept

        # If current cell is dirty, cleaning gives immediate reward
        if env.is_dirty(x, y):
            return "CLEAN"

        # Compute utility for each possible move
        utilities = {}

        moves = {
            "UP": (0, -1),
            "DOWN": (0, 1),
            "LEFT": (-1, 0),
            "RIGHT": (1, 0)
        }

        for action, (dx, dy) in moves.items():
            nx, ny = x + dx, y + dy

            # Invalid move gives negative utility
            if not (0 <= nx < self.width and 0 <= ny < self.height):
                utilities[action] = -999  # Very bad
                continue

            # Expected utility = movement cost + potential dirt reward
            reward = self.clean_reward if env.is_dirty(nx, ny) else 0
            utilities[action] = reward - self.move_cost

        # Choose best action
        return max(utilities, key=utilities.get)


# Run the simulations
def main():
    agents = [SimpleReflexAgent, ModelBasedAgent, GoalBasedAgent, UtilityBasedAgent]
    num_runs = 10  # Run each agent multiple times for reliability
    steps = 30

    print(f"Running {num_runs} simulations of {steps} steps per agent...")
    print()

    results = {}
    for agent_class in agents:
        scores = []
        for run in range(num_runs):
            score = run_simulation(agent_class, steps=steps)
            scores.append(score)

        avg_score = sum(scores) / len(scores)
        results[agent_class.__name__] = {
            'scores': scores,
            'average': avg_score,
            'min': min(scores),
            'max': max(scores)
        }

    # Print results table
    print("=" * 80)
    print(f"{'Agent Type':<25} {'Average Score':<15} {'Min':<8} {'Max':<8} {'Std Dev':<10}")
    print("=" * 80)

    for agent_name in ['SimpleReflexAgent', 'ModelBasedAgent', 'GoalBasedAgent', 'UtilityBasedAgent']:
        data = results[agent_name]
        avg = data['average']
        min_s = data['min']
        max_s = data['max']

        # Calculate standard deviation
        variance = sum((x - avg) ** 2 for x in data['scores']) / len(data['scores'])
        std_dev = variance ** 0.5

        print(f"{agent_name:<25} {avg:<15.2f} {min_s:<8} {max_s:<8} {std_dev:<10.2f}")

    print("=" * 80)
    print()

    # Print individual run data
    print("Individual Run Scores (10 runs, 30 steps each):")
    print()
    for agent_name in ['SimpleReflexAgent', 'ModelBasedAgent', 'GoalBasedAgent', 'UtilityBasedAgent']:
        data = results[agent_name]
        print(f"{agent_name}: {data['scores']}")

    print()
    print("Summary Table for Lab Report:")
    print("-" * 50)
    print(f"{'Agent Type':<25} {'Number of Cells Cleaned':<25}")
    print("-" * 50)
    for agent_name in ['SimpleReflexAgent', 'ModelBasedAgent', 'GoalBasedAgent', 'UtilityBasedAgent']:
        data = results[agent_name]
        print(f"{agent_name:<25} {data['average']:<25.1f}")
    print("-" * 50)


if __name__ == "__main__":
    main()
