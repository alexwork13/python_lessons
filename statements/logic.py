st = 'Print only the words that start with s in this sentence'

list1 = st.split(' ')
print(list1)
for item in list1:
    list2 = [x for x in item ]
    if list2[0] == 's':
        print(item)

        # new comment 4