# Function defined
def create_character(name,strength,intelligence,charisma):
# Name Validation
  if not isinstance(name,str):
    return 'The character name should be a string'

  if name == "":
    return 'The character should have a name'
  if len(name) > 10:
    return 'The character name is too long'
  if " " in name:
    return 'The character name should not contain spaces'

  # Stats validation
  stats = [strength,intelligence,charisma]
  if not all(isinstance(stat,int) for stat in stats): # Added closing parenthesis
    return 'All stats should be integers'
  if any(stat < 1 for stat in stats):
    return 'All stats should be no less than 1'
  if any(stat > 4 for stat in stats):
    return 'All stats should be no more than 4'
  if sum(stats) != 7: # Added colon
    return 'The character should start with 7 points'

  # Return a 4-line string
  full_dot = "●"
  empty_dot ="○"

  def make_line(label, value):
      return f"{label} {full_dot * value}{empty_dot * (10 - value)}"

  return (
      f"{name}\n"
      f"{make_line('STR', strength)}\n"
      f"{make_line('INT', intelligence)}\n"
      f"{make_line('CHA', charisma)}"
  )
# Returns the string
print(create_character('ren', 4, 2, 1))
