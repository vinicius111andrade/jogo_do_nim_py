# jogo_do_nim_py
Esse é um exercício programa em python que recria o chamado Jogo do NIM. Esse programa permite que você jogue contra o computador. O computador escolhe quem começa e usa a estratégia vencedora, por isso é impossível ganhar do computador. Faz parte do charme do jogo rs.

## Regras do Jogo do NIM
Uma pessoa começa e retira um número **n** de peças do tabuleiro, esse número **n** deve ser maior que 1 e não pode ser maior que o número **m** , que é o número máximo de peças a serem retiradas por jogada. Os jogadores alternam entre si e vão retirando peças, o jogador que retirar a última peça ganha o jogo.

## Porque é impossível ganhar do computador?
O computador escolhe quem começa verificando se o número de peças no tabuleiro é múltiplo de **m+1** ou não. Caso seja, o computador começa, caso não seja o usuário começa. Dessa forma seguindo a estratégia vencedora a vitória do computador estará garantida.

## Qual é a estratégia vencedora?
O computador deve sempre deixar um número de peças múltiplo de **m+1** para o jogador, caso isso seja impossível ele deve tirar o número máximo de peças possível.

## Especificações

----------------
computador_escolhe_jogada(n, m)
n, m inteiros

retorna um inteiro correspondente a quantas peças o comp deve retirar do tab
usando a estrategia vencedora


----------------
usuario_escolhe_jogada(n, m)
n, m inteiros

Solicita a jogada, verifica se eh valida, caso n pede uma jogada valida
Devolve uma jogada valida

-----------------

partida()

Solicita ao usuario q informe os valores de n e m (int) //checar se sao validos

Decide quem começa usando a estrategia vencedora

Alterna entre jogadores chamando as funções

A cada jogada o estado atual do jogo eh impresso, ou seja, quantas peças foram removidas
e quantas restam na mesa

Quando a ultima peça eh removida imprime na tela "O computador ganhou!" ou
"Você ganhou!"

------------------

campeonato()

campeonato tem 3 partidas seguidas
ao final mostra o placar e indica o vencedor

"Placar: Você ... X ... Computador"

------------------

Não chamar input() antes de def todas funções da problema no corretor, chamar dentro de func n tem problema

**

n = numero de peças inicial
m = numero max de peças que um jogador pode tirar por jogada

O numero min de peças q pode retirar são 1
Ganha quem tira as ultimas peças

Se n eh multiplo de m+1, o comp deve ser "generoso" e convidar o jogador
a iniciar com a frase "Você começa!"

Caso contrario, o computador toma a iniciativa de começar o jogo,
"Computador começa!"

Estrategia vencedora:
-comp deve sempre deixar um num de peças multiplo de m+1 ao jogador
-caso n seja possivel devera tirar o numero max de peças possivel
