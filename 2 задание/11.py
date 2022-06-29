print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                F = b <= (a and c or d and (not a))
                if not F:
                    print(a, b, c, d)ц