import json

file_name = '伊卡洛斯.txt'
in_path = 'data/' + file_name
out_path = 'out/' + file_name.split('.')[0] + '.json'

with open(in_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# qa_pairs = []
for i in range(0, len(lines), 2):
    # data = {'prompt': lines[i].strip() + '\n', 'completion': lines[i+1].strip()}
    # qa_pairs.append({'prompt': lines[i].strip() + '\n', 'completion': lines[i+1].strip()})
    data = '{"id": ' + str(int(i/2) + 1) + ', "paragraph": [{"q": "' + lines[i].strip() + '", "a": ["' + lines[i+1].strip() + '"]}]}'

    with open(out_path, 'a', encoding='utf-8') as f:
        # json.dump(qa_pairs, f, indent=4, ensure_ascii=False)
        if i == len(lines) - 2:
            f.write(data)
        else:
            f.write(data + '\n')

# with open(out_path, 'a', encoding='utf-8') as f:
#         json.dump(qa_pairs, f, indent=1, ensure_ascii=False)
        