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
Caso de um resultado diferente e não passe no primeiro teste, recorremos a equação $resultado ^ 2 = n - 1 (mod)$. Nesse segundo teste temos um particularidade, repetiremos ele $s - 1$ vezes até uma das seguintes condições se tornem verdadeiras: 
- $s = 0$
- $resultado = n -1$
- $resultado_atual = 1 \land resultado_anterior != n - 1$

> Toda vez que repetimos o teste, usamos o resultado de volta na equação

``` python
for _ in range(0, s-1):
  new = pow(res, 2, n)

  if (new == 1) and (res != (n - 1))
    return False

  elif new == (n - 1):
    return True

  res = new

return False
```

> Caso ele não caia em nenhuma da condições
