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
    - agendamento de tarefas

