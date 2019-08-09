Instalar o gitlab
    docker-compose up -d gitlab
   
Criar conta e repositório no gitlab; fazer push das aplicações
    http://localhost:9090/
    http://localhost:9090/projects/new > agenda_mysql
    http://localhost:9090/projects/new > nodejsserver

Instalar o bando de dados MySQL 

Entrar no container MySQL e executar o script de criação do banco de dados 

Instalar a aplicação agenda

Instalar o Jenkins  

Configurar o Slack para as aplicações

Configurar o Jenkins para a primeira aplicação
No Jenkins: baixar plugins publish over ssh; slack notifications e gitlab

No Jenkins: criar servidor ssh 
No Jenkins: criar job agenda
No job agenda: configurar repositório e Slack notifications

Criar aplicação nodejsserver

No Jenkins: criar servidor ssh nodejsserver
No Jenkins: criar job nodejsserver
No Jenkins: configurar repositório e Slack notifications 

No gitlab: configurar webhook no repositório nodejsserver

No Jenkins, job nodejsserver: marcar csm do gitlab para deploy automatico
