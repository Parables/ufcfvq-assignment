from library import generate_stats, filename, statKey, reduce, padding, vBorderChar, hBorderChar, seperatorChar


def print_stats_table(columns=[], divideRows=False, padding=padding, vBorderChar=vBorderChar, hBorderChar=hBorderChar, seperatorChar=seperatorChar):
    statData = generate_stats(filename)
    statColumns = statData[statKey]
    del statData[statKey]

    selectedColumns = list(statData.keys()) if columns == [] else columns

    cells, widths = get_header_row(["".ljust(10, " ")] +
                             selectedColumns, padding, vBorderChar, seperatorChar)
    lineLength = len(cells)
    print_row(cells, lineLength, hBorderChar)
    print_table_body(statColumns, statData, widths, padding, lineLength,divideRows, vBorderChar, hBorderChar, seperatorChar)


def get_header_row(cells, padding, vBorderChar=vBorderChar, seperatorChar=seperatorChar):
    rows = ""
    widths = []
    for (index, cell) in enumerate(cells):
        if(index == 0):
            c, w = left_aligned(cell, None, padding, vBorderChar, seperatorChar)
            rows = rows + c
            widths += [w]
        elif(index < (len(cells)-1)):
            c, w = center_aligned(cell, None,padding,  seperatorChar)
            rows = rows + c
            widths += [w]
        else:
            c, w = right_aligned(cell, None, padding, vBorderChar)
            rows = rows + c
            widths += [w]
    return rows, widths


def get_body_row(cells,widths, padding, vBorderChar=vBorderChar, seperatorChar=seperatorChar ):
    rows = ""
    for (index, cell) in enumerate(cells):
        if(index == 0):
            c,w = left_aligned(str(cell), widths[index],padding, vBorderChar, seperatorChar)
            rows = rows + c
        elif(index < (len(cells)-1)):
            c,w = center_aligned(str(cell), widths[index],padding, seperatorChar)
            rows = rows + c
        else:
            c,w = right_aligned(str(cell), widths[index],padding, vBorderChar)
            rows = rows + c
    return rows


def print_row(cells, lineLength, hBorderChar=hBorderChar):
    print_line(lineLength, hBorderChar)
    print(cells)
    print_line(lineLength, hBorderChar)


def get_table_body(statColumns, statData):
    # result = { r: [r] for (i,r) in enumerate(startColumns)}
    result = []
    for (firstCellIndex, firstCell) in enumerate(statColumns):
        row = [firstCell]
        for (cellIndex, cell) in enumerate(statData):
            row += [statData[cell][firstCellIndex]]
        result += [row]
    return result


def print_table_body(statColumns, statData, widths, padding, lineLength,divideRows=False, vBorderChar=vBorderChar, hBorderChar=hBorderChar, seperatorChar=seperatorChar):
    rows = get_table_body(statColumns, statData)
    for cells in rows:
        row = get_body_row(cells, widths, padding, vBorderChar,seperatorChar)
        print(row)
        if(divideRows): print_line(lineLength, "_")
    print_line(lineLength)


def left_aligned(string, width=None, padding=padding, vBorderChar=vBorderChar, seperatorChar=seperatorChar, fillchar=" "):
    cell = vBorderChar + " " + \
        string.ljust(
            len(string)+padding if width is None else width, fillchar) + seperatorChar
    width = len(cell) - (len(vBorderChar) + len(seperatorChar))
    return cell, width


def right_aligned(string, width=None, padding=padding, vBorderChar=vBorderChar, fillchar=" "):
    cell = string.rjust(
        len(string)+padding if width is None else width, fillchar) + " " + vBorderChar
    width = len(cell) - len(vBorderChar)
    return cell, width


def center_aligned(string, width=None, padding=padding, seperatorChar=seperatorChar, fillchar=" "):
    cell = string.center(
        len(string)+padding if width is None else width, fillchar) + seperatorChar
    width = len(cell) - len(seperatorChar)
    return cell, width


def print_line(lineLength, lineChar="-"):
    return print(lineChar * lineLength)


print_stats_table()
