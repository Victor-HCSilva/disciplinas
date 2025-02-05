from .models import (
    Disciplina
)

def group(grupo):
    return Disciplina.objects.filter(grupo = grupo)

if __name__=='__main__':
    print(group(1))
    