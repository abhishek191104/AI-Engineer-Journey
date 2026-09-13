# 3.2 Sets in Python

# 1. Creating a Set

numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)


# 2. Sets do not allow duplicate values

numbers = {10, 20, 20, 30, 30, 40}

print("Set without duplicates:", numbers)


# 3. Adding an item

numbers.add(60)

print("After adding 60:", numbers)


# 4. Removing an item

numbers.remove(20)

print("After removing 20:", numbers)


# 5. Discarding an item

numbers.discard(100)

print("After discard:", numbers)


# 6. Checking if an item exists

if 30 in numbers:
    print("30 is present in the set")


# 7. Set Union

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union_set = set_a.union(set_b)

print("Union:", union_set)


# 8. Set Intersection

intersection_set = set_a.intersection(set_b)

print("Intersection:", intersection_set)


# 9. Set Difference

difference_set = set_a.difference(set_b)

print("Difference:", difference_set)


# 10. Set Length

print("Number of elements:", len(set_a))