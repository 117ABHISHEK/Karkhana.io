import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class MobiusStrip:
    def __init__(self, R, w, n):
        """
        Initialize the Möbius strip with given radius, width, and resolution.
        """
        self.R = R
        self.w = w
        self.n = n
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w / 2, w / 2, n)
        )
        self.x, self.y, self.z = self._compute_coordinates()

    def _compute_coordinates(self):
        """
        Compute the 3D coordinates (x, y, z) using the Möbius strip parametric equations.
        """
        u = self.u
        v = self.v
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def surface_area(self):
        """
        Approximate the surface area numerically using the magnitude of the cross product of partial derivatives.
        """
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)

        u = self.u
        v = self.v

        # Partial derivatives with respect to u
        ru_x = - (self.R + v * np.cos(u / 2)) * np.sin(u) - 0.5 * v * np.sin(u / 2) * np.cos(u)
        ru_y = (self.R + v * np.cos(u / 2)) * np.cos(u) - 0.5 * v * np.sin(u / 2) * np.sin(u)
        ru_z = 0.5 * v * np.cos(u / 2)

        # Partial derivatives with respect to v
        rv_x = np.cos(u / 2) * np.cos(u)
        rv_y = np.cos(u / 2) * np.sin(u)
        rv_z = np.sin(u / 2)

        # Cross product of ru and rv
        cross_x = ru_y * rv_z - ru_z * rv_y
        cross_y = ru_z * rv_x - ru_x * rv_z
        cross_z = ru_x * rv_y - ru_y * rv_x

        dA = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        surface_area = np.sum(dA) * du * dv
        return surface_area

    def edge_length(self):
        """
        Approximate the total length of both edges (v = ±w/2) numerically.
        """
        u = np.linspace(0, 2 * np.pi, self.n)
        v_pos = self.w / 2
        v_neg = -self.w / 2

        def edge_curve(v):
            x = (self.R + v * np.cos(u / 2)) * np.cos(u)
            y = (self.R + v * np.cos(u / 2)) * np.sin(u)
            z = v * np.sin(u / 2)
            return x, y, z

        x1, y1, z1 = edge_curve(v_pos)
        x2, y2, z2 = edge_curve(v_neg)

        def compute_length(x, y, z):
            dx = np.diff(x)
            dy = np.diff(y)
            dz = np.diff(z)
            return np.sum(np.sqrt(dx**2 + dy**2 + dz**2))

        return compute_length(x1, y1, z1) + compute_length(x2, y2, z2)

    def plot(self):
        """
        Plot the Möbius strip using matplotlib in 3D.
        """
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, color='cyan', edgecolor='k', alpha=0.8)
        ax.set_title("Mobius Strip")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Create an instance of MobiusStrip
    R=float(input())
    w=float(input()) 
    n=int(input())
    mobius = MobiusStrip(R,w,n)

    # Compute properties
    area = mobius.surface_area()
    length = mobius.edge_length()

    # Output results
    print(f"Surface Area ≈ {area:.4f}")
    print(f"Edge Length ≈ {length:.4f}")

    # Plot the strip
    mobius.plot()
