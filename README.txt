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

Criar container com mysql; 
    cd ~/automatic-deploy
    docker-compose up -d mysql
    
Entrar no container mysql e executar script que restaura o banco de dados adaptando-o para a agenda;
    docker exec -ti mysql bash
    mysql -u root -p < /opt/contatos.sql
    exit

Instalar a aplicação agenda;
    docker-compose up -d agenda
Pegar token/password de login:
    docker logs agenda
    http://localhost:8888/

Instalar o Jenkins e copiar token/password;
    docker-compose up -d jenkins
    docker logs jenkins

Criar configurações iniciais do jenkins;
    http://localhost:8080/
        instalar plugins sugeridos
  
Configurar o Slack para as aplicações;
    https://automatic-deploy.slack.com
        adcionar apps > Jenkins CI > install > add configuration > get token xwpxSs3JahkYitUZNvRsayA8

Configurar plugins no jenkins;
    http://localhost:8080/pluginManager/available
        baixar plugins: publish over ssh; slack notifications e gitlab > restart

Configurar o Jenkins para a primeira aplicação

No Jenkins: criar servidor ssh 
No Jenkins: criar job agenda
No job agenda: configurar repositório e Slack notifications

Criar aplicação nodejsserver

No Jenkins: criar servidor ssh nodejsserver
No Jenkins: criar job nodejsserver
No Jenkins: configurar repositório e Slack notifications 

No gitlab: configurar webhook no repositório nodejsserver

No Jenkins, job nodejsserver: marcar csm do gitlab para deploy automatico
