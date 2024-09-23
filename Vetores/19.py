def funcao(x1, x2):
    mist = [None] * (len(x1) + len(x2))

    for i in range(5):
        mist[2 * i] = x1[i]
        mist[2 * i + 1] = x2[i]

    return mist
