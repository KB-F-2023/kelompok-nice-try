import random

# Constants
BOARD_SIZE = 8
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
GENERATIONS = 1000

# Function to create an initial random population of chess boards


def create_population(size):
    population = []
    for i in range(size):
        board = []
        for j in range(BOARD_SIZE):
            board.append(random.randint(0, BOARD_SIZE-1))
        population.append(board)
    return population

# Function to calculate the fitness of each individual in the population


def calculate_fitness(board):
    conflicts = 0
    for i in range(BOARD_SIZE):
        for j in range(i+1, BOARD_SIZE):
            if board[i] == board[j]:
                conflicts += 1
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return 1 / (conflicts + 1)

# Function to select parents from the population


def select_parents(population):
    fitnesses = [calculate_fitness(board) for board in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness / total_fitness for fitness in fitnesses]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents

# Function to create a child board by combining the genes of two parent boards


def create_child(parents):
    split_point = random.randint(1, BOARD_SIZE-2)
    child = parents[0][:split_point] + parents[1][split_point:]
    return child

# Function to mutate a board by randomly changing one of its genes


def mutate(board):
    if random.random() < MUTATION_RATE:
        gene_to_change = random.randint(0, BOARD_SIZE-1)
        new_gene = random.randint(0, BOARD_SIZE-1)
        board[gene_to_change] = new_gene

# Function to evolve the population by selecting parents, creating children, and mutating them


def evolve(population):
    new_population = []
    for i in range(POPULATION_SIZE):
        parents = select_parents(population)
        child = create_child(parents)
        mutate(child)
        new_population.append(child)
    return new_population

# Function to check if a board is a valid solution to the puzzle


def is_valid(board):
    conflicts = 0
    for i in range(BOARD_SIZE):
        for j in range(i+1, BOARD_SIZE):
            if board[i] == board[j]:
                conflicts += 1
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts == 0

# Main function to run the genetic algorithm


def solve():
    population = create_population(POPULATION_SIZE)
    for generation in range(GENERATIONS):
        population = evolve(population)
        best_board = None
        best_fitness = 0
        for board in population:
            fitness = calculate_fitness(board)
            if fitness > best_fitness:
                best_board = board
                best_fitness = fitness
        print(
            f"Generation {generation+1}: Best solution {best_board} with fitness {best_fitness}")
        if is_valid(best_board):
            return best_board
    return None


# Example usage
solution = solve()
if solution:
    print("Found solution:", solution)
else:
    print("Could not find a solution.")
