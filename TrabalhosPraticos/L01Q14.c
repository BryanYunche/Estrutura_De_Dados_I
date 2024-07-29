#include <stdio.h>

//Ler a Matricula do funcionário, seu SALÁRIO BASE, ANO DE ADMISSÃO e NÚMERO DE DEPENDENTES.  
//Em seguida calcular e apresentar o salário líquido(RECEITAS-DESPESAS) com  base nos créditos e débitos a seguir: 
//CRÉDITOS 
//• 10% de reajuste salarial(reajuste); 
//• R$100.00 para cada 2 anos de tempo de serviço(biênio); 
//• R$50.00  para cada dependente( ajuda de custo); 
//DESPESAS 
//• 25% de INSS(calculado a partir do salário bruto); 
//• 50% de IMPOSTO DE RENDA(calculado a partir do salário bruto deduzido o INSS); 
//• R$ 75.00 por dependente mais o próprio( plano de saúde)

int main(){
    
    int numeroMatricula, anoAdmissao, numeroDependentes, tempoServico;
    double salarioBruto, salarioFinal;

    //Constantes Créditos
    #define REAJUSTE 0.10
    #define BONUS_BIENIO 100
    #define BONUS_DEPENDENTE 50
    #define ANO_ATUAL 2024

    //Constantes Despesas
    #define INSS 0.25
    #define IMPOSTO_RENDA 0.50
    #define DEPENDENTE_SAUDE 75

    //Funcionário Default
    numeroMatricula = 12345;
    anoAdmissao = 2010;
    numeroDependentes = 2;
    salarioBruto = 3000.00;
    salarioFinal = 0.0;

    //Tempo de serviço
    tempoServico = ANO_ATUAL-anoAdmissao;


    //Acrécimos do Salário
    salarioFinal = salarioFinal + (salarioBruto*REAJUSTE);
    salarioFinal = salarioFinal + ((tempoServico/2)*BONUS_BIENIO);
    salarioFinal = salarioFinal + (numeroDependentes*BONUS_DEPENDENTE);

    //Despesas Salario
    salarioFinal = salarioFinal - (salarioBruto*INSS);
    salarioFinal = salarioFinal - ((salarioBruto - (salarioBruto*INSS))*IMPOSTO_RENDA);
    salarioFinal = salarioFinal - DEPENDENTE_SAUDE - (DEPENDENTE_SAUDE*numeroDependentes);

    printf("Digite o número de matricula do funcionario: ");
    scanf("%d", &numeroMatricula);

    printf("Digite o ano de admissao: ");
    scanf("%d", &anoAdmissao);

    printf("Digite o valor de seu salario Base: ");
    scanf("%d", &anoAdmissao);

    printf("Digite o numero de dependentes: ");
    scanf("%d", &anoAdmissao);

    printf("Salario bruto: %f", salarioBruto);
    printf("Acressimos ao salario: %f", salarioBruto);
    printf("Despesas do salaria: %f", salarioBruto);
    printf("Salario liquido final: %f", salarioFinal);



    return 0;
}