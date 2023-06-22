from person import Person


# Obs: Detta är ett exempel på arv där Citizen-klassen ärver egenskaper från
# Person-klassen. På så vis kan man skapa klasser för personer med mer
# "specialiserade" egenskaper (t.ex. att de är medborgare) utan att behöva
# skriva om alla metoder.
class Citizen(Person):
    """En medborgare."""

    def __init__(self, full_name, personal_id, address, parents):
        """
        `full_name` är personens är medborgarens fullständiga namn (sträng).
        Krav: minst ett mellanrum måste existera.
        `personal_id` är personnumret (heltal).
        `address` är medborgarens registrerade address (Address-objekt).
        `parents` ett itererbart objekt (en lista, tupel, etc.) med medborgarens
        föräldrar (max 2 stycken).
        Föräldrarna får vara Person-objekt.
        """
        try:
            first_name, last_name = full_name.split(maxsplit=1)
        except ValueError:
            raise ValueError("ett fullständigt namn måste bestå av åtminstone "
                             "ett mellanrum.")

        super(Citizen, self).__init__(first_name, last_name, address)
        self.__personal_id = personal_id

        if len(parents) > 2:
            raise ValueError("en medborgare kan inte ha fler än två föräldrar.")

        for parent in parents:
            if not isinstance(parent, Person):
                raise ValueError("`parents` får endast innehålla "
                                 "Person-objekt.")

        # `parents` kan vara vilket itererbart objekt som helst
        # (lista, tupel, etc.). Vi vill att `self.__parents` ska vara en tupel,
        # och inget annat, så vi konstruerar en tupel från `parents`.
        self.__parents = tuple(parents)

    @property
    def personal_id(self):
        """Personens personnummer."""
        return self.__personal_id

    @property
    def parents(self):
        """Returnerar en tupel med medborgarens föräldrar (Person-objekt)."""
        return self.__parents
