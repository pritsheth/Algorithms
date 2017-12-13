class PrimeNumbers:
    def getAllPrimes(self, n):
        sieves = [True] * (n + 1)

        for i in range(2, n + 1):
            if i * i > n:
                break

            if sieves[i]:
                for j in range(i + i, n + 1, i):
                    sieves[j] = False

        for i in range(2, n + 1):
            if sieves[i]:
                print(i)


pn = PrimeNumbers()
pn.getAllPrimes(29)
