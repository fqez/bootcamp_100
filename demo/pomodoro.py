from typing import Dict, List, Union


class Pomodoro:
    """
    A class representing a Pomodoro timer.
    """

    def __init__(self) -> None:
        """
        Initialize the Pomodoro timer.
        """
        self.intervals: Dict[str, List[Union[int, str]]] = {
            "working": [25, "Working 😒\n{1} of {4}"],
            "short_break": [5, "Short Break😎\n{1} of {4}"],
            "long_break": [15, "Long Break😎\n{1} of {4}"],
        }

        self.current_interval: str = ""
        self.interval_count: int = 0
        self.total_pomodoros: int = 0

    def next_segment(self) -> Union[List[Union[int, str]], None]:
        """
        Move to the next segment of the Pomodoro timer.

        Returns:
            The next interval as a list [interval_id, interval_name], or None if the interval is not found.
        """
        if not self.current_interval:  # startup
            self.current_interval = "working"
        elif self.current_interval == "working" and self.interval_count >= 3:
            self.current_interval = "long_break"

        elif self.current_interval == "working" and self.interval_count < 3:
            self.current_interval = "short_break"

        elif self.current_interval == "short_break":
            self.interval_count += 1
            self.current_interval = "working"

        elif self.current_interval == "long_break":
            self.total_pomodoros += 1
            self.interval_count = 0
            self.current_interval = "working"

        return self.intervals.get(self.current_interval)
