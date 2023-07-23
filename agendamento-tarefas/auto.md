# Scripts para agendamento de tarefas

## Usando cron

>Conectando com pc em nuvem, tudo feito por terminal
    - ssh {ip} {login} {password}

>No terminal do mac/linux
    - crontab -l = lista todos crontab/scripts
    - crontab -e = editar os crontab/scripts
    - crontab guru, site para verificar os *
        - vai abrir um arquivo de texto
        - usaremos VI
            - passaremos o path do arquivo a ser executado
                - usando o pwd temos o caminho completo
                - contra barra \ ele entende como se tivesse um espaço no nome da pasta
                - which python3 = para descobrir o caminho completo
            - * * * * * ele indica o tempo a ser executado o script

>No windows
    - agendador de tarefas
        - ação > criar tarefa
            - geral
                - coloque o nome
            - disparadores
                - aqui escolhemos o formato que sera disparado o scripts
                - pegando o path python -c "import sys; print(sys.executable)"
                - novo
                    - colocar o path
                    - coloque o nome do arquivo que contém o script.extensão
                    - iniciar em, é a localização do arquivo script
             

