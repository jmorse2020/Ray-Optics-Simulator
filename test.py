import GeometricalOptics as go
import matplotlib.pyplot as plt
lens1 = go.Lens((0,0), 0, 1, -1, 0.8, 1)
# lens1.radius_1 = 1
# lens1.radius_2 = -1
# lens1.diameter = 0.6
# lens1.index = 1
print(lens1.surface_1.center)
fig, ax = plt.subplots()
lens1.draw_lens(ax)
ax.set_xlim([-1.5,1.5])
ax.set_ylim([-1,1])
plt.show()