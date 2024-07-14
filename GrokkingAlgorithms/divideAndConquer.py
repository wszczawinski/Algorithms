def divideFarmInfoSquarePlots(x, y):
    big = max(x, y)
    small = min(x, y)
    print("Current Euclid's farmland to be split:", big, "x", small)

    if big % small == 0:
        return small
    else:
        return divideFarmInfoSquarePlots(small, big % small)


farmDimensions = [1680, 640]

print(
    f"\nBiggest possible square plots to divide Euclid's field of size {farmDimensions[0]}x{farmDimensions[1]}: ",
    divideFarmInfoSquarePlots(farmDimensions[0], farmDimensions[1]),
)
