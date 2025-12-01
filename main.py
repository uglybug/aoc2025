import requests
from dotenv import load_dotenv
import os

load_dotenv()
SESSION = os.getenv("SESSION")


def day1(part=1):
    input = requests.get(
        "https://adventofcode.com/2025/day/1/input",
        cookies={"session": SESSION},
        verify=False,
    ).text.split("\n")[:-1]

    # input = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

    dial = 50
    answer = 0
    times_through = 0

    for move in input:
        direction = move[0]
        distance = int(move[1:])
        times_through = 0

        msg = f"The dial is rotated {move}"

        if direction == "R":
            dial += distance
            times_through = dial // 100
        elif direction == "L":
            dial -= distance
            times_through = dial // -100
            if dial + distance != 0:
                times_through += 1

        if dial < 0 or dial > 99:
            dial = dial % 100

        msg += f" to point to {dial}."

        if dial == 0:
            times_through -= 1
            answer += 1

        if part == 2 and times_through > 0:
            answer += times_through
            msg += f" During this rotation, it points at 0 {times_through} times"

        print(msg)

    return answer


if __name__ == "__main__":
    print(day1(2))
