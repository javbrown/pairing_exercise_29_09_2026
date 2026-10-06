
def single_readable_line(names_list):
    if names_list == []:
        return ""
    elif len(names_list) == 1:
        return str(names_list[0])
    elif len(names_list) == 2:
        return str(names_list[0]) + " & " + str(names_list[1])
    else:
        output_string = ""
        output_string += names_list[0]
        for i in range(1, len(names_list) - 1):
            output_string += ", " + names_list[i] 
        output_string += " & " + names_list[-1] 
        return output_string
