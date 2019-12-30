# List
bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)
print(len(bicycle))


# Accessing Elements in a List
# Index Positions Start at 0, Not 1
print(bicycle[0])
print(len(bicycle[1]))
print(bicycle[0].title())
print(bicycle[1])
print(bicycle[3])

# Index position from last to first
print(bicycle[-1])
print(bicycle[-2])
print(bicycle[-3])
print(bicycle[-4])


# Using Individual Values from a List
message = f"My first bicycle was a {bicycle[0].title()}."
print(message)