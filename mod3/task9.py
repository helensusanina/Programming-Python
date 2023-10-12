def SpiralMove(n):
    x, y = 0, 0
    dx, dy = -1, 0
    step = 1
    for i in range(n):
        for j in range(2):
            for k in range(step):
                x += dx
                y += dy
                n -= 1
                if n != 0:
                    dx, dy = -dy, dx
                    continue
                return x, y
        step += 1
    return x, y


x, y = SpiralMove(int(input()))
print(x, y)
