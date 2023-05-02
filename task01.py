from counter import Counter

c1 = Counter(12)
c2 = Counter()
c3 = Counter(12)

print(c1.get_count())
c1.increment()
c1.increment()
c2.increment()
c3.decrement()
c1.reset()


print(c1)
print(c2)
print(c3)
print(c1)