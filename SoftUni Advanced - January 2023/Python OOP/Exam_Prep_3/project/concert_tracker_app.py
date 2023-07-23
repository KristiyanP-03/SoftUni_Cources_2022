from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.concert import Concert
from project.band import Band


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []



    def create_musician(self, musician_type: str, name: str, age: int):
        valid_musician_types = ["Guitarist", "Drummer", "Singer"]
        if musician_type not in valid_musician_types:
            raise ValueError("Invalid musician type!")

        if name in [person.name for person in self.musicians]:
            raise Exception(f"{name} is already a musician!")

        if musician_type == valid_musician_types[0]:
            musician = Guitarist(name, age)
        if musician_type == valid_musician_types[1]:
            musician = Drummer(name, age)
        if musician_type == valid_musician_types[2]:
            musician = Singer(name, age)

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."




    def create_band(self, name: str):
        if name in [band.name for band in self.bands]:
            raise Exception(f"{name} band is already created!")

        current_band = Band(name)

        self.bands.append(current_band)
        return f"{name} was created."




    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in [location.place for location in self.concerts]:
            current_concert_genre_in_the_same_place = [g.genre for g in self.concerts if place == g.place][0]
            raise Exception(f"{place} is already registered for {current_concert_genre_in_the_same_place} concert!")

        current_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(current_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in [person.name for person in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in [band.name for band in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        target_band = [band for band in self.bands if band.name == band_name][0]
        target_musician = [person for person in self.musicians if person.name == musician_name][0]

        target_band.members.append(target_musician)
        return f"{musician_name} was added to {band_name}."




    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in [band.name for band in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        target_band = [band for band in self.bands if band.name == band_name][0]

        if musician_name not in [name for name in target_band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        for musician in target_band.members:
            if musician == musician_name:
                target_band.members.remove(musician)
                return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [x for x in self.bands if x.name == band_name][0]
        concert = [x for x in self.concerts if x.place == concert_place][0]
        members = band.members
        type_members = [type(x).__name__ for x in band.members]

        if "Guitarist" not in type_members or "Drummer" not in type_members or "Singer" not in type_members:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            needed_skills = ["play the drums with drumsticks", "sing high pitch notes", "play rock"]

        elif concert.genre == "Metal":
            needed_skills = ["play the drums with drumsticks", "sing low pitch notes", "play metal"]

        elif concert.genre == "Jazz":
            needed_skills = ["play the drums with drum brushes", "sing high pitch notes", "sing low pitch notes",
                             "play jazz"]

        for member in members:
            needed_skills_copy = needed_skills.copy()
            for skill in needed_skills_copy:
                if skill in member.skills:
                    needed_skills.remove(skill)

        if needed_skills:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

from project.concert_tracker_app import ConcertTrackerApp

musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))