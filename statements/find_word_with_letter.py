st = 'Print only the words that start with s in this sentence'


for item in st.split():
    list2 = [x for x in item ]
    if list2[0] == 's':
        print(item)

        # new comment 4