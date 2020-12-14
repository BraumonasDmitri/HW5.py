with open('classes.txt', 'r', encoding='utf-8') as f:
    subj = {}
    for line in f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
print(f'Общее количество часов по предмету: {subj}')