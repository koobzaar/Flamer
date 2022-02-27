# Flamer (flaming)
1. Envolver-se em uma discussão online com ataques pessoais infundados ou sem sentido para uma ou mais pessoas.

[ 🔥 ] Flamer é um projeto para passar o tempo, desenvolvido em Python, open-source, baseado em um tweet que apareceu na minha timeline a respeito de um amigo que havia feito um bot para xingar todos os tweets e respostas que o outro amigo fizesse na rede.

<p align="center">
  <img src="https://i.imgur.com/RMfks8z.png" width="700" align="center">
 </p>
 
### Como funciona?
Flamer tem um observador que detecta automaticamente quando a pessoa que você definiu realiza um tuíte, e quando acontece, ela extraí o texto contido naquele tweet, o traduz através da biblioteca Deep Translator (pt->en),  processa simbolicamente e estatísticamente a linguagem natural contida no texto, assim detectando automaticamente a emoção contida; então define se é um tweet positivo, neutro ou triste. Posteriormente escolhe um xingamento aleatório de uma das listas, dependendo de qual sentimento foi detectado.

## Iniciando o Flamer

1. Clone o repositório baixando-o diretamente ou através do comando:
```git
git clone https://github.com/koobzaar/flamer.git
```

2. Instale as dependências

```python
pip install -r requirements.txt
```

3. Obtenha o ID do usuário que você quer definir como target. Você pode utilizar o TweeterID para isso. Então edite o arquivo .env na raiz da pasta, contendo as seguintes características:
```env
# Target
TWITTER_TARGET_USER_ID = "IDdoUsuarioVitima"

# Twitter API
TWITTER_API_KEY = 'chaveDeApiDoTwitter'
TWITTER_API_SECRET = 'chaveSecretDoTwitter'
TWITTER_ACESS_TOKEN = 'tokenDeAcesso'
TWITTER_SECRET_TOKEN = 'tokenSecreto'
```

4. Adicione os xingamentos nos arquivos .fodase dentro da pasta insults - obviamente seguindo as emoções dos tweets
5. Inicie o Flamer com 
```py
py ./Flamer.py
```


## Nuvem
O aplicativo já está praticamente pronto para ser upado para a Heroku. Crie o arquivo .env e siga este tutorial:
https://youtu.be/x8hVoalU0MA


## ATENÇÃO

Preciso nem dizer que tu precisa ter autorização da pessoa que você ta targeteando pra fazer isso, né babaca? Isso aqui foi feito pra brincar com um amigo, não com uma pessoa aleatória.
Também não me responsabilizo por qualquer idiotice que você faça com isso, nem com quem você brinca. Depois que você baixou, a responsabilidade é tua.

## Licença

MIT


