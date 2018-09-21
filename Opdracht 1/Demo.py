def swapFS(lijst):
    if len(lijst) > 1:
        lijst[0], lijst[1] = lijst[1], lijst[0]

lijst = ['een', 'twee', 'drie']
swapFS(lijst)

print(lijst)