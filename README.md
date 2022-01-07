
<div>
<h1 align="center">WhatsApp API Python ChatBot</h1>
<p align="center">Este repositório contém uma aplicação que se utiliza da API do Moorse para envio e recebimento de mensagens, tornando possível, a partir do uso de uma simples base de dados como o sqlite, a simulação de atendimento de uma pizzaria.</p>
<h4 align="center">
	<strong>
		<a href="https://whatsapp.moorse.io/">Nosso Site</a>
		<span> · </span>
		<a href="https://moorse.readme.io/">Documentação</a>
	</strong>
</h4>

# Como usar? 

## :mag: Pré-instalação

Para utilizar esta aplicação, é necessário antes de tudo estar registrado em nosso <a href="https://app.moorse.io/">site</a>, apenas necessitamos do seu e-mail e uma senha que você pode escolher e tudo estará pronto.

## :rocket: Instalando e configurando a aplicação
Este tópico objetiva concluir corretamente a instalação e configuração do projeto. 

O primeiro requisito para conseguir executar esta aplicação com sucesso é ter o Python 3 instalado corretamente em sua máquina, para isso, segue <a href="https://www.python.org/">link</a> da página oficial do Python para download e instalação do mesmo. Após tê-lo instalado certifique-se de ter instalado o pip (instalador de módulos do Python) juntamente ao Python. Sua instalação pode ser verificada pela simples execução no terminal do comando `pip` quando em Linux, entretanto, se o usuário utilizar Windows podem haver 3 combinações diferentes para chamada do pip, são elas:
 
1. `python -m pip`
2. `python3 -m pip`
3. `py -m pip`

Tal variação ocorre porque o caminho do `pip` não vem por padrão no caminho da variável PATH, entretanto, para sanar tal variação, recomenda-se fortemente que o usuário adicione o caminho do `pip` à variável de ambiente PATH, para que possa utilizar o `pip` igualmente no Linux e no Windows.

_(A partir daqui, consideraremos que o leitor usuário de Windows já colocou o caminho do pip dentro da variável PATH, porém, é possível continuar a leitura da documentação tendo que lidar com as três possibilidades de utilização do pip.)_

Pós instalação do Python e do pip, devemos instalar os pacotes necessários à utilização da aplicação. Tais pacotes se encontram na raiz do projeto dentro do arquivo `requirements.txt`, para a instalação destes basta executar o comando `install` do pip com o argumento `-r` que servirá para ler o arquivo `requirements.txt`. Então, vá até a pasta onde o requirements.txt está e no terminal/cmd utilize: 

`pip install -r requirements.txt`

Agora com todas as dependências instaladas, entre na pasta resources do repositório e edite o arquivo `application.yml`, aqui, basta adicionar seu token e sua integração desejada nos respectivos lugares indicados no arquivo. Para conseguir tais dados siga os passos:

- Para conseguir o token, logue na sua conta do Moorse e em *dashboard*, vá até o canto superior direito e clique em "copiar token de acesso".

- De forma semelhante à de conseguir o token, para conseguir o id da sua integração logue na sua conta do Moorse e na aba lateral esquerda clique em *whatsapp*, quando ver sua integração desejada clique no ícone de engrenagem (*Gerenciar integração*),  após isso, sua integração surge na URL do site, basta retirar ela de lá.

## :computer: Configurando o webhook

Este é o último passo da configuração para que você consiga utilizar a API do Moorse. Para que nossa API lhe envie requisições HTTP quando mensagens forem enviadas ao seu Whatsapp, é necessário que ela conheça seu IP, entretanto, isso nem sempre é possível,  e para facilitar tal comunicação, utilizaremos o <a href="https://ngrok.com/">ngrok</a>, ele será responsável por receber as requisições da API do Moorse e, então, redirecioná-las ao seu computador, assim, certifique-se de <a href="https://ngrok.com/download">baixá-lo</a> e instalá-lo  corretamente.

Agora com o ngrok instalado, precisamos criar nosso ip remoto, para isso, use o comando:

`ngrok http 8080`

Isso faz o ngrok criar um ip remoto que quando recebe uma requisição, redireciona-a ao seu computador. Agora com nosso ip remoto em mãos, precisamos avisar à API da Moorse que queremos receber informações das novas mensagens nesse ip, para isso, logue em sua conta da <a href="https://app.moorse.io/">moorse</a> e na aba lateral clique em webhook, vá até _adicionar novo webhook_, escolha o método _POST_, e na URL coloque o ip remoto fornecido pelo ngrok seguido por /webhooks (Observe que sempre que o ngrok for desligado será necessário refazer toda esta parte).

Tudo pronto!

Sua aplicação e seus webhooks foram totalmente configurados.

## :gear: Executando a aplicação :gear:

A aplicação principal fica dentro da pasta app, o arquivo é nomeado de `main.py`, basta executá-lo para que o bot seja ligado e receba as requisições enviadas pela API do Moorse.

## Moorse support free on Whatsapp, Telegram and Discord
	
|Whatsapp|Telegram|Discord|
|---|---|---|
|<a display="inline" target="_blank" href="https://web.whatsapp.com/send?phone=5511975923164&text=oi" target="_blank"><img align="center" title="whatsapp" height="50" width="50" src="images/whatsapp.png"/></a>|<a display="inline" float="left" target="_blank" href="https://t.me/moorseio" target="_blank"><img title="Telegram" height="50" width="50" src="images/telegram.png" align="center"/></a>|<a display="inline" target="_blank" href="https://discord.gg/uPp2SmCA" target="_blank"><img src="images/discord.png" height="50" width="50" align="center"></a>|
