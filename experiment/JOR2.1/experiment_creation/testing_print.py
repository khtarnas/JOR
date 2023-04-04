comparisons = [[4, 6], [22, 18], [4, 22], [4, 8], [6, 22], [14, 30], [18, 30], [22, 30], [6, 30], [10, 4], [8, 30], [6, 16], [6, 8], [8, 16], [40, 28], [40, 6], [4, 40], [14, 22], [8, 10], [40, 8], [40, 14], [22, 10], [10, 40], [40, 22], [34, 40], [6, 10], [10, 30], [4, 16], [22, 8], [10, 16], [16, 14], [30, 4], [18, 40], [30, 28]]
test_order = [26, 43, 18, 9, 86, 63, 55, 23, 75, 66, 46, 10, 7, 59, 37, 40, 81, 19, 22, 1, 24, 28, 0, 52, 14, 8, 45, 15, 48, 31, 58, 50, 32, 42, 56, 49, 11, 4, 38, 74, 13, 21, 83, 82, 72, 79, 80, 60, 77, 12, 68, 78, 53, 44, 47, 54, 29, 76, 17, 70, 41, 73, 30, 27, 85, 2, 36, 25]
study_order = [18, 10, 63, 59, 9, 40, 66, 19, 48, 35, 28, 58, 37, 42, 43, 7, 26, 46, 23, 38, 86, 31, 55, 75, 13, 79, 52, 80, 22, 12, 81, 15, 24, 49, 1, 77, 0, 8, 14, 45, 56, 83, 44, 16, 50, 60, 4, 21, 32, 11, 74, 2, 82, 30, 72, 29, 36, 3, 54, 25, 78, 84, 53, 70, 68, 41, 73, 85, 76, 17, 47, 87, 69, 71, 67, 34, 5, 33, 27, 65, 57, 20, 39, 62, 61, 51, 64, 6]

# print(len(comparisons))
# print(len(test_order))

for idx, i in enumerate(comparisons):

  # Find real distances: (position in study + 22) - position in test
  # + 22 because of 11 study cards with 2 items each
  item1 = test_order[idx * 2]
  item2 = test_order[idx * 2 + 1]
  dist1 = ((idx * 2) - study_order.index(item1) + 22) // 2
  dist2 = ((idx * 2) - study_order.index(item2) + 22) // 2

  # print(idx * 2)
  # print(study_order.indexOf(item1))

  # Print
  print("Item " + str(item1) + " supposed to be at distance " + str(i[0]) + ", but at " + str(dist1))
  print("Item " + str(item2) + " supposed to be at distance " + str(i[1]) + ", but at " + str(dist2))
  print("")
