from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == 'main':
    with open(r'somefile.txt') as f:
        for line, prevlines in search(f, 'e', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

def case01():
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.append(4)
    print(q)
    q.append(5)
    print(q)

# case01()


def case02():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.appendleft(4)
    print(q)
    a = q.pop()
    print(a)
    print(q)
    b = q.popleft()
    print(b)
    print(q)

# case02()