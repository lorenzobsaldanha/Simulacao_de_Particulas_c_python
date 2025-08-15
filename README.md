# Simulacao_de_Particulas_c_python
O repositório possui os arquivos particle_sim em C e python, e um Makefile capaz de realizar a conexão entre as duas linguagens.
Ao entrar no repositório em um prompt e usar o comando "make", o arquivo libparticle_sim.so será criado, para assim poder executar os comandos "make caso_estudo1", "make caso_estudo2" e "make caso_estudo3" para mostrar uma simulação de partículas com 7, 35 e 100 partículas, respectivamente.

O código python necessita da instalação das bibliotecas matplotlib e numpy
Em Windows isso pode ser feito com os comandos "pip install matplotlib" e "pip install numpy" 


Make é um comando natural de linux, entretanto para usuários de Windowns este comando precisa ser configurado. Seguem os seguintes passos para implementar o uso de make no prompt do Windows:

-Baixe GnuWin no site: https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81.exe/download?use_mirror=sitsa&download

-Execute o setupwizard, apenas clicando em prosseguir. A única opção que não está previamente assinalada é a de concordar com os termos de serviço.

-Após concordar, não precisa alterar ou marcar nenhuma das opções que já estão marcadas, apenas vá prosseguindo.

-Ao finalizar o setupwizard do GnuWin, ainda é necessário configurá-lo como variável de usuário.

-Para isso, vá até C:\Program Files (x86)\GnuWin32\bin, copie este caminho, pressione a tecla "windows" do seu teclado e digite "var".

-Isso já deve ser o suficiente para que apareça o aplicativo "Editar as variáveis de ambiente do sistema". Abra-o, clique no botão "variaveis de ambiente",
dê dois cliques na palavra "Path" do retângulo superior, após isso clique em "novo" e cole o caminho que você havia copiado antes ("C:\Program Files (x86)\GnuWin32\bin")

-Clique em todos os botões "ok" que estiverem aparecendo na tela e parabéns, você pode usar o comando "make" no terminal agora!

