if __name__ == '__main__':
    rps_values = [5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602', 14116, 
                  '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203', 13303, '7330', 7186, '10213', '8063', '12283', 
                  15564, 17664, '8996', '12179', '13657', 15817, 15817, 15817, 15817, 15817, 15817,15817, 15817,'16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639', '7335', 
                  '11531', '14346', 7493, 15850, '12791', 11288]
    # sum_of_rps_values = 0
    rps_values_int = []
    
    # while True:
    #     print("Input data:")
    #     input_data = input()
    #     if input_data.isdigit():
    #         rps_values.append(int(input_data))
    #     elif ";" in input_data:
    #         rps_values.extend(map(int, input_data.split(";")))
    #     elif input_data == "":
    #         break
    #     else:
    #         print("Not correct data")
            
    rps_values_int.extend(map(int, rps_values))
    
    info_frequency = {}
    
    for values in rps_values_int:
        if values in info_frequency:
            continue
        else:
            info_frequency.setdefault(values, 0)
            
    for keys in info_frequency:
        i = 0
        for values in rps_values_int:
            if keys == values:
                i += 1
                info_frequency[keys] = i
    print(info_frequency)
    
    # for values in rps_values_int:
    #     sum_of_rps_values += values
    
    # average_rps = sum_of_rps_values / len(rps_values_int)          
    
    # rps_values_int.sort()    
    # quotient, remainder = divmod(len(rps_values_int), 2)
    # median = rps_values_int[quotient] if remainder else sum(rps_values_int[quotient - 1:quotient + 1]) / 2
    
    # if average_rps - median > median * 0.25:
    #     print(average_rps, median, "Происходят скачки")
    # elif average_rps - median <= median * 0.25:
    #     print(average_rps, median, "Нагрузка стабильна")
    # else:
    #     print(average_rps, median, "Происходят снижения")
        
# Second part 
    # rps_values_int_slice = rps_values_int.copy()
    
    # while True:
    #     print("Input slice left and right:")
    #     input_slice_left, input_slice_right = input(), input()
    #     if input_slice_left.isdigit() and input_slice_right.isdigit():
    #         input_slice_left = int(input_slice_left)
    #         input_slice_right = int(input_slice_right)
    #         break
    #     elif input_slice_left == "" or input_slice_right == "":
    #         input_slice_left = 0
    #         input_slice_right = len(rps_values_int_slice)
    #         break
    #     else:
    #         print("Error input")
    
    
    # rps_values_int_slice[input_slice_left:input_slice_right]
    
    
    # for values in rps_values_int_slice:
    #     sum_of_rps_values += values
    
    # average_rps = sum_of_rps_values / len(rps_values_int_slice)          
    
    # rps_values_int_slice.sort()    
    # quotient, remainder = divmod(len(rps_values_int_slice), 2)
    # median = rps_values_int_slice[quotient] if remainder else sum(rps_values_int_slice[quotient - 1:quotient + 1]) / 2
    
    # if average_rps - median > median * 0.25:
    #     print(average_rps, median, "Происходят скачки")
    # elif average_rps - median <= median * 0.25:
    #     print(average_rps, median, "Нагрузка стабильна")
    # else:
    #     print(average_rps, median, "Происходят снижения")  