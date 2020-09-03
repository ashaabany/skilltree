from graph import Graph

# a job has a description and a weight (but ignore weights i was just messing round)


class Job:

    def __init__(self, data):
        self.data = data
        self.weight = 0
        self.child = None

    def show_tree(self):
        print(self.data)

# a person has a name and a list of jobs they've had


class Person:
    def __init__(self, name):
        self.name = name
        self.job = []

    def add_job(self, x):
        self.job.append(x)


root = Job("hello")
root.show_tree()

job_list = []

Thomas = Person("Thomas")
Thomas.add_job("Crier")
Thomas.add_job("Chicken Eater")

Kyle = Person("Kyle")
Kyle.add_job("Jumper")
Kyle.add_job("Data Analyst")


Jeff = Person("Jeff")
Jeff.add_job("Crier")
Jeff.add_job("Soldier")

# ecosystem represents all the people in our network that we're getting data from, for this model
ecosystem = [Thomas, Kyle, Jeff]

# this graph represents all the jobs in our network
graph = Graph()

# update function makes it so given an ecosystem of people, take all the jobs and put in the graph,
# unless the job already exists in graph. if a person had 2 jobs, a connection will be made in the
# graph between the two jobs.


def update():
    for person in ecosystem:
        for a in person.job:
            if a in job_list:
                continue
            else:
                job_list.append(a)
    for x in job_list:
        graph.add_vertex(x)
    for person in ecosystem:
        if len(person.job) > 1:
            graph.add_edge({person.job[0], person.job[1]})


def show_graph():
    for x in graph.vertices():
        x.show_tree()


update()
print(graph.vertices())
print(graph.edges())


# ASSUMPTIONS: We're assuming for this model that people can only have up to 2 jobs (this is just cause of
# my pure laziness). U can print graph vertices to see all jobs in our network, and edges to see our connections.
# My latest thing is trying to mess with the graph.py edges section to see if i can add weights to the edges
# based on frequency, to simulate a neural network.