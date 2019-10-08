studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]


def gemiddelde_per_student(studentencijfers):
    antw = []
    for list in studentencijfers:
       res = sum(list) / len(list)
       antw.append(res)
    return antw


def gemiddelde_van_alle_studenten(studentencijfers):
    antw = sum(gemiddelde_per_student(studentencijfers)) / len(gemiddelde_per_student(studentencijfers))
    return antw


print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
