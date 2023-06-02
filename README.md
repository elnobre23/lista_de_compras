<body>
  <h1>Documentação do Código: Lista de Compras</h1>
  <p>
    Este código em Python implementa uma lista de compras interativa, onde o usuário pode adicionar itens, marcar itens como pagos, listar os itens da lista e sair do programa.
  </p>

  <h2>Importação</h2>
  <p>
    O código utiliza a biblioteca <code>os</code> para executar o comando de limpar a tela do console.
  </p>

  <h2>Lista de Compra</h2>
  <p>
    A lista de compras é representada por uma lista vazia inicialmente:
    <code>lista_de_compra = []</code>.
  </p>

  <h2>Opções</h2>
  <p>
    O código oferece as seguintes opções para o usuário:
  </p>
  <ul>
    <li><code>i</code>: Inserir um item na lista de compras.</li>
    <li><code>a</code>: Pagar um item da lista de compras.</li>
    <li><code>l</code>: Listar os itens da lista de compras.</li>
    <li><code>s</code>: Sair do programa.</li>
  </ul>

  <h2>Laço Principal</h2>
  <p>
    O código utiliza um laço <code>while True:</code> para continuar a execução até que o usuário decida sair do programa.
  </p>
  <p>
    Dentro do laço, o código realiza as seguintes etapas:
  </p>
  <ol>
    <li>
      <code>opcao = input('Selecione uma opção:\n[i]nserir, [a]pagar, [l]istar ou [s]air: ').lower()</code>: Solicita ao usuário que selecione uma opção digitando a letra correspondente e converte a entrada para minúsculo.
    </li>
    <li>
      <code>if opcao in opcoes:</code>: Verifica se a opção fornecida pelo usuário está na lista de opções válidas.
      <ul>
        <li><code>if opcao == opcoes[0]:</code>: Verifica se a opção é 'i' (inserir).
          <ul>
            <li><code>adicionar_compra = input('Adicione um item: ')</code>: Solicita ao usuário que adicione um item à lista de compras e armazena a entrada na variável <code>adicionar_compra</code>.</li>
            <li><code>lista_de_compra.append(adicionar_compra)</code>: Adiciona o item à lista de compras utilizando o método <code>append()</code>.</li>
          </ul>
        </li>
        <li><code>elif opcao == opcoes[1]:</code>: Verifica se a opção é 'a' (pagar).
          <ul>
            <li><code>i = int(input('Selecione um índice para apagar: '))</code>: Solicita ao usuário que selecione um índice da lista de compras para apagar e converte a entrada para o tipo <code>int</code>.</li>
            <li><code>try:</code>: Inicia um bloco de tratamento de exceção para lidar com o possível erro de índice inválido.
              <ul>
                <li><code>apagar_compra = lista_de_compra.pop(i)</code>: Remove o item da lista de compras no índice especificado utilizando o método <code>pop()</code> e armazena o item removido na variável <code>apagar_compra</code>.</li>
              </ul>
            </li>
            <li><code>except IndexError:</code>: Captura a exceção de índice inválido caso ocorra.
              <ul>
                <li><code>print('Não foi possível apagar esse índice.')</code>: Exibe uma mensagem de erro informando que não foi possível apagar o índice fornecido.</li>
                <li><code>continue</code>: Continua para a próxima iteração do laço utilizando a instrução <code>continue</code>.</li>
              </ul>
            </li>
          </ul>
        </li>
        <li><code>elif opcao == opcoes[2]:</code>: Verifica se a opção é 'l' (listar).
          <ul>
            <li><code>for indice, item in enumerate(lista_de_compra):</code>: Itera sobre a lista de compras utilizando a função <code>enumerate()</code> para obter o índice e o item correspondente.
              <ul>
                <li><code>print(indice, item)</code>: Exibe o índice e o item da lista de compras.</li>
              </ul>
            </li>
          </ul>
        </li>
        <li><code>else:</code>: Executa caso a opção seja 's' (sair).
          <ul>
            <li><code>os.system('cls')</code>: Executa o comando para limpar a tela do console (apenas em sistemas operacionais Windows).</li>
            <li><code>lista_de_compra = []</code>: Limpa a lista de compras.</li>
          </ul>
        </li>
      </ul>
    </li>
    <li>
      <code>else:</code>: Executa caso o usuário digite uma opção inválida.
      <ul>
        <li><code>print('Digite uma opção válida!')</code>: Exibe uma mensagem de erro informando que a opção digitada é inválida.</li>
      </ul>
    </li>
  </ol>

  <h2>Saída</h2>
  <p>
    O código exibe mensagens ao usuário para solicitar a entrada de opções, adicionar itens, exibir a lista de compras e informar sobre opções inválidas. As mensagens são formatadas com os valores dos itens e índices utilizando a função <code>print()</code>.
  </p>

</body>
</html>
