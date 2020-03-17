import infomap


def infomap_function(distances, ctys):
    
    # Command line flags can be added as a string to Infomap
    myInfomap = infomap.Infomap("--two-level --directed")  # Assuming undirected links and two-level map equation
    # to recursively search for multilevel solutions.

    # Access the default network to add links programmatically
    network = myInfomap.network()

    i = 0

    while i < len(list(ctys)):

        j = 0

        while j <= i:
            network.addLink(i, j, distances[list(ctys)[i]][list(ctys)[j]])
            j = j + 1

        i = i + 1

    # Run the Infomap search algorithm to find optimal modules
    myInfomap.run()

    # print("Found {} modules with codelength: {}".format(myInfomap.numTopModules(), myInfomap.codelength()))
    # print("Result")
    # print("\n#node module")

    ingredientModules = []

    for node in myInfomap.iterTree():
        if node.isLeaf():
            # print("{} {}".format(node.physicalId, node.moduleIndex()))
            ingredientModules.append(node.moduleIndex())

    return ingredientModules
