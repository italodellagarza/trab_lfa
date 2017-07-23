Este programa minimiza um autômato finito determinístico completo, no 
formato descrito no arquivo-texto exemplo, gerando o autômato resultante 
e a tabela de minimização. O programa, se necessário, também converte um AFD
incompleto em completo.

Uso:

./minimizar.py <automato-de-entrada>.txt <tabela-de-saida>.txt 
<automato-de-saida>.txt

O programa foi feito em Python 3.6.1 e testado usando GNU/Linux.

Na pasta arquivos_exemplo temos três autômatos no modelo que o programa lê.
Caso o usuário deseje usar o código em outro autômato, este deverá seguir o seguinte padrão:
(
{<nome_dos_estados_separados_por_vírgula>}
{<alfabeto_separado_por_vírgula>}
{
(<transicao1.estado1>,letra-><transicao1.estado2>),
...
(<transicaoN.estado1>,letra-><transicaoN.estado2>)
}
<estado_inicial>,
{<estados_finais>}
)

O uso de uma sintaxe diferente para o autômato pode acarretar em mau funcionamento do código.
