main_list = []
final_list = []
def dong():

    # input all data
    tedad_jens = int(input("Chan Ta Jens Kharidid Ba Ham ?   "))
    for j in range(tedad_jens):
        list1 = []
        sharh = input("Chi Kharidid ?   ")
        list1.append(sharh)
        chan_nafar_kharide = int(input("Chan Nafari Kharidid ?   "))
        print("Aval Begoo Ki Baad Begoo Cheghad Kharj Karde...")

        for i in range(chan_nafar_kharide):
            esm = input("Ki ?   ")
            list1.append(esm)
            cheqad = int(input("Cheqad Kharj Karde ?   "))
            list1.append(cheqad)

        x = list1.copy()
        main_list.append(x)
        list1.clear()

    # calculate dongs for each person
    for m in range(len(main_list)):
        summ = 0
        for k in range(2, len(main_list[m]), 2):
            summ += main_list[m][k]
        avg = summ // chan_nafar_kharide
        # avg = round(avg, 2)
    
    for nafar in range(len(main_list)):
        amaliat = 0
        for nafar2 in range(2, len(main_list[nafar]), 2):
            amaliat = avg - main_list[nafar][nafar2]
            final_list.append(amaliat)

    # print(main_list)
dong()