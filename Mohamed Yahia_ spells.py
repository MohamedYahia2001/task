class Spells:
    def __init__(self, spell_name, spell_value):
        self.spell_name = spell_name
        self.spell_value = spell_value


class Person():
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def change_health(self, value):
        self.health = self.health - value

    def change_energy(self, value):
        self.energy = self.energy - value


Harry = Person(100, 500)
Voldmort = Person(100, 500)
while Harry.health != 0 and Voldmort.health != 0:
    full_input = input("Enter the two spells (Harry then Voldmort):\n").split()

    V_dic = {
        "AvadaKedavra": 100, "Crucio": 40, "Imperio": 20,
        "sheild": 0, "Taboo": 80, "Expulso": 60, "Confringo": 55
    }
    H_dic = {
        "AvadaKedavra": 100, "Crucio": 40, "Imperio": 20,
        "sheild": 0, "Reducto": 60, "Fiendfyre": 50, "Nebulus": 40,
    }
    try:
        spell_1 = Spells(full_input[0], H_dic[full_input[0]])
        spell_2 = Spells(full_input[1], V_dic[full_input[1]])
    except:
        print("invalid spell")
        continue
    if spell_2.spell_name != "sheild" and spell_1.spell_name != "sheild":
        if spell_2.spell_value > spell_1.spell_value:
            Harry.change_health(abs(spell_2.spell_value - spell_1.spell_value))
        else:
            Voldmort.change_health(abs(spell_2.spell_value - spell_1.spell_value))
    Harry.change_energy(spell_1.spell_value)
    Voldmort.change_energy(spell_2.spell_value)
    print("\tHarry\tVoltmort")
    print("Health : " + str(Harry.health) + "\t\t" + str(Voldmort.health))
    print("Energy : " + str(Harry.energy) + "\t\t" + str(Voldmort.energy))
if Harry.health == 0:
    print("Voldmort is the winner ..")
else:
    print("Harry is the winner ..")
