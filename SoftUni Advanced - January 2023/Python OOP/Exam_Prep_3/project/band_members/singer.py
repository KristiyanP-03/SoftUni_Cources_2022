from project.band_members.musician import Musician

SKILLS_LIST = ["sing high pitch notes", "sing low pitch notes"]

class Singer(Musician):
    def learn_new_skill(self, new_skill: str):

        if new_skill in SKILLS_LIST and new_skill not in self.skills:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."

        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        else:
            raise ValueError(f"{new_skill} is not a needed skill!")
