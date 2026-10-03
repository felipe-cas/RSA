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

1. Ponto **A** e **B** geram suas chaves criptograficas (Privada, Pública).
2. Ponto **A** e **B** trocam suas chaves Públicas.
3. Ponto **A** criptografa os dados com a chave Pública de **B**
  - **B** descriptografa os dados com sua chave Privada.
5. Ponto **B** criptografa os dados com a chave Pública de **A**
  - **A** descriptografa os dados com sua chave Privada.

<div align="center">
    <img src="https://dhg1h5j42swfq.cloudfront.net/2022/11/07211315/criptografiaassimetrica.png" width="600" heigth="300">
</div>
<br><br>

<h2 align="center">MATEMÁTICA SIMPLIFICADA 🤓</h2>

A matemática por trás da geração das chaves toma como base a multiplicação de dois numeros primos gigantes (é considerado seguro partir com numeros de 2048 bits, equivalente a cerca de 617 digitos).  
Mas como certificar que os numeros escolhidos são realmente primos? Utilizamos o algoritmo de Miller-Rabin.  
O mesmo se aplica da seguinte maneira:

<br>

### 1. TESTE BASICO
Escolhemos um numero aleatório e fazemos divisões simples por valores baixos para já eliminar numeros obvios, como numeros pares ou multiplos de 3 ou 5 por exemplo.

``` python
nums_primos = [2, 3, 5]

def teste_basico(n):
    for p in nums_primos:
        if p > n//2:
            break

        if n%p == 0:
            return True
        
    return False
```
