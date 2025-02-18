def read(inp):
    lines=inp.split("\n")
    out=[]
    expecting_value=False
    current_record={}
    t=""
    for i in lines:
        if expecting_value:
            if i.startswith("|"):
                t+=i[1:]
                continue
            else:
                current_record[directive]=t
                expecting_value=False
        i=i.strip()
        if i=="=====":
            out.append(current_record)
            current_record={}
            continue
        if i.startswith("#"):
            continue
        else:
            splitted=i.split(":")
            directive,value=splitted[0],":".join(splitted[1:])
            directive=directive.strip()
            if value=="":
                expecting_value=True
                t=""
            else:
                current_record[directive]=value.strip()
    out.append(current_record)
    return out

def write(records):
    out=""
    for i in records:
        for j in i:
            if ":" in j:
                raise ValueError("Property names cannot have colons")
            out+=j+": "
            if i[j].strip()!=i[j] or "\n" in i[j]:
                for line in i[j].split("\n"):
                    out+="\n|"+line
            else:
                out+=i[j]
            out+="\n"
        out+="=====\n"
    return out[:-6]