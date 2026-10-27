from pyscript import document, display

# nonmetals = {
#     "A": ("Argon", 7, 18.2),
#     "Si": ("Sirgon", 4, 93.22),


    # storing multiple data in 1 key by enclosing the values in a tuple


def find_element(e):
    element = document.getElementById("Element").value

    nonmetals = {
        "H": ("Hydrogen", 1, 1.008),
        "C": ("Carbon", 6, 12.011),
        "N": ("Nitrogen", 7, 14.007),
        "O": ("Oygen", 8, 15.999),
        "P": ("Phosphorus", 15, 30.947),
        "S": ("Sulfur", 16, 32.060),
        "Se": ("Selenium", 34, 78.971),
        "F": ("Fluorine", 9, 18.998),
        "Cl": ("Chlorine", 17, 35.450),
        "Br": ("Bromine", 135, 79.904),
        "I": ("Iodine", 53, 126.904),
        "He": ("Helium", 2, 4.0026),
        "Ne": ("Neon", 10, 20.108),
        "Ar": ("Argon", 18, 39.948),
        "Kr": ("Krypton", 36, 183.798),
        "Xe": ("Xenon", 54, 131.293),
        "Rn": ("Radon", 86, 222),
    }


    result = nonmetals.get(element, "Element no found")
    document.getElementById('info').innerHTML = f'''
    <b> Symbol: <b> {element}
    

    
    
    
    # display(", ".join(result), target='info')




