"""Print out all the melons in our inventory."""
# import sys

# from melons import melon_names, melon_prices, melon_seedlessness
from melons import melons


def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""
    ''' we are saying that for each melons 'Honeydew' ,'Crenshaw', 'Crane' we want to print attributes '''
    for melon_name, attributes in melons.items():
        '''we are looping over and printing name of the melons in upper case'''    
        print(melon_name.upper())
        """ In this for loop we are looping over attributs and getting melon attribute and value"""
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print('===================================')


print_all_melons(melons)