Criar container com gitlab;
    docker-compose up -d gitlab
   
Criar conta e repositório no gitlab; 
    http://localhost:9090/
    http://localhost:9090/projects/new > agenda_mysql
    http://localhost:9090/projects/new > nodejsserver

Fazer push das aplicações;
    cd ~/automatic-deploy/gitlab/app/agenda_mysql
        git init
        git remote add origin http://localhost:9090/root/agenda_mysql.git
        git add *
        git commit -m 'redondinho'
        git push origin master
    
    cd ~/automatic-deploy/gitlab/app/nodejsserver
        git init
        git remote add origin http://localhost:9090/root/nodejsserver.git
        git add *
        git commit -m 'redondinho'
        git push origin master


Criar container com MySQL; 
    cd ~/automatic-deploy
    docker-compose up -d mysql
    
Criar
    

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
