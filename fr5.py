
def readfile(filename):
    with open(filename, encoding='utf-8') as f:
        columns= f.readline().replace('\n', "").strip().split(",")
        rows= [row.replace('\n', "").strip().split(",") for row in f.readlines()]
        content = {h: list() for h in columns}

        for (rowIndex, row) in enumerate(rows):
            for (cellIndex, cell) in enumerate(row):
                header = columns[cellIndex]
                headerValue = content.get(header, [])
                content[header] = headerValue + [cell]
        return {
            "columns": columns,
            "rows": rows,
            "content": content
        }




def read_column(filename, columnIndex):
    file = readfile(filename);
    header = file['columns'][columnIndex]
    return header, file['content'][header];

# print(read_column("task1.csv", -2))