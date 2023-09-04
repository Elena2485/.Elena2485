def indent(s: str, width: int) -> str:
    return ' ' * (max(0, width - len(s))) + s
print (indent('1,2,3' , 123))


####
def Spisok(a: list, b: list ) -> int:
    return max(len(a), len(b))