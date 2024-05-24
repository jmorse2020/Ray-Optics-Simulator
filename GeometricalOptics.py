import numpy as np
import math

class OpticalElement():
    def __init__(self, center, angle):
        self.center = center
        self.angle = -1*np.deg2rad(angle) # pass angle in degrees, convert to radians for calculations

class Lens(OpticalElement):
    def __init__(self, center, angle, radius_1, radius_2, diameter, index):
        super().__init__(center, angle)
        self.radius_1 = radius_1
        self.radius_2 = radius_2
        self.diameter = diameter
        self.index = index
        self.surface_1 = Lens.lens_surface(self, self.radius_1)
        self.surface_2 = Lens.lens_surface(self, self.radius_2)

    def lens_surface(self, radius):
        theta = math.asin((self.diameter / 2) / radius)
        r_prime = radius * math.cos(theta)
        delta_x = r_prime * math.cos(self.angle)
        delta_y = r_prime * math.sin(self.angle)
        gamma = theta - self.angle
        if radius > 0:
            start_angle = -1*gamma
            end_angle = (2*theta-gamma)
        elif radius < 0:
            start_angle = 1*(2*theta-gamma)
            end_angle = -1*gamma
        center = (self.center[0] - delta_x, self.center[1] - delta_y)
        return Arc(center=center, radius=radius, start_angle=start_angle, end_angle=end_angle)

    def draw_lens(self, ax):
        import matplotlib.patches as patches
        # Unpack the arc parameters
        ax.plot(self.center[0], self.center[1], marker='x', color='green')
        for arc in [self.surface_1, self.surface_2]:
            center, radius, start_angle, end_angle = arc.center, arc.radius, arc.start_angle, arc.end_angle
            
            # Create the arc patch
            arc_patch = patches.Arc(center, 2*radius, 2*radius, angle=0, theta1=np.rad2deg(start_angle), theta2=np.rad2deg(end_angle), edgecolor='b')
            
            # Add the arc to the axis
            ax.add_patch(arc_patch)
            
            # Plot the center of the arc
            ax.plot(center[0], center[1], 'ro')  # Center point
            
            # Set the aspect of the plot to be equal
            # ax.set_aspect('equal')
            


    def details(self):
        print(f"Optical element type: Lens\nPosition: {self.position}\nOrientation: {self.orientation}")


class Arc:
    def __init__(self, center, radius, start_angle, end_angle):
        self.center = center
        self.radius = radius
        self.start_angle = start_angle
        self.end_angle = end_angle

    