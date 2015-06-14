#!python3

import hid

try:
    print("Opening device ...")
    h = hid.device()
    h.open( 1356, 616) #ps3 controller
    
    print("Manufacturer:",h.get_manufacturer_string())
    print("Product:", h.get_product_string())
    print("Serial No:",h.get_serial_number_string())

    print("Doing operational mode ...")
    # lets write operational mode, have to send 0xf5 report
    h.write([0xf5])
    
    print("Done! HAVE FUN!")
    h.close()

except (IOError) as ex:
    print(ex)
