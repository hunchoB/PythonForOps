if __name__ == '__main__':
    rps_values = (5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602', 14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203', 13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850, '12791', 11288)
    sum_of_rps_values = 0
    rps_values_int = ()

    for values in rps_values:
        values = int(values)
        rps_values_int += (values,)
        sum_of_rps_values += values
        
    tur = sorted(rps_values_int)    
    quotient, remainder = divmod(len(rps_values_int), 2)
    median = tur[quotient] if remainder else sum(tur[quotient - 1:quotient + 1]) / 2
    
    average_rps = sum_of_rps_values / len(rps_values_int)
    print(average_rps, median)
    # print(quotient, remainder)

