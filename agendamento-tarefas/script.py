import os

def organize_files():
#buscando a raiz do path independente do sistema operacional
    base_path = os.path.expanduser('~')
    path = os.path.join(base_path, 'Downloads')

    #navegando até a pasta
    cwd = os.chdir(path)

    #vai listar todos os arquivos contido dentro da pasta dowloads
    full_list = os.listdir(cwd)

    types = ['jpg', 'png', 'zip']
    #vamos criar uma pasta para cada types
    for type_ in types:
        #existe type_ dentro de listando todos os arquivos dentro de downloads
        if type_ not in os.listdir():
            #se não existir crie-o diretório
            os.mkdir(type_)

    #para cada arquivo dentro da pasta que esta dentro de full_list
    for file in full_list:
        #para cada type de pasta
        for type_ in types:
            # se .type dentro da pasta (download) que aqui é file
            if '.' + type_ in file:
                #joga para dentro da pasta especificada
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, type_, file)
                os.replace(old_path, new_path)
                
if __name__ == '__main__':
    organize_files()