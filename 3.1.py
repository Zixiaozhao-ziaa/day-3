import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

st.title("EXERCISE 3")

## STEP 1: 创建文本框，接收用户输入的 hypothetical scenario
scenario = st.text_area(
    "Hypothetical Scenario Involving Contract Formation",
    height=200,
    placeholder="e.g., describe the parties involved, what was offered, and how it was accepted..."
)

## STEP 2 & 3: 按钮触发 AI 分析，并将结果存入 session_state 以便持久显示
## 用户写完、点击按钮后才提交给 AI，减少不必要的调用
if st.button("Analyse Scenario"):
    prompt = f"""
    You are a contract law assistant. Base your analysis STRICTLY on the six 
    elements of contract formation defined below (sourced from the Victorian 
    Law Handbook). Do not rely on general legal knowledge beyond what is 
    described here — only apply these specific tests.

    1. Offer and Acceptance:
    A contract requires a definite offer by one party that is accepted, 
    exactly as proposed, by the other party. A mere willingness to negotiate 
    is not an offer. Acceptance must be a clear and unequivocal response 
    communicated to the offeror, and can be shown through words or conduct.

    2. Intention to Create Legal Relations:
    The parties must have intended their agreement to be legally binding. 
    This is assessed objectively (what a reasonable person would think), not 
    by what the parties privately believed. Commercial/arm's-length dealings 
    are presumed to carry this intention; social or domestic arrangements 
    (e.g. between family or friends) are presumed NOT to, unless stated otherwise.

    3. Consideration:
    Each party must give something of value in exchange for the other's 
    promise (not necessarily money). Courts do not assess whether the value 
    given was "fair," only whether some value existed. Love, affection, or a 
    pure gift do not count as valid consideration.

    4. Legal Capacity:
    Both parties must have the legal capacity to contract. Certain groups 
    (minors/young people under 18, people with mental impairment, bankrupts, 
    corporations acting through authorised representatives, and prisoners) may 
    have limited or conditional capacity to contract.

    5. Consent:
    Each party's agreement must be genuine and freely given. Consent can be 
    undermined by mistake, misrepresentation, duress, undue influence, or 
    (in standard form contracts) unfair terms.

    6. Legality:
    The contract (or its terms) must not involve illegal conduct or be 
    contrary to public policy. Contracts that are illegal are generally void 
    and unenforceable.

    For each of the six elements above, state clearly whether it appears to be 
    satisfied, not satisfied, or unclear based on the scenario, and explain 
    your reasoning by referring only to the facts given and the definitions 
    above. Then give an overall conclusion on whether a contract has been formed.

    Scenario: {scenario}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    ## 只存纯文字内容，不存整个 API 返回对象
    st.session_state.initial_response = response.choices[0].message.content

## 只要分析过一次，结果就会一直显示，不受页面重跑影响
if "initial_response" in st.session_state:
    st.write(st.session_state.initial_response)

## STEP 4: 追问功能（依赖 initial_response 已存在）
if "initial_response" in st.session_state:
    followup = st.text_input("Ask a follow-up question about this analysis")

    if st.button("Ask Follow-up"):
        followup_prompt = f"""
        Here is your previous analysis of a contract formation scenario:

        {st.session_state.initial_response}

        The user has a follow-up question about this analysis:
        {followup}

        Answer the follow-up question, staying consistent with your previous analysis 
        and the six elements of contract formation used above.
        """

        followup_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": followup_prompt}]
        )
        st.session_state.followup_response = followup_response.choices[0].message.content

    if "followup_response" in st.session_state:
        st.write(st.session_state.followup_response)

## STEP 5: 导出 .docx（待添加）