st = 'Print every word in this sentence that has an even number of letters'
list1 = st.split(' ')

for item in list1:
    if len(item) % 2 == 0:
        print(f"{item} - четная длина {len(item)}")
