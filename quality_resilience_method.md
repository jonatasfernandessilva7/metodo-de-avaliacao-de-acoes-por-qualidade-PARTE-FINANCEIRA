## Documentação: Sistema de Valuation de Qualidade (Híbrido)

O sistema foi projetado para investidores que buscam empresas capazes de manter receita e lucro constantes mesmo em cenários adversos, priorizando a solvência e a eficiência real.

### 1. Núcleo de Projeção: Fluxo de Caixa Livre (FCL)

O ponto de partida é o **FCL**, o dinheiro que sobra após todas as despesas e investimentos operacionais.

* **Lógica Temporal:** O programa projeta esse fluxo por X anos e calcula o **Valor Terminal** (perpetuidade), assumindo que empresas resilientes sobrevivem indefinidamente.
* **WACC:** A taxa de desconto não é estática. Se a empresa for uma "má pagadora de dívidas", o sistema aumenta o custo de capital automaticamente, reduzindo o valor presente.

---

### 2. CORE: Fatores de Qualidade

Diferente de cálculos tradicionais, o sistema aplica um **multiplicador de qualidade** que premia ou pune a empresa com base em quatro pilares:

#### A. Eficiência de Ativos (ROA) e Capital (ROE)

* **ROA (*Return on Assets*):** Avalia se a empresa gera lucro com sua estrutura total (ativos). Se o ROA for menor que **7%**, o sistema aplica uma punição, identificando que a empresa precisa de "muita máquina" para pouco resultado.
* **ROE (*Return on Equity*):** Foca no retorno para o sócio. Abaixo de **15%**, a empresa é considerada ineficiente.

#### B. Resiliência (Volatilidade do Lucro)

* Representa a capacidade de se manter constante em crises. Se a volatilidade histórica for superior a **20%**, o programa entende que o futuro é imprevisível e reduz o **Fator de Qualidade**.

#### C. PEG Ratio (Preço por Crescimento)

* Baseado na filosofia de Peter Lynch, ele valida se o crescimento projetado é "barato". Um **PEG < 1.0** bonifica o valuation; um **PEG > 2.0** aplica um desconto por euforia excessiva do mercado.

---

### 3. Empresas Comuns vs. Instituições Financeiras

O sistema detecta automaticamente o setor através do campo de **Dívida Líquida**:

* **Empresas Comuns (Dívida > 0):** O foco é na relação **Dívida Líquida/EBITDA**. Se for maior que **3.0x**, o risco aumenta. O valor da dívida é subtraído do valor total da empresa para achar o valor do acionista.
* **Financeiras (Dívida <= 0):** O sistema ignora a dívida líquida e foca na **Margem Líquida**. Se a margem for inferior a **15%**, o risco é aumentado. O valor gerado pelo fluxo já é considerado o valor direto do acionista (*Equity Value*).

---

### 4. Estrutura Matemática do Preço Teto

O sistema segue esta hierarquia de cálculo:

1. **Cálculo do Enterprise Value (EV):** Valor presente dos fluxos de X anos + Valor Terminal.
2. **Ajuste Qualitativo:**  $EV_{ajustado} = EV \times Fator\_Qualidade$ (Onde o fator varia conforme ROE, ROA, PEG e Volatilidade).
3. **Dedução de Passivos:** $Equity\ Value = EV_{ajustado} - Divida\ Liquida$ (Ignorado no modo Instituição Financeira).
4. **Margem de Segurança:** O valor por ação sofre o desconto final definido por você (ex: 10% ou 20%).

- Fórmula Preço Teto: $$\text{Preço Teto} = \left( \frac{\text{Equity Value}}{\text{Total de Ações}} \right) \times (1 - \text{Margem de Segurança})$$
---

### 5. Resumo

| Índice | Limite | Ação do Sistema |
| --- | --- | --- |
| **Dívida/EBITDA** | > 3.0x | Aumenta o WACC (Risco) |
| **Margem Líquida** | < 15% (Bancos) | Aumenta o WACC (Risco) |
| **ROE** | < 15% | Reduz Fator de Qualidade |
| **ROA** | < 7% | Reduz Fator de Qualidade |
| **Volatilidade** | > 20% | Reduz Fator de Qualidade |