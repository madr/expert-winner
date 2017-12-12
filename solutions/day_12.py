from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '12.txt'
    seen = []

    def __str__(self):
        return 'Day 12: Digital Plumber'

    def _walk(self, i, programs):
        piped = programs[i].split()[2:]
        self.seen.append(i)
        for p in [int(p.replace(',', '')) for p in piped]:
            if p not in self.seen:
                self._walk(p, programs)

    def solve(self, puzzle_input):
        programs = puzzle_input.splitlines()
        self.seen = []
        self._walk(0, programs)
        return len(self.seen)

    def solve_again(self, puzzle_input):
        programs = puzzle_input.splitlines()
        self.seen = []
        groups = 0
        for pid, line in enumerate(programs):
            if pid not in self.seen:
                self._walk(pid, programs)
                groups += 1
        return groups


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
