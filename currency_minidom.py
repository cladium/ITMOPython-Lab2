import xml.dom.minidom as minidom

FILENAME = "currency.xml"

doc = minidom.parse(FILENAME)
valutes = doc.getElementsByTagName("Valute")

for valute in valutes:
    nominal_elements = valute.getElementsByTagName("Nominal")
    # check for existence of <Nominal> element
    if nominal_elements:
        nominal_value = nominal_elements[0].firstChild.data.strip()
        if nominal_value in {"10", "100"}:
            charcode_elements = valute.getElementsByTagName("CharCode")
            if charcode_elements:
                charcode_value = charcode_elements[0].firstChild.data.strip()
                print(charcode_value)
