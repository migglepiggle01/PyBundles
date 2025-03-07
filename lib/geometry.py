import math

class Plane2D:
    def __init__(self, name="Plane"):
        self.name = name
        self.shapes = []  # A list to hold shapes

    def add_shape(self, shape):
        self.shapes.append(shape)

    def output(self):
        plane_info = {"plane_name": self.name, "shapes": []}
        for shape in self.shapes:
            # Adding detailed properties of each shape
            plane_info["shapes"].append(str(shape))
        return plane_info

class Geometry2D:
    class Triangle:
        def __init__(self, p1, p2, p3, new_plane=True, calculate_angles=True, validate_triangle=True, **kwargs):
            self.p1 = p1  # Vertex 1 (x1, y1)
            self.p2 = p2  # Vertex 2 (x2, y2)
            self.p3 = p3  # Vertex 3 (x3, y3)

            self.a = None  # Side length opposite to vertex p1
            self.b = None  # Side length opposite to vertex p2
            self.c = None  # Side length opposite to vertex p3

            self.angles = None
            self.is_valid = None

            # Create a new plane if new_plane is True
            self.plane = None
            if new_plane:
                self.plane = Plane2D()
                self.plane.add_shape(self)

            # Calculate side lengths
            self.calculate_side_lengths()

            # Calculate angles if calculate_angles is True
            if calculate_angles:
                self.calculate_angles()

            # Validate triangle if validate_triangle is True
            if validate_triangle:
                self.validate_triangle()

        def calculate_side_lengths(self):
            # Calculate distances between points (side lengths)
            self.a = self._distance(self.p2, self.p3)  # side opposite to vertex p1
            self.b = self._distance(self.p1, self.p3)  # side opposite to vertex p2
            self.c = self._distance(self.p1, self.p2)  # side opposite to vertex p3

        def calculate_angles(self):
            # Using the law of cosines to calculate angles
            angle_A = math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
            angle_B = math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c))
            angle_C = math.acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b))

            self.angles = {
                "angle_A": math.degrees(angle_A),
                "angle_B": math.degrees(angle_B),
                "angle_C": math.degrees(angle_C),
            }

        def validate_triangle(self):
            # Using the triangle inequality theorem to check if the triangle is valid
            if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
                self.is_valid = True
            else:
                self.is_valid = False

        def _distance(self, p1, p2):
            # Calculate the distance between two points (p1, p2)
            return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

        def __str__(self):
            # Provide a human-readable description of the triangle
            return (
                f"Triangle with vertices: {self.p1}, {self.p2}, {self.p3}\n"
                f"Side lengths: {self.a:.2f}, {self.b:.2f}, {self.c:.2f}\n"
                f"Angles: Angle A: {self.angles['angle_A']:.2f}°, "
                f"Angle B: {self.angles['angle_B']:.2f}°, "
                f"Angle C: {self.angles['angle_C']:.2f}°\n"
                f"Valid: {'Yes' if self.is_valid else 'No'}"
            )