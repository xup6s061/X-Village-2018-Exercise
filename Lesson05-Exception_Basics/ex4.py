class RelationException(Exception):
    def __init__(self, msg ):
        self.msg= msg
    def __str__(self):
        return self.msg

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    try:
        if relation[pa] != pb and relation[pb] !=pa:
            raise RelationException('Are you sure that '+pa +' and ' +pb +' are in love with each other?')
    except KeyError:
        raise RelationException('No relation found'+'\n'+'Are you sure that '+pa +' and ' +pb +' are in love with each other?')
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except RelationException as e:
    print(e)