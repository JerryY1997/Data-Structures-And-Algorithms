
def avg(lines):
    return sum(lines)/len(lines)

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

def case01():
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = record
    print(name)
    print(email)
    print(phone_numbers)

# case01()

def case02(sales_record):
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    print(trailing_avg)
    print(current_qtr)

# case02(sales_record = [10, 8, 7, 1, 9, 5, 10, 3])

def do_foo(x, y):
    print("foo", x, y)

def do_bar(s):
    print("bar", s)

def case03(records):
    for tag, *args in records:
        if tag == "foo":
            do_foo(*args)
        if tag == "bar":
            do_bar(*args)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

# case03(records)

def case05():
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')
    print(uname)
    print(fields)
    print(homedir)
    print(sh)

# case05()

def case06():
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name)
    print(year)

# case06()

def sun(items):
    head, *tail = items
    return head + sum(tail) if tail else head

items = [1, 10, 7, 4, 5, 9]
print(sum(items))