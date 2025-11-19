
import sys
from collections import deque


def predict_party_victory(senate: str) -> str:
    n = len(senate)
    radiant = deque()
    dire = deque()

    for i, ch in enumerate(senate):
        if ch == "R":
            radiant.append(i)
        elif ch == "D":
            dire.append(i)
        else:
            continue

    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()

        if r < d:
            radiant.append(r + n)
        else:
            dire.append(d + n)

    return "Radiant" if radiant else "Dire"


def main():
    data = sys.stdin.read().strip()
    if not data:
        print("Radiant") 
        return

    result = predict_party_victory(data)
    print(result)


if __name__ == "__main__":
    main()
