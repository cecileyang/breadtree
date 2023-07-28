import streamlit as st
from PIL import Image

if 'num' not in st.session_state:
    st.session_state.num = 0

choices1 = ['2 years', '3 - 5 years', '6 - 10 years', '11 - 15 years', 'More than 15 years']
choices2 = ['1 - 2 years', '3 - 4 years', '5 - 6 years', '7 - 8 years', 'More than 8 years']
choices3 = ['Very inexperienced', 'Somewhat inexperienced', 'Someewhat experienced', 'Experienced', 'Very Experienced']
choices4 = ['1 year or less', '1 - 2 years', '3 - 5 years', '6 - 10 years', '11 - 15 years', 'More than 15 years']
choices5 = ['Very unstable', 'Unstable', 'Somewhat stable', 'Stable', 'Very Stable']
choices6 = ['Sell all the remaining investment', 'Sell a portion of the remaining investment', 'Hold onto the investment and sell nothing',
            'Buy more of the remaining investment']
choices7 = ['A - minimal volatility', 'B - moderate volatility', 'C - most volatility']
choices8 = ['Strongly disagree', 'Disagree', 'Somewhat agree', 'Agree', 'Strongly agree']
choices9 = ['Strongly disagree', 'Disagree', 'Somewhat agree', 'Agree', 'Strongly agree']
choices10 = ['Sell all the remaining investment', 'Sell a portion of the remaining investment', 'Hold onto the investment and sell nothing',
            'Buy more of the remaining investment']
choices11 = ['Strongly disagree', 'Disagree', 'Somewhat agree', 'Agree', 'Strongly agree']
choices12 = []

questions = [
    ('As I withdraw money from these investments, I plan to spend it over a period of...', choices1),
    ('When making long-term investment, I plan to keep the money invested for...', choices2),
    ('When it comes to investing in stock or bond mutual funds or ETFs - or individual stocks or bonds - \
     I would describe myself as...', choices3),
    ('I plan to begin taking money from my investments in...', choices4),
    ('My current and future income sources (for example, salary, social security, pensions) are...', choices5),
    ('From September 2008 through October 2008, bonds lost 4%. If I owned a bond investment that lost 4% in two months, I would...\
     \n(If you owned bonds during this period, please select thee answer that matches your actions at that time.)', choices6),
    ('The chart shows the greatest 1-year loss and the highest 1-year gain on 3 different hypothetical investments of $10,000.\
     Given the potential gain or loss in any 1 year, I would invest my money in...', choices7),
     ('During market declines, I tend to sell portions of my riskier assets and invest the money in safer assets.', choices8),
    ('I would invest in a mutual fund or ETF (exchanged-trade fund) based solely on a brief conversation with a friend, co-worker, \
     or relative.', choices9),
    ('From September 2008 through November 2008, stocks lost over 31%. If I owned a stock investment that lost about 31% in three \
     months, I would... \nIf you owned bonds during this period, please select thee answer that matches your actions at that time.)',
     choices10),
    ('Generally, I prefer an investment with little or no ups and downs in value, and I am willing to accept the lower returns these \
     investments may make.', choices11),
    ('My current asset allocation. \n Enter the current asset allocation in whole numbers. Your percentage must total 100%. If you don\'t \
    enter any percentage, the questionnaire will assume that 100% of your assets are in short-term reserves.', choices12)
    ]

def render_questionnaire():
  with st.form('Risk Questionnaire'):
    for question, choices in questions:
        num = st.session_state.num
        print(num)
        # https://github.com/streamlit/streamlit/issues/7049 no radio pre-selection
        if num < 11:
            st.radio(question, key=num+1, options=choices)
        else:
            st.write(question)
            number_percent_field('Short-term reserves')
            number_percent_field('Bonds')
            number_percent_field('Stocks')
        if num == 6:
           image = Image.open('chart.png')
           st.image(image)   
        st.session_state.num += 1
        if st.session_state.num >= 12:
           st.session_state.num = 0
    st.form_submit_button('Submit')
    st.stop()

def number_percent_field(label, columns=None, **input_params):
    c1, c2 = st.columns(columns or [2, 4])

    # Display field name with some alignment
    c1.markdown("##")
    c1.markdown(label)

    # Sets a default key parameter to avoid duplicate key errors
    input_params.setdefault("key", label)

    # Forward number input parameters
    return c2.number_input("", **input_params, min_value=0, max_value=100)


render_questionnaire()