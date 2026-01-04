# **VRQ – Valuation por Resiliência e Qualidade**

O **VRQ** é um sistema híbrido de valuation projetado para investidores que buscam empresas capazes de manter **lucros consistentes, baixa alavancagem e resiliência em crises**.
O método combina **DCF (Fluxo de Caixa Descontado)** com **indicadores de qualidade e risco.**

> ⚠️ Este modelo não constitui recomendação de investimento. Use apenas como apoio educacional.

---

## 📌 1. Núcleo de Projeção: Fluxo de Caixa Livre (FCL)

O VRQ utiliza o **Fluxo de Caixa Livre (FCL)** como base.

* projeção do FCL por *X* anos
* cálculo do **Valor Terminal** via perpetuidade
* desconto pelo **WACC ajustado dinamicamente**

Empresas resilientes tendem a sobreviver indefinidamente; por isso o modelo adota o conceito de perpetuidade.

---

## 🧠 2. CORE: Fatores de Qualidade e Score

O VRQ aplica um **multiplicador de qualidade**, que ajusta o valuation para cima ou para baixo conforme quatro pilares:

### ✅ A. Eficiência de Ativos (ROA) e Capital (ROE)

**ROA – Return on Assets**

| ROA   | Ação             |
| ----- | ---------------- |
| ≥ 10% | bônus            |
| 7–10% | neutro           |
| 4–7%  | penalidade leve  |
| < 4%  | penalidade forte |

**ROE ajustado pela alavancagem**

| ROE ajustado | Ação             |
| ------------ | ---------------- |
| ≥ 20%        | bônus            |
| 15–20%       | neutro           |
| 10–15%       | penalidade leve  |
| < 10%        | penalidade forte |

> O ajuste por alavancagem evita premiar empresas com retorno artificialmente elevado devido a endividamento.

---

### 🛡️ B. Resiliência (Volatilidade do Lucro)

| Volatilidade do lucro | Ação             |
| --------------------- | ---------------- |
| ≤ 10%                 | bônus            |
| 10–20%                | neutro           |
| 20–30%                | penalidade leve  |
| > 30%                 | penalidade forte |

Baixa volatilidade indica:

* previsibilidade
* estabilidade de margens
* menor risco de crise

---

### 📈 C. PEG Ratio (Preço / Crescimento)

| PEG | Ação       |
| --- | ---------- |
| ≤ 1 | bônus      |
| 1–2 | neutro     |
| > 2 | penalidade |

O PEG evita pagar caro demais por crescimento.

---

### 🏁 D. Score e Classificação Final

O **fator de qualidade** é convertido em **score de 0 a 100**.

| Score | Classificação |
| ----- | ------------- |
| ≥ 80  | 🟢 COMPRAR    |
| 65–79 | 🟡 OBSERVAR   |
| < 65  | 🔴 EVITAR     |

O score também:

* ajusta o **WACC**
* reforça prêmio para empresas de qualidade
* penaliza negócios frágeis

---

## 🏦 3. Empresas Comuns vs. Instituições Financeiras

O sistema trata setores de forma distinta.

### 🏭 Empresas não financeiras

* **Dívida Líquida / EBITDA > 3x → risco**
* dívida impacta o **Equity Value**
* solvência afeta o WACC

### 🏦 Bancos e financeiras

* dívida líquida é ignorada

* foco recai sobre:

  * margem líquida
  * ROE
  * volatilidade do lucro

* margem líquida < 15% aumenta o risco

---

## 🧮 4. Estrutura Matemática do Preço-Teto

1. **Valor Presente dos Fluxos + Valor Terminal** <br><br>


$EV = \sum \frac{FCL_t}{(1+WACC)^t} + \frac{FCL_{terminal}}{(WACC-g)}
$

2. **Ajuste por Qualidade** <br><br>

$EV_{ajustado} ​= EV × Fator \ de \ Qualidade$

3. **Dedução de Passivos (exceto bancos)** <br><br>

$Equity \ Value=EV_{ajustado}​−Dívida \ Líquida$

4. **Preço Justo por Ação** <br><br>

$Prec\c​o \ Justo=\frac{Total \ de \ Ac\c​ões} {Equity \ Value}$	​

5. **Preço-Teto com Margem de Segurança** <br><br>

$$\text{Preço Teto} = \left( \frac{\text{Equity Value}}{\text{Total de Ações}} \right) \times (1 - \text{Margem de Segurança})$$

---

## ⚖️ 5. Ajuste do WACC pelo Score

| Score   | Ajuste no WACC |
| ------- | -------------- |
| ≥ 105%  | −1%            |
| 95–105% | 0%             |
| 85–95%  | +1%            |
| < 85%   | +2%            |

Empresas melhores → menor taxa de desconto
Empresas piores → maior taxa de desconto

---

## 📋 6. Resumo de Regras Automáticas

| Indicador               | Condição | Efeito                   |
| ----------------------- | -------- | ------------------------ |
| Dívida/EBITDA           | > 3x     | aumenta WACC             |
| Margem líquida (bancos) | < 15%    | aumenta WACC             |
| ROE                     | < 15%    | reduz fator de qualidade |
| ROA                     | < 7%     | reduz fator de qualidade |
| Volatilidade do lucro   | > 20%    | reduz fator de qualidade |
| PEG                     | > 2      | penalidade               |
| PEG                     | < 1      | bônus                    |

---