from __future__ import annotations
from concurrent.futures import ProcessPoolExecutor
from typing import Callable
from andy import Andy
from face import Face


def _run_one(args: tuple[Callable[[], Face], int]) -> int:
    face_generator, max_step_count = args
    return Andy(face_generator()).wander_until_back(max_step_count)


class Scenario:
    def __init__(
        self,
        face_generator: Callable[[], Face],
        sim_count: int,
        max_step_count: int
    ) -> None:
        self.sim_count = sim_count
        self.max_step_count = max_step_count
        self.face_generator = face_generator

    def run(self) -> float:
        args = [(self.face_generator, self.max_step_count)] * self.sim_count
        with ProcessPoolExecutor() as executor:
            move_counts = list(executor.map(_run_one, args))
        return sum(move_counts) / float(self.sim_count)
