# Building-an-RPG-Character
A simple Python lab that can help you get better at Python by making a character creation code for an Role-Playing-Game

#Objective
To pass all of the tests, user stories need to be followed. This can be done by using create_character(name, strength, intelligence, charm).

#User Stories

1. Function named create_character accepting name, strength, intelligence, and charisma in order.
2. Name validation:
 - Not a string → "The character name should be a string."
 - Empty → "The character should have a name."
 - Longer than 10 chars → "The character name is too long."
 - Contains spaces → "The character name should not contain spaces."

3. Stats validation:
- Not integers → "All stats should be integers."
- Any < 1 → "All stats should be no less than 1."
- Any > 4 → "All stats shou  ld be no more than 4."
- Sum ≠ 7 → "The character should start with 7 points."

4. On success, return a w4-line string:
 - Line 1: character name
 - Line 2: STR ●●●○○○○○○○ (● repeated by strength, ○ to total 10)
 - Line 3: INT ●●○○○○○○○○ (same for intelligence)
 - Line 4: CHA ●●●●○○○○○○ (same for charisma)
