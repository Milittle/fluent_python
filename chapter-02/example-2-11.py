# author:milittle
# Line items from a flat file invoice


invoice = '''
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
'''

def test():
    SKU = slice(0, 6)
    DESCRIPTION = slice(6, 40)
    UNIT_PRICE = slice(40, 52)
    QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)
    line_items = invoice.split('\n')[2:-1]

    for item in line_items:
        print(item[UNIT_PRICE], item[DESCRIPTION])



def main():
    test()

if __name__ == '__main__':
    main()