from anytree import Node, RenderTree, Resolver, AsciiStyle, findall, findall_by_attr
import string

words = string.ascii_lowercase

start_node = Node('')
current_node = Node('', parent=start_node)
r = Resolver('name')

with open('day7.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines() 
    for line in lines:
        line = line.strip()
        #Case when we have a cd
        if (line[0] == '$'):
            if (line[2] == 'c'):
                if (line[5] == '.'):
                    current_node = r.get(current_node,'..')
                elif (line[5] == '/'):
                    current_node = start_node
                else:
                    current_node = r.get(current_node, line[5:])
        else:
            if (line[0] == 'd'):
                dir = line[4:]
                dir_node = Node(dir, parent=current_node)
            else:
                count = 0
                for ch in line:
                    if ch.isdigit():
                        count += 1
                size = line[0:count]
                name = line[count+1:]
                file_node = Node(name, parent=current_node)
                dimension = Node(int(size), parent=file_node)

print(RenderTree(start_node,style=AsciiStyle()).by_attr())
