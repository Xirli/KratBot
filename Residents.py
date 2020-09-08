import xml.etree.ElementTree as ET
from config import RES_FILE


class Resident:

    def __init__(self, user_id, first_name, username, money=0):
        self.user_id = user_id
        self.first_name = first_name
        self.username = username
        self.money = money

        self.list_spell = []
        self.list_ban = []
        self.mana = 1
        self.max_mana = 1
        self.regeneration = 1

    @classmethod
    def generate_resident_xml(cls, xml_element):
        user_id = int(xml_element.attrib['id'])
        first_name = xml_element.find("first_name").text
        username = xml_element.find("username").text
        money = int(xml_element.find("money").text)
        return cls(user_id, first_name, username, money)

    def generate_xml_element(self):
        resident = ET.Element("resident", id=str(self.user_id))

        first_name = ET.Element('first_name')
        first_name.text = self.first_name

        username = ET.Element('username')
        username.text = self.username

        money = ET.Element('money')
        money.text = str(self.money)

        spells = ET.Element("spells")
        for sp in self.list_spell:
            spells.append(sp.generate_xml_element(self))

        resident.append(first_name)
        resident.append(username)
        resident.append(money)
        resident.append(spells)

        return resident


def new_resident(user, residents=None):
    assert (get_resident(user, residents) is None)
    return Resident(user.id, user.first_name, user.username)


def write_xml(residents, output_file=RES_FILE):
    xml = ET.Element('Residents')
    for res in residents:
        xml.append(res.generate_xml_element())
    file = ET.ElementTree(xml)
    file.write(output_file)


def read_xml(input_file=RES_FILE):
    try:
        xml = ET.parse(input_file)
    except FileNotFoundError:
        xml = ET.Element('Residents')
        file = ET.ElementTree(xml)
        file.write(input_file)
        return []

    residents_xml = xml.getroot()
    residents = []
    for res in residents_xml:
        residents.append(Resident.generate_resident_xml(res))
    return residents


def get_resident(user, residents):
    for resident in residents:
        if user.id == resident.user_id:
            return resident
    return None
