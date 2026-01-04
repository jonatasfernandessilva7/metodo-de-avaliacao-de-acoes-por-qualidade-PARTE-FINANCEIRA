# **VRQ – Valuation por Resiliência e Qualidade**

O **VRQ** é um sistema híbrido de valuation projetado para investidores que buscam empresas capazes de manter receita e lucro constantes mesmo em cenários adversos, priorizando a solvência, eficiência e disciplina financeira.

---

## 1. Núcleo de Projeção: Fluxo de Caixa Livre (FCL)

O ponto de partida é o **FCL**, o dinheiro que sobra após todas as despesas e investimentos operacionais.

* **Projeção Temporal:** O VRQ projeta o FCL por X anos e calcula o **Valor Terminal** (perpetuidade), assumindo que empresas resilientes sobrevivem indefinidamente.
* **WACC Dinâmico:** A taxa de desconto é ajustada automaticamente conforme o risco da empresa e o **fator de qualidade**, aumentando para empresas menos resilientes e diminuindo para empresas de alta qualidade.

---

## 2. CORE: Fatores de Qualidade e Score

O VRQ aplica um **multiplicador de qualidade** que premia ou pune a empresa com base em quatro pilares:

### A. Eficiência de Ativos (ROA) e Capital (ROE)

* **ROA (*Return on Assets*):** Mede a eficiência da empresa em gerar lucro com seus ativos totais.

  * ROA ≥ 10% → bônus de qualidade
  * ROA 7–10% → neutro
  * ROA 4–7% → penalidade leve
  * ROA < 4% → penalidade forte

* **ROE (*Return on Equity*):** Mede o retorno sobre o patrimônio líquido. Ajustado pela alavancagem, o VRQ avalia o retorno real do capital.

  * ROE ajustado ≥ 20% → bônus
  * ROE 15–20% → neutro
  * ROE 10–15% → penalidade leve
  * ROE < 10% → penalidade forte

### B. Resiliência (Volatilidade do Lucro)

* Baixa volatilidade indica capacidade de resistir a crises.

  * Volatilidade ≤ 10% → bônus
  * Volatilidade 10–20% → neutro
  * Volatilidade 20–30% → penalidade leve
  * Volatilidade > 30% → penalidade forte

### C. PEG Ratio (Preço por Crescimento)

* Avalia se o crescimento projetado é barato ou caro.

  * PEG ≤ 1 → bônus
  * PEG 1–2 → neutro
  * PEG > 2 → penalidade

### D. Score de Qualidade e Classificação Final

* O VRQ transforma o **fator de qualidade** em um **score de 0–100**:

  * Score ≥ 80 → 🟢 **COMPRAR**
  * Score 65–79 → 🟡 **OBSERVAR**
  * Score < 65 → 🔴 **EVITAR**

* O score influencia diretamente o **WACC ajustado**: empresas de alta qualidade recebem menor WACC, enquanto empresas de baixa qualidade têm WACC aumentado.

---

## 3. Empresas Comuns vs. Instituições Financeiras

O sistema detecta automaticamente o setor:

* **Empresas Comuns (Dívida Líquida > 0):**

  * Relação **Dívida Líquida / EBITDA** > 3 → aumenta o WACC
  * Valor da dívida é subtraído do Enterprise Value para calcular Equity Value

* **Instituições Financeiras (Dívida Líquida ≤ 0):**

  * Foco em **Margem Líquida** (≥15% para ser resiliente)
  * Equity Value é derivado diretamente do fluxo, ignorando dívida líquida

---

## 4. Estrutura Matemática do Preço Teto

O cálculo segue a hierarquia:

1. **Enterprise Value (EV):** Valor presente dos fluxos projetados + Valor Terminal
2. **Ajuste Qualitativo:**
    
    $EV_{ajustado} ​= EV × Fator \ de \ Qualidade$

3. **Dedução de Passivos:**
   
   $Equity \ Value=EV_{ajustado}​−Dívida \ Líquida$

   (ignorado em bancos/instituições financeiras)
   
4. **Margem de Segurança:** <br><br>
   $$\text{Preço Teto} = \left( \frac{\text{Equity Value}}{\text{Total de Ações}} \right) \times (1 - \text{Margem de Segurança})$$
   
6. **Score e Classificação:**

* Score 0–100, influencia WACC e decisão final

---

## 5. Ajuste de WACC pelo Score

| Score de Qualidade | Ajuste no WACC |
| ------------------ | -------------- |
| ≥ 105% (excelente) | -1%            |
| 95–105% (neutro)   | 0%             |
| 85–95% (moderado)  | +1%            |
| < 85% (baixo)      | +2%            |

---

## 6. Resumo de Regras

| Índice             | Limite         | Ação do Sistema            |
| ------------------ | -------------- | -------------------------- |
| **Dívida/EBITDA**  | > 3.0x         | Aumenta WACC (Risco)       |
| **Margem Líquida** | < 15% (Bancos) | Aumenta WACC (Risco)       |
| **ROE**            | < 15%          | Reduz Fator de Qualidade   |
| **ROA**            | < 7%           | Reduz Fator de Qualidade   |
| **Volatilidade**   | > 20%          | Reduz Fator de Qualidade   |
| **PEG Ratio**      | > 2.0          | Reduz Fator de Qualidade   |
| **PEG Ratio**      | < 1.0          | Aumenta Fator de Qualidade |

---

## 7. Observações

* O VRQ é **híbrido**: combina **valuation clássico (DCF)** com **fatores qualitativos** e ajustes automáticos de risco
* Pode ser aplicado a **empresas comuns e financeiras**

* Permite decisões objetivas: **Comprar, Observar ou Evitar** → ***(Não leve como uma recomendação de investimento, a decisão final é de sua responsabilidade)***
