
def swap_files():
    original_file = input("The Original File: ")
    dummy_file = input("The Dummy File: ")

    with open(original_file, 'r') as original_read:
        read_original_file = original_read.read()

    with open(dummy_file, 'r') as dummy_read:
        read_dummy_file = dummy_read.read()  

    with open(original_file, 'w') as original_swapped_to_dummy_file:
        original_swapped_to_dummy_file.write(read_dummy_file)

    with open(dummy_file, 'w') as dummy_swapped_to_original_file:
        dummy_swapped_to_original_file.write(read_original_file)  

    print("Hey Presto! Abracadabra! Check Your Files")    
                       
swap_files()    