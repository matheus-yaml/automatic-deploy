1 #######################################################################################################################
2 Para agilizar... vamos baixar as seguintes images:
3     docker pull gitlab/gitlab-ce;  
4    docker pull mysql;
5    docker pull jupyter/minimal-notebook;
6    docker pull jenkins/jenkins:lts;
7    docker pull node


10 INSTALAR DOCKER: sudo curl –fsSL https://get.docker.com | bash 
11 INSTALAR DOCKER-COMPOSE: sudo apt-get install docker-compose
#######################################################################################################################

14 Clonar repositório: git clone https://github.com/matheusolivv/automatic-deploy

16 Criar container com gitlab;
17     docker-compose up -d gitlab
   
19 Criar conta e repositório no gitlab; 
20     http://localhost:9090/
21     http://localhost:9090/projects/new > agenda_mysql
22     http://localhost:9090/projects/new > nodejsserver
    
24     Permitir solicitações para a rede local de ganchos e serviços
25         http://localhost:9090/admin/application_settings/network
26             [x] Allow requests to the local network from hooks and services

28 Fazer push das aplicações;
29     cd ~/automatic-deploy/gitlab/app/agenda_mysql
30         git init
31         git remote add origin http://localhost:9090/root/agenda_mysql.git
32         git add *
33         git commit -m 'redondinho'
34         git push origin master
    
36     cd ~/automatic-deploy/gitlab/app/nodejsserver
37         git init
38         git remote add origin http://localhost:9090/root/nodejsserver.git
39         git add *
40         git commit -m 'redondinho'
41         git push origin master

43 Criar container com mysql; 
44     cd ~/automatic-deploy
45     docker-compose up -d mysql
    
47 Entrar no container mysql e executar script que restaura o banco de dados adaptando-o para a agenda;
48     docker exec -ti mysql bash
49     mysql -u root -p < /opt/contatos.sql
50     exit

52 Criar container para aplicação agenda;
53     docker-compose up -d agenda
54 Pegar token/password de login:
55     docker logs agenda
56     http://localhost:8888/

58 Instalar o Jenkins e copiar token/password;
59     docker-compose up -d jenkins
60     docker logs jenkins

62 Criar configurações iniciais do jenkins;
63     http://localhost:8080/
64         instalar plugins sugeridos
  
66 Configurar o Slack para as aplicações;
67     https://automatic-deploy.slack.com
68         invite friends > https://join.slack.com/t/automatic-deploy/shared_invite/enQtNzA5MjE5NTg4MzQyLTc3YzJjNjA4NjVjZDExNjgxYjQ0ZTNkMTU4NmQxNTM5YjQwMTQ0ZjQ3NTcwNjA4ZTY1NWIyMDhiOWNhYTZiYTc
69         adcionar apps > Jenkins CI > install > add configuration > get token FdN8CFq69ELjyK625Ufbuamv

71  Configurar plugins no jenkins;
72      http://localhost:8080/pluginManager/available
73         baixar plugins: publish over ssh; slack notifications e gitlab > restart

75 Configurar o Jenkins para a primeira aplicação;
76     criar ssh server > http://localhost:8080/configure
77         name: agenda
78         hostname: 192.168.77.130
79         username: matheus
80         remote Directory: /home/matheus/automatic-deploy/agenda
81         Passphrase / Password: xxx
       
83     criar job agenda
84         No job agenda: configurar repositório GIT e Slack notifications
85             Repository URL: http://gitlab/root/agenda_mysql
86             Build > Send files or execute commands over SSH:
87                 Name: agenda
88                 Source files: **/*
89                 Exec command: docker restart agenda
90             Post-build actions > slack notifications > advanced
91                 Slack compatible app URL (necessary): https://automatic-deploy.slack.com/services/hooks/jenkins-ci
92                 Integration Token: xwpxSs3JahkYitUZNvRsayA8
93             # Test aplication #

95 Criar container para a aplicação nodejsserver;
96     docker-compose up -d nodejsserver

98 Configurar o Jenkins para a segunda aplicação;
99     criar ssh server > http://localhost:8080/configure
100         name: nodejsserver
101         hostname: 192.168.77.130
102         username: matheus
103         remote Directory: /home/matheus/automatic-deploy/nodejsserver
104         Passphrase / Password: xxx
        
106     criar job nodejsserver;
107         No job nodejsserver: configurar repositório GIT e Slack notifications
108             Repository URL: http://gitlab/root/nodejsserver
109             Build > Send files or execute commands over SSH:
110                 Name: nodejsserver
111                 Source files: **/*
112                 Exec command: docker restart nodejsserver
113            Post-build actions > slack notifications > advanced
114                Slack compatible app URL (necessary): https://automatic-deploy.slack.com/services/hooks/jenkins-ci
115                Integration Token: xwpxSs3JahkYitUZNvRsayA8
116             # Test aplication #

118 No job nodejsserver: 
119     Build Triggers:
120        [x] Build when a change is pushed to GitLab. GitLab webhook URL: http://localhost:8080/project/nodejsserver
121        Advanced > generete secret token

123 No gitlab: configurar webhook no repositório nodejsserver
124     http://localhost:9090/root/nodejsserver/-/settings/integrations
125         URL: http://jenkins:8080/project/nodejsserver
126         Secret Token: xxx
    
128 No job agenda: 
129     Build Triggers:
130         [x] Build when a change is pushed to GitLab. GitLab webhook URL: http://localhost:8080/project/agenda
131         Advanced > generete secret token

133 No gitlab: configurar webhook no repositório agenda
134     http://localhost:9090/root/agenda/-/settings/integrations
135         URL: http://jenkins:8080/project/agenda
136        Secret Token: xxx
