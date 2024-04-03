import os

def reverse(inputpath, outputpath):
    with open(inputpath, 'r') as infile:
        content = infile.read()
    reversed_content = content[::-1]
    with open(outputpath, 'w') as outfile:
        outfile.write(reversed_content)

def copy(inputpath, outputpath):
    with open(inputpath, 'rb') as infile:
        with open(outputpath, 'wb') as outfile:
            outfile.write(infile.read())

def duplicate_contents(inputpath, outputpath, n):
    with open(inputpath, 'r') as infile:
        content = infile.read()
    duplicated_content = content * n
    with open(outputpath, 'w') as outfile:
        outfile.write(duplicated_content)

def replace_string(inputpath, outputpath, needle, newstring):
    with open(inputpath, 'r') as infile:
        content = infile.read()
    replaced_content = content.replace(needle, newstring)
    with open(outputpath, 'w') as outfile:
        outfile.write(replaced_content)

# 使用例
current_directory = os.path.dirname(os.path.abspath(__file__))  # スクリプトのディレクトリを取得

input_filename = "input.txt"
input_path = os.path.join(current_directory, input_filename)
output_reverse_filename = "output_reverse.txt"
output_reverse_path = os.path.join(current_directory, output_reverse_filename)
output_copy_filename = "output_copy.txt"
output_copy_path = os.path.join(current_directory, output_copy_filename)
output_duplicate_filename = "output_duplicate.txt"
output_duplicate_path = os.path.join(current_directory, output_duplicate_filename)
output_replace_filename = "output_replace.txt"
output_replace_path = os.path.join(current_directory, output_replace_filename)

# それぞれの操作で新しいファイルを作成するように修正
copy(input_path, output_copy_path)
reverse(input_path, output_reverse_path)
duplicate_contents(input_path, output_duplicate_path, 3)
replace_string(input_path, output_replace_path, "needle", "newstring")
