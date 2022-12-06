# flake8: noqa
from dataclasses import dataclass


@dataclass
class NameAndBits:
    name: str
    bits: int


STRUCTURE = {
    0: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 1),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 1),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 1),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 1),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 1),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 1),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 1),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 1),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 1),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 1),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 1),
        NameAndBits("weapon_type", 5),
    ],
    1: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 1),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 2),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 2),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 2),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
    ],
    2: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 3),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 2),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 2),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 2),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
    ],
    3: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 3),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 2),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 2),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
    ],
    4: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 3),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 2),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 2),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
    ],
    5: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 3),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 2),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 2),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
        NameAndBits("is_elf_ear", 1),
    ],
    6: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 3),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 2),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("_unknown", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
        NameAndBits("is_elf_ear", 1),
    ],
    7: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 3),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 2),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("is_sub_weapon", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
        NameAndBits("is_elf_ear", 1),
    ],
    8: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 3),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 3),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 2),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("is_sub_weapon", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
        NameAndBits("is_elf_ear", 1),
    ],
    9: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 3),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 4),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 2),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("is_sub_weapon", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
        NameAndBits("is_elf_ear", 1),
    ],
    10: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 3),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 4),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 3),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("is_sub_weapon", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
        NameAndBits("is_elf_ear", 1),
    ],
    11: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 3),
        NameAndBits("is_hair_over_40000", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 4),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 3),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("is_sub_weapon", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
        NameAndBits("is_elf_ear", 1),
    ],
    12: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 3),
        NameAndBits("is_hair_over_40000", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 4),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 3),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("is_sub_weapon", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 5),
        NameAndBits("is_elf_ear", 1),
        NameAndBits("is_lef_ear", 1),
        NameAndBits("_unknown", 2),
        NameAndBits("hair_mix_color", 4),
        NameAndBits("hair_mix_ratio", 7),
    ],
    13: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 4),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 3),
        NameAndBits("is_hair_over_40000", 1),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 4),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 3),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("is_sub_weapon", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 8),
        NameAndBits("is_elf_ear", 1),
        NameAndBits("is_lef_ear", 1),
        NameAndBits("_unknown", 2),
        NameAndBits("hair_mix_color", 4),
        NameAndBits("hair_mix_ratio", 7),
    ],
    23: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 10),
        NameAndBits("face_type", 1),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 4),
        NameAndBits("hair_type", 4),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 4),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 3),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("is_sub_weapon", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 8),
        NameAndBits("is_elf_ear", 1),
        NameAndBits("is_lef_ear", 1),
        NameAndBits("_unknown", 14),
        NameAndBits("hair_mix_color", 4),
        NameAndBits("hair_mix_ratio", 7),
    ],
    24: [
        NameAndBits("gender", 1),
        NameAndBits("skin_id", 10),
        NameAndBits("face_type", 1),
        NameAndBits("face_id", 10),
        NameAndBits("face_gender", 4),
        NameAndBits("hair_type", 4),
        NameAndBits("hair_id", 10),
        NameAndBits("hair_gender", 4),
        NameAndBits("cap_id", 10),
        NameAndBits("cap_gender", 3),
        NameAndBits("face_accessory_id", 10),
        NameAndBits("face_accessory_gender", 2),
        NameAndBits("eye_accessory_id", 10),
        NameAndBits("eye_accessory_gender", 2),
        NameAndBits("ear_accessory_id", 10),
        NameAndBits("ear_accessory_gender", 2),
        NameAndBits("is_long_coat", 1),
        NameAndBits("coat_id", 10),
        NameAndBits("coat_gender", 4),
        NameAndBits("pants_id", 10),
        NameAndBits("pants_gender", 2),
        NameAndBits("shoes_id", 10),
        NameAndBits("shoes_gender", 2),
        NameAndBits("glove_id", 10),
        NameAndBits("glove_gender", 2),
        NameAndBits("cape_id", 10),
        NameAndBits("cape_gender", 2),
        NameAndBits("is_not_blade", 1),
        NameAndBits("is_sub_weapon", 1),
        NameAndBits("shield_id", 10),
        NameAndBits("shield_gender", 4),
        NameAndBits("is_cash_weapon", 1),
        NameAndBits("weapon_id", 10),
        NameAndBits("weapon_gender", 2),
        NameAndBits("weapon_type", 8),
        NameAndBits("is_elf_ear", 1),
        NameAndBits("is_lef_ear", 1),
        NameAndBits("_unknown", 14),
        NameAndBits("hair_mix_color", 4),
        NameAndBits("hair_mix_ratio", 7),
    ]
}
