from random import sample

population = range(1, 101)
# will run only when ask for, lazy operation
lists = [sample(population, 15) for _ in range(3)]
i = 1
for l in lists:
    print(f"l{i},start={l}")
    l.sort(reverse=True)
    print(f"l{i},sorted={l}")
    del l[5:]
    print(f"l{i},truncated={l}")
    i += 1
