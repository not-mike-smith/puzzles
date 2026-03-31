from __future__ import annotations


class Face:
    def __init__(self, name: str) -> None:
        self.name = name
        self._adjacent: list[Face] = []

    def touch(self, face: Face) -> Face:
        """Register that two faces share an edge. Both faces are updated.
        Returns face param to allow chaining: home.touch(side1).touch(side2)."""
        if face not in self._adjacent:
            self._adjacent.append(face)
            face._adjacent.append(self)
        return face

    def pick_adjacent_face(self, random_number: float) -> Face:
        return self._adjacent[int(random_number * len(self._adjacent))]
