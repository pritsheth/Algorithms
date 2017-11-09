
# we can delete the best player and update the tournament tree in logn time.
#we just have to compute the all the parents of the best player till the root.
def deleteBestPlayerAndCreateTournamentTree(dict,dp,tree):
    bestPlayer = dp[0]
    index = dict[bestPlayer]
    # Seting the best player as -1 to delete it from the tournament tree
    dp[index] = -1
    parent = (index-1) //2
    # Arrange the match between player and store the winner
    while parent >= 0:
        dp[parent] = max(dp[2 * parent + 1], dp[2 * parent + 2])
        parent = (parent-1) //2
    print(dp)


def getSecondBestPlayer(tree):
    length = 2 * len(tree) - 1
    dp = [0] * length
    dict = {}

    index = len(tree) - 1
    print(index)

    # copy the team player value into the end of the tournament tree array!!
    for j in range(len(tree)):
        dp[index] = tree[j]
        dict[tree[j]] = index
        index += 1

    print(dp)
    i = len(tree) - 2

    # Arrange the match between player and store the winner
    while i >= 0:
        dp[i] = max(dp[2 * i + 1], dp[2 * i + 2])
        i = i - 1
    print(dp)
    deleteBestPlayerAndCreateTournamentTree(dict,dp,tree)



tree = [1, 2, 3, 4, 5]
getSecondBestPlayer(tree)
