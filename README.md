<div align="center">
  <h1>🔑 CRIPTOGRAFIA RSA 🔒</h1>
  <strong>
    <p>Suposta frase daora</p>
  </strong>
  <br><br>
</div>

<div>
  <p>Este é um estudo do funcionamento matemático e lógico da criptografia assimétrica RSA. Nesse programa abordo o algoritmo de Teste de Primalidade de Miller-Rabin, a estrutura lógica da criação de chaves publicas e privadas e seu funcionamento para a criptografia de dados.</p>
  <div align="center">
    <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3Vjc29rbmM3enpuMnY3eXRuZDg1ZGRiMjZ0cG91ZG0ycmU5a3hzMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OMK7LRBedcnhm/giphy.gif" width="600px" height="200px">
  </div>
  <br>
</div>

<div>
  <h2 align="center">O PRINCIPIO</h2>
  <p>Partindo com base na troca segura de informação, entre o ponto <strong>A</strong> e o ponto <strong>B</strong>, temos o seguinte fluxo da criptografia:</p>
  <ol>
    <li>Ponto <strong>A</strong> e <strong>B</strong> geram suas chaves criptograficas (Privada, Pública).</li>
    <br>
    <li>Ponto <strong>A e</strong> <strong>B</strong> trocam suas chaves Públicas.</li>
    <br>
    <li>
      Ponto <strong>A</strong> criptografa os dados com a chave Pública de <strong>B</strong> e <strong>B</strong> descriptografa os dados com sua chave Privada.
    </li>
    <br>
    <li>
      Ponto <strong>B</strong> criptografa os dados com a chave Pública de <strong>A</strong> e <strong>A</strong> descriptografa os dados com sua chvave Privada.
    </li>
  </ol>
  <br>
  <div align="center">
    <img src="https://dhg1h5j42swfq.cloudfront.net/2022/11/07211315/criptografiaassimetrica.png" width="600" heigth="300">
  </div>
</div>
