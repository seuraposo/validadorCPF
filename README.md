# validadorCPF
Validador CPF  em python

Esse arquivo apresenta uma classe que recebe um numero, primeiro limpa qualquer ".","-" e " ".

Após isso ele valida o primeiro valor seguindo as regras de validação de CPF, após a volidação der OK é habilitada a verificação do segundo digito,
Nessa segunda validação e utilizado o valor original do numero recebido pois só realiza essa etapa com a validação do primeiro digito, assim validando o segundo digito segundo a formula de validação,
assim não sendo necessário utilizar diretamento o codigo da primeira validação tornando o codigo mais legivel e também impedindo que se chame a segunda validação sem ter feito primeira diretamente.
Com ambas as validações retornando True o CPF e validado.
