"""Simple RAM simulation module.

Provides a RAM class that mimics byte addressable memory. The class
supports reading, writing, loading sequences of bytes and dumping
memory contents.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator, Tuple


@dataclass
class RAM:
    """A simple byte-addressable RAM simulator.

    Attributes
    ----------
    size: int
        The total number of addressable bytes.
    memory: list[int]
        Backing storage for the simulated memory.
    """

    size: int

    def __post_init__(self) -> None:
        if self.size <= 0:
            raise ValueError("RAM size must be positive")
        self.memory = [0] * self.size

    def _validate_address(self, address: int) -> None:
        if not 0 <= address < self.size:
            raise IndexError(f"Address {address} out of range")

    def read(self, address: int) -> int:
        """Read a single byte from memory."""
        self._validate_address(address)
        return self.memory[address]

    def write(self, address: int, value: int) -> None:
        """Write a single byte to memory."""
        self._validate_address(address)
        if not 0 <= value <= 0xFF:
            raise ValueError("Value must be between 0 and 255")
        self.memory[address] = value

    def load(self, data: Iterable[int], start_address: int = 0) -> None:
        """Load a sequence of bytes into memory starting at start_address."""
        for offset, byte in enumerate(data):
            self.write(start_address + offset, byte)

    def dump(self, start: int = 0, end: int | None = None) -> Iterator[Tuple[int, int]]:
        """Iterate over memory contents from ``start`` to ``end``.

        Yields tuples of ``(address, value)``.
        """
        if end is None:
            end = self.size
        for address in range(start, end):
            self._validate_address(address)
            yield address, self.memory[address]


def _demo() -> None:
    """Run a demonstration of the RAM simulator."""
    ram = RAM(16)
    ram.write(0, 10)
    ram.write(1, 20)
    print("Value at address 0:", ram.read(0))
    print("Value at address 1:", ram.read(1))
    print("\nMemory dump:")
    for addr, val in ram.dump():
        print(f"{addr:04d}: {val:02X}")


if __name__ == "__main__":
    _demo()
