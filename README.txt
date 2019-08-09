Criar container com gitlab;
    docker-compose up -d gitlab
   
Criar conta e repositório no gitlab; 
    http://localhost:9090/
    http://localhost:9090/projects/new > agenda_mysql
    http://localhost:9090/projects/new > nodejsserver
    
    Permitir solicitações para a rede local de ganchos e serviços
        http://localhost:9090/admin/application_settings/network
            [x] Allow requests to the local network from hooks and services

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

Criar container para aplicação agenda;
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

Configurar o Jenkins para a primeira aplicação;
    criar ssh server > http://localhost:8080/configure
        name: agenda
        hostname: 192.168.77.130
        username: matheus
        remote Directory: /home/matheus/automatic-deploy/agenda
        Passphrase / Password: xxx
       
    criar job agenda
        No job agenda: configurar repositório GIT e Slack notifications
            Repository URL: http://gitlab/root/agenda_mysql
            Build > Send files or execute commands over SSH:
                Name: agenda
                Source files: **/*
                Exec command: docker restart agenda
            Post-build actions > slack notifications > advanced
                Slack compatible app URL (necessary): https://automatic-deploy.slack.com/services/hooks/jenkins-ci
                Integration Token: xwpxSs3JahkYitUZNvRsayA8
            # Test aplication #

Criar container para a aplicação nodejsserver;
    docker-compose up -d nodejsserver

Configurar o Jenkins para a segunda aplicação;
    criar ssh server > http://localhost:8080/configure
        name: nodejsserver
        hostname: 192.168.77.130
        username: matheus
        remote Directory: /home/matheus/automatic-deploy/nodejsserver
        Passphrase / Password: xxx
       
    criar job nodejsserver;
        No job nodejsserver: configurar repositório GIT e Slack notifications
            Repository URL: http://gitlab/root/nodejsserver
            Build > Send files or execute commands over SSH:
                Name: nodejsserver
                Source files: **/*
                Exec command: docker restart nodejsserver
            Post-build actions > slack notifications > advanced
                Slack compatible app URL (necessary): https://automatic-deploy.slack.com/services/hooks/jenkins-ci
                Integration Token: xwpxSs3JahkYitUZNvRsayA8
            # Test aplication #

No job nodejsserver: 
    Build Triggers:
        [x] Build when a change is pushed to GitLab. GitLab webhook URL: http://localhost:8080/project/nodejsserver
        Advanced > generete secret token

No gitlab: configurar webhook no repositório nodejsserver
    http://localhost:9090/root/nodejsserver/-/settings/integrations
        URL: http://jenkins:8080/project/nodejsserver
        Secret Token: xxx
    
    
No Jenkins, job nodejsserver: marcar csm do gitlab para deploy automatico
