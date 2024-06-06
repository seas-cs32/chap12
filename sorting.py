### chap12/sorting.py
from unsort import unsort

print('The `sort` method on Python lists sorts in-place')
a, c, w = unsort()
a.sort()
c.sort()
w.sort()
print(f'a = {a}\nc = {c}\nw = {w}\n')

print('The `sorted` built-in function leaves the input object unchanged')
a, c, w = unsort()
aa = sorted(a)
cc = sorted(c)
ww = sorted(w)
print(f'aa = {aa}\ncc = {cc}\nww = {ww}\n')

print('The `sort` method reversed')
a, c, w = unsort()
a.sort(reverse=True)
c.sort(reverse=True)
w.sort(reverse=True)
print(f'a = {a}\nc = {c}\nw = {w}\n')

print('The `sorted` built-in function reversed')
a, c, w = unsort()
aa = sorted(a, reverse=True)
cc = sorted(c, reverse=True)
ww = sorted(w, reverse=True)
print(f'aa = {aa}\ncc = {cc}\nww = {ww}\n')

print('`sorted` ignoring capitalization')
a, c, w = unsort()
w_caps = sorted(w)
w_nocaps = sorted(w, key=str.lower)
print(f'w_caps = {w_caps}')
print(f'w_nocaps = {w_nocaps}')
print()

cs32_staff = [
    # fields: name, fav_color, fav_animal, batting_avg
    ('Mike', 'blue', 'dog', 0.042),
    ('Dhilan', 'brown', 'lion', 0.333),
    ('Manana', 'black', 'golden eagle', 0.395),
    ('Emily', 'forest green', 'bird', 0.400),
    ('Jiahui', 'red', 'bear', 0.392),
    ('Matthew', 'yellow', 'ram', 0.299),
    ('Karly', 'white', 'dolphin', 0.315),
    ('Sid', 'baby blue', 'orange', 0.215),
    ('Nadine', 'purple', 'owl', 0.357),
    ('Patrick', 'green', 'dragon', 0.278),
    ('Cosmo', 'yellow', 'squirrel', 0.043),
]

def batting_avg(t):
    return t[3]

print('`sorted` using an attribute')
print(sorted(cs32_staff, key=batting_avg, reverse=True))
print()
