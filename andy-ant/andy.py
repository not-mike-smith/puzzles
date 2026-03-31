from __future__ import annotations
from face import Face
import random


class Andy:
    def __init__(self, initial_face: Face) -> None:
        self.initial_face = initial_face
        self.current_face = initial_face
        self.move_count = 0
        self._rng = random.Random()

    # get random float [0 1)
    def get_random_float(self) -> float:
        return self._rng.random()

    def move(self) -> None:
        self.current_face = self.current_face.pick_adjacent_face(
            self.get_random_float()
        )
        self.move_count += 1

    def wander_until_back(self, max_move_count) -> int:
        self.move()
        while (self.move_count < max_move_count
               and self.current_face is not self.initial_face):
            self.move()

        return self.move_count
