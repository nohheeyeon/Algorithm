correct_pieces = [1, 1, 2, 2, 2, 8]

found_pieces = list(map(int, input().split()))

needed_pieces = [correct - found for correct, found in zip(correct_pieces, found_pieces)]
print(" ".join(map(str, needed_pieces)))
