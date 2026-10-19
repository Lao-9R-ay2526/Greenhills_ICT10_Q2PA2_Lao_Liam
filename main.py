# Participation Activity 1: Lists
from pyscript import display, document

def get_name(e):
        document.getElementById('output').innerHTML = ' '

        grade_seven = {'Matteo Resurreccion', 'Josua Ortiz', 'Pocholo Comanda', 'Zangief Briones'} # Custom Grade 7
        grade_eight = {'Matt Witness', 'Ferb Fletcher', 'Joe Swanson', 'Arkin San Agustin'} # Custom Grade 8
        grade_nine = {'Bareel Johnson', 'Miguel Velarde', 'Peter Griffin', 'Cleveland Brown'} # Custom Grade 9
        grade_ten = {'Liam Lao', 'Juan Piansay', 'Daphne Mariano'} # Actual Grade 10

        fname = document.getElementById('first').value
        lname = document.getElementById('last').value
        fullname = fname + lname


        members = (grade_seven | grade_eight | grade_nine | grade_ten)
        members.add(fullname)

        display(f'List of members {members} amount of members{len(members)}', target='output')
