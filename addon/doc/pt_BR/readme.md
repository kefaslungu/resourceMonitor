# Monitor de Recursos (Resource Monitor)

* Autores: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst e outros colaboradores do NVDA

Este complemento fornece informações sobre carga da CPU, uso de memória e outras informações de uso de recursos.

## Atalhos

Todos os comandos suportam o modo de fala sob demanda.

* NVDA+Shift+E: apresenta uso da ram (memória), carga média do processador, e informações de bateria caso disponível.
* NVDA+Shift+1: apresenta a carga média do processador e caso se tratem de CPUs multinúcleo (multicore) mostra a carga de cada núcleo.
* NVDA+Shift+2/5: apresenta espaço usado e total das memórias ram física e virtual.
* NVDA+Shift+3: apresenta espaço usado e o total das unidades fixas e removíveis.
* NVDA+Shift+4: apresenta porcentagem da bateria, status de carga, tempo restante (se não estiver carregando) e alerta caso a bateria esteja baixa ou crítica.
* NVDA+Shift+6: apresenta a arquitetura da CPU e os números da versão do Windows e do service pack.
* NVDA+Shift+7: apresenta o tempo de atividade do sistema (tempo desde a inicialização).
* NVDA+Shift+8: apresenta informações sobre a conexão sem fio, nome e intensidade do ssid ou nenhum ssid, se não houver nenhum disponível.

Você pode alterar essas teclas de atalho por meio da caixa de diálogo de gestos de entrada.

## Notas de uso

Este complemento não substitui o gerenciador de tarefas e outros programas de informações de sistema para Windows. Note também o seguinte:

* As informações de recursos não podem ser copiadas para a área de transferência se o complemento for executado em telas seguras.
* O uso da CPU é fornecido para processadores lógicos, não para núcleos físicos. Isso é perceptível nos processadores que usam Hyper-Threading, em que o número de CPUs é o dobro do número de núcleos da CPU. Em alguns computadores mais novos, nem todos os núcleos da CPU terão o hyper-threading ativado.
* Se houver atividade intença de disco, como ao copiar arquivos grandes, pode haver lentidão ao obter informações de uso do disco.
* Ao anunciar informações sobre a arquitetura do processador, “x86” e “AMD64” referem-se aos processadores Intel e AMD de 32 e 64 bits (x64), respectivamente.
* Esse complemento requer o Windows 10 22H2 (2022 Update/build 19045) ou posterior.
* Não há suporte para a instalação do complemento no Windows 10/11 LTSC.
