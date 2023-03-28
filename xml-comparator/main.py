import xml.etree.ElementTree as ET

first_file = './file1.xml'
second_file = './file2.xml'

first_tree = ET.parse(first_file)
second_tree = ET.parse(second_file)

first_root = first_tree.getroot()
second_root = second_tree.getroot()


def compare(root1, root2, diffs):
    if root1.text != root2.text:
        diffs.append(f'{root1.tag}: {root1.text} | {root2.text}')
    if root1.tail != root2.tail:
        diffs.append(f'{root1.tag}: {root1.tail} | {root2.tail}')
    if root1.attrib != root2.attrib:
        diffs.append(f'{root1.tag}: {root1.attrib} | {root2.attrib}')

    child1 = list(root1)
    child2 = list(root2)
    for i in range(len(child1)):
        try:
            compare(child1[i], child2[i], diffs)
        except IndexError:
            diffs.append(f'Child element mismatch: {root1.tag} has more child elements than {root2.tag}')
            break
    if len(child1) != len(child2):
        diffs.append(f'Child element count difference: {root1.tag} has {len(child1)} children, while {root2.tag} has {len(child2)}')


diffs = []

compare(first_root, second_root, diffs)

# write the differences to the txt file
with open('differences.txt', 'w') as f:
    f.write(f"Left side is {first_file[2:]} | Right side is {second_file[2:]}\n\n")
    for diff in diffs:
        f.write(diff + '\n')
