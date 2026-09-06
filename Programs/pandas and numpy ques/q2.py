def count(labels):
    count = {}

    for label in labels:
        if label in count:
            count[label] += 1
        else:
            count[label] = 1

    return count

result = count(['spam', 'ham', 'spam', 'ham', 'jam'])
print(result)