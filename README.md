# Flamer (flaming)
1. To engage in an online argument usually involving unfounded personal attacks by one or more parties.

[ 🔥 ] Flamer é um projeto para passar o tempo, desenvolvido em Python, open-source, baseado em um tweet que apareceu na minha timeline. O tweet dizia sobre um amigo que tinha feito um bot que respondia todo post e retweet de outro (obviamente amigo também). Tendo essa premissa em mente, conclui-se que o Flamer é um bot que utiliza a API do Twitter para xingar automaticamente outra pessoa (mas pode servir para bons usos também xD).

### Como funciona?
Flamer tem um observador que detecta automaticamente quando a pessoa que você definiu realiza um tuíte, e quando acontece, ela extraí o texto contido naquele tweet, o traduz através da biblioteca Deep Translator,  processa simbolicamente e estatísticamente a linguagem natural contida no texto - detectando automaticamente a emoção contida -, então define se é um tweet positivo, neutro ou triste. Posteriormente escolhe randomicamente um xingamento de uma lista predefinida com na principal emoção contida no tweet, e o responde.

<p align="center">
  <img src="https://i.imgur.com/RMfks8z.png" width="150" align="center">
 </p>
## Iniciando o Flamer

1. Clone o repositório baixando-o diretamente ou através do comando:
```git
git clone https://github.com/koobzaar/flamer.git
```

2. Instale as dependências

```python
pip install -r requirements.txt
```

Perdão, fiquei com preguiça de fazer um requirements.txt, então se vira aí

3. Crie um arquivo .env na raiz da pasta, contendo as seguintes características:
```env
# Target
TWITTER_TARGET_USER_ID = "userid"

# Twitter API
TWITTER_API_KEY = 'apikey'
TWITTER_API_SECRET = 'apisecret'
TWITTER_ACESS_TOKEN = 'acesstoken'
TWITTER_SECRET_TOKEN = 'secretoken'
```

4. Adicione os xingamentos nos arquivos .fodase dentro da pasta insults - obviamente seguindo as emoções dos tweets
5. Inicie o Flamer com 
```py
py ./Flamer.py
```

6. Vai ná fé.


## Nuvem
O aplicativo já está praticamente pronto para ser upado para a Heroku. Crie o arquivo .env e siga este tutorial:
https://youtu.be/x8hVoalU0MA


## ATENÇÃO

Preciso nem dizer que tu precisa ter autorização da pessoa que você ta targeteando pra fazer isso, né babaca? Isso aqui foi feito pra brincar com um amigo, não com uma pessoa aleatória.
Também não me responsabilizo por qualquer idiotice que você faça com isso, nem com quem você brinca. Depois que você baixou, a responsabilidade é tua.

## Licença

MIT


