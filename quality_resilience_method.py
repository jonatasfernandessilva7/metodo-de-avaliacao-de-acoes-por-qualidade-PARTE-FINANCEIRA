import streamlit as st

def format_brl(valor):
    try:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return "R$ 0,00"

def valuation_final(
    fcl, crescimento, anos, wacc, divida_liquida, ebitda,
    patrimonio_liquido, lucro_liquido, ativos_totais, receita_liquida,
    peg_ratio, volatilidade_lucro, total_acoes, margem_seguranca,
    is_banco
):
    
    # --- BANCO vs EMPRESA COMUM ---
    if (not is_banco) and (ebitda > 0):
        dl_ebitda = divida_liquida / ebitda if ebitda != 0 else 0
        alerta_solvencia = dl_ebitda > 3.0
    else:
        dl_ebitda = 0
        margem_liquida = (
            lucro_liquido / receita_liquida if receita_liquida > 0 else 0
        )
        alerta_solvencia = margem_liquida < 0.15

    # --- AJUSTE WACC POR SOLVÊNCIA ---
    if alerta_solvencia:
        wacc += 0.02

    # --- ROE e ROA ---
    roe = lucro_liquido / patrimonio_liquido if patrimonio_liquido > 0 else 0
    roa = lucro_liquido / ativos_totais if ativos_totais > 0 else 0

    # --- ALAVANCAGEM ---
    alavancagem = (
        ativos_totais / patrimonio_liquido
        if patrimonio_liquido > 0 else 0
    )
    roe_ajustado = roe / alavancagem if alavancagem > 0 else roe

    fator_qualidade = 1.0

    # --- ROE AJUSTADO ---
    if roe_ajustado >= 0.20:
        fator_qualidade += 0.05
    elif roe_ajustado >= 0.15:
        fator_qualidade += 0.00
    elif roe_ajustado >= 0.10:
        fator_qualidade -= 0.05
    else:
        fator_qualidade -= 0.10

    # --- ROA ---
    if roa >= 0.10:
        fator_qualidade += 0.05
    elif roa >= 0.07:
        fator_qualidade += 0.00
    elif roa >= 0.04:
        fator_qualidade -= 0.05
    else:
        fator_qualidade -= 0.10

    # --- VOLATILIDADE DO LUCRO ---
    if volatilidade_lucro <= 0.10:
        fator_qualidade += 0.05
    elif volatilidade_lucro <= 0.20:
        fator_qualidade += 0.00
    elif volatilidade_lucro <= 0.30:
        fator_qualidade -= 0.05
    else:
        fator_qualidade -= 0.10

    # --- PEG RATIO (CORRIGIDO) ---
    if peg_ratio <= 1.0:
        fator_qualidade += 0.05
    elif peg_ratio <= 2.0:
        fator_qualidade += 0.00
    elif peg_ratio <=0 or peg_ratio > 3.0:
        fator_qualidade -= 0.10
    else:
        fator_qualidade -= 0.15

    # --- AJUSTE WACC PELO FATOR DE QUALIDADE ---
    if fator_qualidade >= 1.05:
        wacc -= 0.01
    elif fator_qualidade >= 0.95:
        wacc += 0.00
    elif fator_qualidade >= 0.85:
        wacc += 0.01
    else:
        wacc += 0.02

    # --- DCF ---
    valor_presente = 0
    for t in range(1, anos + 1):
        fcl_projetado = fcl * ((1 + crescimento) ** t)
        valor_presente += fcl_projetado / ((1 + wacc) ** t)

    # crescimento perpétuo padrão
    g = 0.03

    fcl_terminal = (fcl * (1 + crescimento) ** anos * (1 + g)) / (wacc - g)
    valor_terminal_presente = fcl_terminal / ((1 + wacc) ** anos)

    # --- EQUITY VALUE ---
    if is_banco:
        equity_value = (valor_presente + valor_terminal_presente) * fator_qualidade
    else:
        enterprise_value = (valor_presente + valor_terminal_presente) * fator_qualidade
        equity_value = enterprise_value - divida_liquida

    # --- PREÇO POR AÇÃO ---
    if total_acoes is None or total_acoes <= 0:
        v_justo_acao = 0
        p_teto = 0
    else:
        v_justo_acao = equity_value / total_acoes
        p_teto = v_justo_acao * (1 - margem_seguranca)

    # --- SCORE ---
    score_qualidade = int(max(0, min(100, (fator_qualidade - 0.8) * 250)))

    if score_qualidade >= 80:
        classificacao = "🟢 COMPRAR"
    elif score_qualidade >= 65:
        classificacao = "🟡 OBSERVAR"
    else:
        classificacao = "🔴 EVITAR"

    return (
        v_justo_acao,
        p_teto,
        roe,
        dl_ebitda,
        fator_qualidade,
        score_qualidade,
        classificacao,
        wacc,
    )


# ==============================
# STREAMLIT APP
# ==============================

st.set_page_config(page_title="Valuation Resiliente - VR", layout="wide")
st.title("📈 Calculadora de Valuation por Resiliência e Qualidade (VRQ)")

with st.sidebar:
    st.header("Configurações Globais")
    anos = st.slider("Anos de projeção", 5, 20, 10)
    wacc = st.number_input("WACC Base", 0.0, 1.0, 0.10)
    margem_seg = st.slider("Margem de Segurança (%)", 0, 50, 10) / 100
    is_banco = st.checkbox("🏦 Empresa do Setor Financeiro?")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Dados Operacionais")
    fcl = st.number_input("Fluxo de Caixa Livre (R$)", value=0.0)
    receita = st.number_input("Receita Líquida (R$)", value=0.0)
    ebitda = st.number_input("EBITDA (R$)", value=0.0)
    crescimento = st.number_input("Crescimento (%)", 0.0, 1.0, 0.10)

with col2:
    st.subheader("⚖️ Dados de Balanço e DRE")
    divida_liquida = st.number_input("Dívida Líquida (R$)", value=0.0)
    patrimonio = st.number_input("Patrimônio Líquido (R$)", value=0.0)
    lucro_l = st.number_input("Lucro Líquido (R$)", value=0.0)
    ativos = st.number_input("Ativos Totais (R$)", value=0.0)
    peg = st.number_input("PEG Ratio", value=0.0)
    volatilidade = st.number_input("Volatilidade do Lucro (%)", value=0.10)
    total_acoes = st.number_input("Total de Ações", min_value=1, value=1, step=1)

if st.button("CALCULAR PREÇO TETO"):

    (
        v_justo,
        p_teto,
        roe_calc,
        dl_ebitda_calc,
        fator_q,
        score_q,
        classe_final,
        wacc_final,
    ) = valuation_final(
        fcl, crescimento, anos, wacc, divida_liquida, ebitda,
        patrimonio, lucro_l, ativos, receita, peg, volatilidade,
        total_acoes, margem_seg, is_banco
    )

    st.divider()
    r1, r2, r3, r4 = st.columns(4)

    r1.metric("Valor Justo", format_brl(v_justo))
    r2.metric("Preço Teto", format_brl(p_teto))
    r3.metric("ROE", f"{roe_calc*100:.2f}%")
    r4.metric("Score Qualidade", f"{score_q}/100")

    st.subheader("📌 Classificação Final")
    st.markdown(f"### {classe_final}")

    st.caption(f"Fator de Qualidade: {fator_q:.2f} | WACC Ajustado: {wacc_final*100:.2f}%")

    if is_banco:
        st.info("🏦 Modo Instituição Financeira Ativado: Dívida Líquida ignorada no cálculo.")
