from queens import Queens


def main():
    size = 8
    queens = Queens(8)
    bfs_solutions = queens.solve_bfs()
    for i, solution in enumerate(bfs_solutions):
            print('BFS Solution %d:' % (i + 1))
            queens.print(solution)
    print('Total BFS solutions: %d' % len(bfs_solutions))


if __name__ == '__main__':
    main()