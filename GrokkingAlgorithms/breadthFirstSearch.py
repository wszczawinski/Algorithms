from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["ann", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thomas", "johnny"]
graph["ann"] = []
graph["peggy"] = []
graph["thomas"] = []
graph["johnny"] = []

print(f"Initial graph: {graph} \n")


def person_is_seller(name):
    return name[-1] == "s"


def find_seller(name):
    searched = []
    search_queue = deque()
    search_queue += graph[name]
    print(f"Initial queue: {search_queue} \n")

    while search_queue:
        person = search_queue.popleft()

        print(f"Current person: {person}")
        print(f"Current queue: {search_queue}")
        print(f"Already searched: {searched} \n")

        if not person in searched:

            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


find_seller("you")
