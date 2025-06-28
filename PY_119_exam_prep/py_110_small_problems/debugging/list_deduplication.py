data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed

index, datum = enumerate(data[0])
print(index)
print(datum)