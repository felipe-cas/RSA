<div align="center">
  <h1>🔑 CRIPTOGRAFIA RSA 🔒</h1>
  <strong>
    <p>Suposta frase daora</p>
  </strong>
</div>

***

Este é um estudo do funcionamento matemático e lógico da criptografia assimétrica RSA. Nesse programa abordo o algoritmo de Teste de Primalidade de Miller-Rabin, a estrutura lógica da criação de chaves publicas e privadas e seu funcionamento para a criptografia de dados.

<div align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3Vjc29rbmM3enpuMnY3eXRuZDg1ZGRiMjZ0cG91ZG0ycmU5a3hzMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OMK7LRBedcnhm/giphy.gif" width="600px" height="200px">
</div>
<br><br>
<h2 align="center">O PRINCIPIO</h2>

Partindo com base na troca segura de informação, entre o ponto **A** e o ponto **B**, temos o seguinte fluxo da criptografia:

1. Ponto **A** e **B** geram suas chaves criptográficas (Privada, Pública).
2. Ponto **A** e **B** trocam suas chaves Públicas.
3. Ponto **A** criptografa os dados com a chave Pública de **B**
>**B** descriptografa os dados com sua chave Privada.
4. Ponto **B** criptografa os dados com a chave Pública de **A**
>**A** descriptografa os dados com sua chave Privada.

<div align="center">
    <img src="https://dhg1h5j42swfq.cloudfront.net/2022/11/07211315/criptografiaassimetrica.png" width="600" heigth="300">
</div>
<br><br>

<h2 align="center">MATEMÁTICA SIMPLIFICADA 🤓</h2>

A matemática por trás da geração das chaves toma como base a multiplicação de dois números primos gigantes (é considerado seguro partir com números de 2048 bits, equivalente a cerca de 617 digitos).  
Mas como certificar que os números escolhidos são realmente primos? Utilizamos o algoritmo de Miller-Rabin.  
O mesmo se aplica da seguinte maneira:

<br>

### 1. TESTE BÁSICO
Escolhemos um numero aleatório e fazemos divisões simples por valores baixos para já eliminar numeros óbvios, como numeros pares ou múltiplos de 3 ou 5 por exemplo.

``` python
for p in lista_nums:
  if num_aleatorio % p == 0:
    return False
  return True
```
> Se o resultado da modularização for 0, pode descartar o numero e gerar um novo.

<br>

### 2. DECOMPOSIÇÃO
Decompomos o numero aleatório de forma a representá-lo na equação $2^s * d = n - 1$ onde $d$ é interio impar e $s$ potência inteira de 2.

```
n = 67

(2 ^ s) *  d ==  n - 1
(2 ^ 1) * 33 == 67 - 1

d = 33
s =  1
```

<br>

### 3. TESTES SEMI DEFINITIVO
Os testes semi definitivos são divididos na verificação da veracidade de duas equações.

***

#### PRIMEIRO TESTE
Testamos a equação $a^d = ((n - 1) \parallel 1) (mod)$ sendo $a$ um numero aleatório entre **0** e **n-1**

``` python
a = randint(0, n-2)
res = pow(a, d, n)
if (res == 1) or (res == n-1):
  return True
```
> Se o resultado for **1** ou **n-1** ele passou no primeiro teste e não será necessário fazer o segundo teste.

#### SEGUNDO TESTE
Caso de um resultado diferente e não passe no primeiro teste, recorremos a equação $resultado ^ 2 = n - 1 (mod)$. Nesse segundo teste temos uma particularidade, repetiremos ele $s - 1$ vezes até uma das seguintes condições se tornem verdadeiras: 
- $s = 0$
- $resultado = n -1$
- $resultadoAtual = 1 \land resultadoAnterior != n - 1$

> Toda vez que repetimos o teste, usamos o resultado de volta na equação

``` python
for _ in range(0, s-1):
  new = pow(res, 2, n)

  if (new == 1) and (res != (n - 1))
    return False

  elif new == (n - 1):
    break

  res = new

else:
  return False
```

> Caso ele não caia em nenhuma da condições acima, o numero não é primo


**ATENÇÃO**: O teste de Miller-Rabin é considerado um teste Semi-Probabilístico (assim é como gosto de chamar, mas o termo técnico correto seria Algoritmo de Monte-Carlo). É um texto com tempo limite de execução determinístico, porem o resultado com uma margem de erro probabilística.  
Um segundo ponto a se considerar é seu resultado probabilístico, quando o algoritmo disser que o numero não é primo, a resposta é 100% determinístico e sem margens de erro, porem quando acusar que o resultado é primo, terá uma pequena margem de erro, sendo então considerado um provável primo. Para diminuirmos a margem de erro, podemos repetir o algoritmo k vezes para o mesmo numero. Essa foi a sacada genial de Michael O. Rabin.

<h2 align="center">🔑 GERANDO AS CHAVES 😎</h2>

Finalmente é chegada é hora de gerar as chaves! É sempre bom lembrar que a criptografia RSA é assimétrica, isso significa que possui duas chaves diferentes, uma pública usada para criptografar e uma privada para descriptografar.

<br>

Para gerar ambas as chaves, devemos escolher dois numeros primos grandes (2048 bits) e multiplicarmos um pelo outro, gerando o numero $n$, usaremos os numeros $p = 17$ e $q = 41$ para simplificar nosso exemplo:

```python
p = 17
q = 41

n = p * q  #17 * 41 = 697
```
> Esse valor $n$ será usado em ambas as chaves

<br>

Logo após, definimos a Função Totiente de Euller, também conhecida como $\phi$ (phi), para o valor de N. Sua formula se descreve da seguinte maneira: $\phi = (p - 1) * (q - 1)$

```python
phi = (p-1) * (q-1)  #(17-1) * (41-1) = 16 * 40 = 640
```

<br>

### Chave Pública

Para criar a chave pública, devemos escolher um valor para E, que atenda as seguintes condições:

- E > 1
- E < phi(n)
- E coprimo de phi(n)

> Nesse exemplo, escolhi o numero 13, sendo $mdc(640, 13) == 1$

Nessa etapa, nossa chave pública já esta pronta, sendo o conjunto N e E

```python
n = 697
e = 13
chavePublica = [n, e]
```

<br>

### Chave Privada

Para criar a chave privada, usaremos o valor de phi e E, definidos anteriormente, para gerar o valor D, segundo a condição: $(d * e) mod \phi == 1$  
Dessa forma, nossa chave privada também ja esta pronta, sendo o conjunto N e D

```python
n = 697
d = pow(e, -1, phi)  # pow(13, -1, 640) = 197
chavePrivada = [n, d]
```
<br>

<h2 align="center">🔒 Processo de Criptografia e Descriptografia 🔑</h2>

O processo de criptografia e descriptografia são relativamente simples de se aplicar, usaremos a função inverso modular em cada caractere ascii da mensagem, usando a chave pública para criptografar e a privada para descriptografar.

### Criptografando mensagem

```python
n = 697
e = 13
chavePublica = [n, e]

# 111 == 'o'; 105 =='i'
msg = [111, 105]

# Para cada caractere ascii da mensagem, elevamos em E, e aplicamos o modulo de N
msgCriptografada = [pow(c, chavePublica[1], chavePublica[0]) for c in msg]

# msgCriptografada == [110, 318]
```

<br>

### Descriptografando mensagem

```python
n = 697
d = 197
chavePrivada = [n, d]

# msgCriptografada == [110, 318]

# Para cada caractere da mensagem criptografada, elevamos em D, e aplicamos o modulo de N
msgDescriptografada = [pow(c, chavePrivada[1], chavePrivada[0]) for c in msgCriptografada]

# msgDescriptografada == [111, 105]
```

<br>

<h2 align="center">📚 Conclusão 🌐</h2>

Esse projeto trata apenas a matematica basica da criptografia RSA. Atualmente foram implementadas diversas técnicas e avanços com o intuito de tornar a criptgrafia mais rápida, viável e segura.  

<br>

### **PRINCIPAIS IMPLEMENTAÇÕES**

|       Aplicação      |                    Descrição                    |
|:---------------------|:------------------------------------------------|
| Certificados SSL/TLS | Autenticação e troca de chaves simétricas       |
| Assinaturas Digitais | Verifica Autenticidade e a Integridade de dados |
| SSH                  | Autenticação de Servidores e Usuarios           |
| VPN                  | Autenticação e Troca de chaves                  |
| Blockchains          | Assinatura de transações                        |


<br>

### **IIMPLEMENTAÇÃO SEGURA**

Apesar de ser computacionalmente inviavel tentar quebrar uma chave RSA com a tecnologia que temos hoje ou algum dia teremos, é de extrema importância que sua implementação seja seguramente bem feita, assim, evitando ataques matematicos e de padding!  
> Recomenda-se seguir as normas da NIST SP 800-57 para gerenciamento de chaves criptograficas.

<br>

#### BOAS PRATICAS

- Tamanho minimo da chave de 2048 bits
- Utilizar padding OAEP (Evite PKCS#1 v1.5)
- Utilizar E com o valor padrão 65537 (Já testado e consagrado)
- Não utilizar RSA para grande volume de dados (lento)
- Utilizar geradores pseudo-aleatórios seguros para P e Q (Não use os de propósito geral)
- **NUNCA EXPONHA A CHAVE PRIVADA**

<br>

### **ALTERNATIVAS AO RSA**

| Algoritimo    | Vantagens                   | Desvantagens                             |
|:--------------|:----------------------------|:-----------------------------------------|
| RSA           | Amplamente Suportado        | Chaves grandes, Computacionalmente lento |
| ECC           | Chaves menores, mais rápido | Pouco Auditado                           |
| AES           | Alta segurança, mais rápido | Manuseio de chaves complexa(Simétrica)   |

> O recomendado é interpolar os algoritimos, por exemplo, RSA para troca de chaves e AES para envio de conteudo

<br>
<h2 align="center">Referências 📚</h2>
<br>

- [Biblia do Pentest](https://github.com/morteerror404/BibliaDoPentestBR) - ```https://github.com/morteerror404/BibliaDoPentestBR```

- [Calculadora Miller-Rabin](https://pt.planetcalc.com/8995/) - ```https://pt.planetcalc.com/8995/```

- [The RSA Cryptosystem](https://cryptobook.nakov.com/asymmetric-key-ciphers/the-rsa-cryptosystem-concepts) - ```https://cryptobook.nakov.com/asymmetric-key-ciphers/the-rsa-cryptosystem-concepts```

- [Criptografia Assimétrica RSA](https://medium.com/@tarcisioma/algoritmo-de-criptografia-assim%C3%A9trica-rsa-c6254a3c7042) - ```https://medium.com/@tarcisioma/algoritmo-de-criptografia-assim%C3%A9trica-rsa-c6254a3c7042```

- [Introdução à criptografia RSA](https://www.youtube.com/watch?v=rvdI-uhvQgc) - ```https://www.youtube.com/watch?v=rvdI-uhvQgc```

- E muita I.A
