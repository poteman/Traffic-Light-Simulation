from Environment import Environment

environment = Environment(0)

# Testing route generation
routes = environment.generateRoutes()
print(routes)

for time in range(100):
    environment.update(time)
