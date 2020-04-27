notes = {'Ab': 11, 'A': 0, 'A#': 1, 'Bb': 1, 'B': 2, 'B#': 3, 'Cb':2, 'C': 3, 'C#': 4, 'Db': 4, 'D': 5, 'D#': 6, 'Eb': 6, 'E': 7, 'E#': 8, 'Fb': 7, 'F': 8, 'F#': 9, 'Gb': 9, 'G': 10, 'G#': 11}
notes_index = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')


while True:
    T = tuple(input().split())
    if T == ('***',):
        break
    else:
        pass
    delta = int(input())
    output = []
    for note in T:
        moved = notes[note] + delta
        output.append(notes_index[moved % 12])
    else:
        print(' '.join(map(str, output)))
