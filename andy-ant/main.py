import hedron as Hedron
from simulation import Scenario

result = Scenario(Hedron.soccer_ball, 100000, 10000).run()
print(f"Average steps to return home: {result}")
