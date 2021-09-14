from a.utils import get_rounded_to_print


class LineSegment:
    def __init__(self, left: float, right: float):
        if right < left:
            raise ValueError("The beginning of a line segment cannot exceed its end.")

        self.left = left
        self.right = right

    @property
    def length(self):
        return self.right - self.left

    @property
    def center(self):
        return (self.right + self.left) / 2

    def to_str(self, print_accuracy=4):
        return (
            f"[{get_rounded_to_print(self.left, print_accuracy)}, {get_rounded_to_print(self.right, print_accuracy)}]"
        )

    def __str__(self):
        return self.to_str()

    def __repr__(self):
        return str(self)

    def copy(self):
        return LineSegment(self.left, self.right)
