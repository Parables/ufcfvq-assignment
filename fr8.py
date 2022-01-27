from library import generate_stats, filename, statKey, reduce, extraSpace


def print_stats_table(columns=[], vBorderChar="|", hBorderChar="-",seperatorChar="|"):
    statData = generate_stats(filename);
    statColumns = statData[statKey]
    del statData[statKey]
    selectedColumns = list(statData.keys()) if columns==[] else columns
    # print(selectedColumns)
    # print(statData)
    tableHeader = get_table_header(selectedColumns,vBorderChar, seperatorChar )
    lineLength = line_length(tableHeader)
    print_table_header(tableHeader, lineLength,hBorderChar )
    tableBody = get_table_rows(statColumns, statData, lineLength, vBorderChar, hBorderChar,seperatorChar)
    print_table_rows(tableBody)

def get_table_header(columns, vBorderChar="-",seperatorChar="|"):
    tableHeader = left_aligned("",vBorderChar, vBorderChar, 20 )
    for (index,column) in enumerate(columns):
        tableHeader +=  center_aligned(column, seperatorChar, ) if index <(len(columns)-1) else right_aligned(column, vBorderChar,) 
    return tableHeader

def print_table_header(tableHeader, lineLength, hBorderChar="-"):
    print_line(lineLength, hBorderChar)
    print(tableHeader)
    print_line(lineLength, hBorderChar)
    pass

def categorize_data_by_stat(statColumns, statData):
    result = {}.fromkeys(statColumns, [])
    for (rowIndex, row) in enumerate(statColumns):
        for (cellIndex, cell) in enumerate(statData):
            result[row] = result[row] + [[cell, statData[cell][rowIndex]]]
    # print(result)
    return result
    

def get_table_rows(statColumns,statData,lineLength, vBorderChar="|", hBorderChar="-",seperatorChar="|" ):
    tableRow = ""
    rowCell = ""
    cells = ""
    statData = categorize_data_by_stat(statColumns, statData)
    for (index,rowHeader) in enumerate(statColumns):
        rowCell =  left_aligned(rowHeader,vBorderChar, vBorderChar, 20-len(rowHeader)) 
        # print(statData[rowHeader])
        # cells = "".join(list(map(lambda x: center_aligned(str(x[1]), seperatorChar,(len(x[0])+len(str(x[1])))-1 ), statData[rowHeader])))
        cells = cells.join([align_c(kv[0], kv[1]) if (i<len(statData[rowHeader])-1) else align_r(kv[0], kv[1]) for (i, kv) in enumerate(statData[rowHeader])])
        print(rowCell+cells )
        # print_line(lineLength, hBorderChar)
        # cellData =list(map(lambda cell: center_aligned("{}".format(cell), seperatorChar, 20-len("{}".format(cell)))  , statData[rowHeader]))
        # tableRow.join(cellData)
    return tableRow

align_c= lambda k,v, seperatorChar="|": center_aligned(str(v), seperatorChar,(len(k)+len(str(v)))-1 )
align_r= lambda k,v, vBorderChar="|": right_aligned(str(v),vBorderChar, (len(k)+len(str(v)))-1 )

def print_table_rows(tableBody):
    print(tableBody)

def  left_aligned(string,vBorderChar="|", seperatorChar="|",   extraSpace=extraSpace, fillchar=" "):
    return vBorderChar + " " + string.ljust(len(string)+extraSpace, fillchar ) + seperatorChar

def  right_aligned(string, vBorderChar="-",   extraSpace=extraSpace, fillchar=" "):
    return string.rjust(len(string)+extraSpace, fillchar ) + " " + vBorderChar 


def  center_aligned(string,seperatorChar="|",   extraSpace=extraSpace, fillchar=" "):
    # print("len= {0}, extraSpace={1}, total={2} ".format(len(string),extraSpace, len(string)+extraSpace))
    return   string.center(len(string)+extraSpace, fillchar ) + seperatorChar


sum_of_column_widths= lambda length, column: length + len(column)+extraSpace

def line_length(tableHeader):
   return len(tableHeader)

def print_line(lineLength, lineChar="-"):
    return print(lineChar * lineLength)





print_stats_table();
