# parfeito
Curtidor automatizado do site de relacionamentos Par Perfeito utilizando Python e Selenium

### Primeiramente
Por quê??? Porque a vida de solteiro é difícil e ficar dando like em app de relacionamento todo dia também.

### Ok, mas par perfeito???
Foi o único site de relacionamento que eu encontrei que 1) funcionava em browser e 2) tem likes ilimitados na conta free.

### Certo, como isso funciona então
O bom e velho selenium, encontrando onde clicar pelo xPath dos elementos. Basicamente ele vai abrir o site, aceitar os cookies, colocar seu usuário e senha e começar a dar likes. Coloquei também pra pular a opção de enviar mensagem sobre algum assunto quando isso aparecer. Caso você passe pela parte do login repetidas vezes num curto período de tempo por algum motivo, isso vai ativar o sistema de captcha, então coloquei um "Deseja continuar?" para o programa esperar você inserir manualmente o captcha, depois de inserido basta dar um enter ou digitar "n" se quiser parar.

### O que eu preciso pra rodar?
Claramente criar uma conta no [Par Perfeito](https://www.parperfeito.com.br/), depois é só incluir seu usuário e senha no arquivo "secrets.py". Depois disso, falta apenas instalar o selenium:
```
pip install selenium
```
e ter o arquivo chromedriver.exe (que vai ser usado pra abrir o Chrome automatizado) no seu PATH ou na pasta que esteja rodando o código. Como eu não acho legal colocar .exe aqui no github, vou deixar o site aqui para baixarem a última/melhor versão para o seu caso: https://chromedriver.chromium.org/downloads

### Recomendações
O Par Perfeito só tem limites até o ponto onde não houver mais pessoas para te recomendar, então recomendo (rs) diminuir o máximo de restrições (idade, distância, etc.) para poder maximizar o número de likes, mas aí também vai de você, por isso que é uma *recomendação*.

### Problemas
A única coisa até então que eu vi dar problema é que aparentemente chega um momento em que ele "cansa" kkkkk mas isso já vai acionar a pergunta "Deseja continuar?" (se ela já não foi acionada lá no começo no captcha), então é só dar um enter que ele volta ao estado "dar likes infinitos". Na pior das hipóteses, é só reiniciar o bot (ou resolver o problema, mas daí eu deixo pra vocês).

### Agradecimentos
Eu basicamente só adaptei esse [vídeo](https://www.youtube.com/watch?v=lvFAuUcowT4) e esse [repositório](https://github.com/aj-4/tinder-swipe-bot) pra funcionar com o Par Perfeito ao invés do Tinder.
