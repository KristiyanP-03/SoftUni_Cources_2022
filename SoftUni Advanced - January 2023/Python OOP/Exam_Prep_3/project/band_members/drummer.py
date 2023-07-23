from project.band_members.musician import Musician

SKILL_LIST = ["play the drums with drumsticks","play the drums with drum brushes","read sheet music"]

class Drummer(Musician):
    def learn_new_skill(self, new_skill: str):
        if new_skill not in SKILL_LIST:
            raise ValueError(f"{new_skill} is not a needed skill!")

        elif new_skill in SKILL_LIST and new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."