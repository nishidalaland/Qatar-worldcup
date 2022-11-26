import streamlit as st
import pandas as pd
import time

st.title('2022 Qatar World Cup (11/20~12/18)')

#Participating countries
NLD = 'Netherlands🇳🇱(8)'
SEN = 'Senegal🇸🇳(18)'
ECU = 'Ecuador🇪🇨(44)'
QAT = 'Qatar🇶🇦(50)'
ENG = 'England🏴󠁧󠁢󠁥󠁮󠁧󠁿(5)'
WAL = 'Wales🏴󠁧󠁢󠁷󠁬󠁳󠁿(19)'
USA = 'United States🇺🇸(16)'
IRN = 'Iran🇮🇷(20)'
MEX = 'Mexico🇲🇽(13)'
POL = 'Poland🇵🇱(26)'
ARG = 'Argentina🇦🇷(3)'
SAU = 'Saudi Arabia🇸🇦(51)'
FRA = 'France🇫🇷(4)'
AUS = 'Australia🇦🇺(38)'
DNK = 'Denmark🇩🇰(10)'
TUN = 'Tunisia🇹🇳(30)'
ESP = 'Spain🇪🇸(7)'
CRI = 'Costa Rica🇨🇷(31)'
DEU = 'Germany🇩🇪(11)'
JPN = 'Japan🇯🇵(24)'
CAN = 'Canada🇨🇦(41)'
BEL = 'Belgium🇧🇪(2)'
HRV = 'Croatia🇭🇷(12)'
MAR = 'Morocco🇲🇦(22)'
BRA = 'Brazil🇧🇷(1)'
SRB = 'Serbia🇷🇸(21)'
CHE = 'Switzerland🇨🇭(15)'
CMR = 'Cameroon🇨🇲(43)'
PRT = 'Portugal🇵🇹(9)'
GHA = 'Ghana🇬🇭(61)'
URY = 'Uruguay🇺🇾(14)'
KOR = 'Korea🇰🇷(28)'


#FIFA Ranking
if st.sidebar.checkbox('FIFA Ranking'):
    st.header('FIFA Ranking')
    with st.spinner('Wait for it...'):
        time.sleep(1.0)
    st.write('World Cup participating countries are colored.')

    df = pd.DataFrame(
        {
            'Team':['Brazil','Belgium','Argentina','France','England','Itary','Spain','Netherlands','Portugal','Denmark','Germany','Croatia','Mexico','Uruguay','Switzerland','United States','Colombia','Senegal','Wales',
                    'Iran','Serbia','Morocco','Peru','Japan','Sweden','Poland','Ukraine','Korea','Chile','Tunisia','Costa Rica','Nigeria','Russia','Austria','Czech Republic','Hungary','Algeria',
                    'Australia','Egypt','Scotland','Canada','Norway','Cameroon','Ecuador','Turkey','Mali','Paraguay',"Côte d'Ivoire",'Republic of Ireland','Qatar','Saudi Arabia']
        }
    )

    
    def color_background_yellow(val):
        if val == 'Itary':
            color = 'white' 
        elif val == 'Colombia':
            color = 'white'
        elif val == 'Sweden':
            color = 'white'
        elif val == 'Ukraine':
            color = 'white'
        elif val == 'Chile':
            color = 'white'
        elif val == 'Nigeria':
            color = 'white'
        elif val == 'Russia':
            color = 'white'
        elif val == 'Austria':
            color = 'white'
        elif val == 'Czech Republic':
            color = 'white'
        elif val == 'Hungary':
            color = 'white'
        elif val == 'Algeria':
            color = 'white'
        elif val == 'Egypt':
            color = 'white'
        elif val == 'Scotland':
            color = 'white'
        elif val == 'Norway':
            color = 'white'
        elif val == 'Turkey':
            color = 'white'
        elif val == 'Mali':
            color = 'white'
        elif val == 'Paraguay':
            color = 'white'
        elif val == "Côte d'Ivoire":
            color = 'white'
        elif val == 'Republic of Ireland':
            color = 'white'
        else:
            color = 'yellow'

        return 'background-color: %s' % color
    
    def color_background_pink(index):
        color = 'white' if index == 11 else 'pink'
        return 'background-color: %s' % color

    df.index = df.index + 1
    st.table(df.style.applymap(color_background_yellow))


    Europe = [NLD,ENG,WAL,POL,FRA,DNK,ESP,DEU,BEL,HRV,SRB,CHE,PRT]
    Africa = [SEN,TUN,MAR,CMR,GHA]
    Asia = [QAT,IRN,SAU,AUS,JPN,KOR]
    North_America = [USA,MEX,CAN]
    South_America = [ECU,ARG,CRI,BRA,URY]
   
    num_data = [len(Europe), len(Africa), len(Asia), len(North_America), len(South_America)]
    group_labels = ['Europe','Africa','Asia','North America','South America']


    st.write('Worldcup paticipating countries by regions')
    df = pd.DataFrame(
        {
            '#':[1,3,2,5,4],
            'Regions':group_labels,
            'Number':num_data,
        }
    )
    df = df.sort_values(by='Number', ascending=False)
    df = df.set_index('#')
    st.table(df.style)



#define
def Group_A(): 
    st.header('Group A')

    #define
    match_NLD = 0
    match_SEN = 0
    match_ECU = 0
    match_QAT = 0
    pts_NLD = 0
    pts_SEN = 0
    pts_ECU = 0
    pts_QAT = 0
    wins_NLD = 0
    wins_SEN = 0
    wins_ECU = 0
    wins_QAT = 0
    draws_NLD = 0
    draws_SEN = 0
    draws_ECU = 0
    draws_QAT = 0
    loses_NLD = 0
    loses_SEN = 0
    loses_ECU = 0
    loses_QAT = 0
    gd_NLD = 0
    gd_SEN = 0
    gd_ECU = 0
    gd_QAT = 0

    if st.checkbox('🇪🇨vs🇶🇦'):
            match_ECU += 1
            match_QAT += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ECU, key=0, step=1)
            score_2=right_column.number_input(QAT, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇪🇨vs🇶🇦', value=result)

            gd_ECU += score_1-score_2
            gd_QAT += score_2-score_1

            if score_1 > score_2:
                pts_ECU += 3
                pts_QAT += 0
                wins_ECU += 1
                loses_QAT += 1
            elif score_1 < score_2:
                pts_ECU += 0
                pts_QAT += 3
                wins_QAT += 1
                loses_ECU += 1
            else:
                pts_ECU += 1
                pts_QAT += 1
                draws_ECU += 1
                draws_QAT += 1

    if st.checkbox('🇳🇱vs🇸🇳'):
            match_NLD += 1
            match_SEN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(NLD, key=0, step=1)
            score_2=right_column.number_input(SEN, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇳🇱vs🇸🇳', value=result)

            gd_NLD += score_1-score_2
            gd_SEN += score_2-score_1

            if score_1 > score_2:
                pts_NLD += 3
                pts_SEN += 0
                wins_NLD += 1
                loses_SEN += 1
            elif score_1 < score_2:
                pts_NLD += 0
                pts_SEN += 3
                wins_SEN += 1
                loses_NLD += 1
            else:
                pts_NLD += 1
                pts_SEN += 1
                draws_NLD += 1
                draws_SEN += 1

    if st.checkbox('🇸🇳vs🇶🇦'):
            match_SEN += 1
            match_QAT += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(SEN, key=2, step=1)
            score_2=right_column.number_input(QAT, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇸🇳vs🇶🇦', value=result)

            gd_SEN += score_1-score_2
            gd_QAT += score_2-score_1

            if score_1 > score_2:
                pts_SEN += 3
                pts_QAT += 0
                wins_SEN += 1
                loses_QAT += 1
            elif score_1 < score_2:
                pts_SEN += 0
                pts_QAT += 3
                wins_QAT += 1
                loses_SEN += 1
            else:
                pts_SEN += 1
                pts_QAT += 1
                draws_SEN += 1
                draws_QAT += 1

    if st.checkbox('🇳🇱vs🇪🇨'):
            match_NLD += 1
            match_ECU += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(NLD, key=2, step=1)
            score_2=right_column.number_input(ECU, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇳🇱vs🇪🇨', value=result)

            gd_NLD += score_1-score_2
            gd_ECU += score_2-score_1

            if score_1 > score_2:
                pts_NLD += 3
                pts_ECU += 0
                wins_NLD += 1
                loses_ECU += 1
            elif score_1 < score_2:
                pts_NLD += 0
                pts_ECU += 3
                wins_ECU += 1
                loses_NLD += 1
            else:
                pts_NLD += 1
                pts_ECU += 1
                draws_NLD += 1
                draws_ECU += 1

    if st.checkbox('🇳🇱vs🇶🇦'):
            match_NLD += 1
            match_QAT += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(NLD, key=1, step=1)
            score_2=right_column.number_input(QAT, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇳🇱vs🇶🇦', value=result)

            gd_NLD += score_1-score_2
            gd_QAT += score_2-score_1

            if score_1 > score_2:
                pts_NLD += 3
                pts_QAT += 0
                wins_NLD += 1
                loses_QAT += 1
            elif score_1 < score_2:
                pts_NLD += 0
                pts_QAT += 3
                wins_QAT += 1
                loses_NLD += 1
            else:
                pts_NLD += 1
                pts_QAT += 1
                draws_NLD += 1
                draws_QAT += 1

    if st.checkbox('🇪🇨vs🇸🇳'):
            match_ECU += 1
            match_SEN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ECU, key=1, step=1)
            score_2=right_column.number_input(SEN, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇪🇨vs🇸🇳', value=result)

            gd_ECU += score_1-score_2
            gd_SEN += score_2-score_1

            if score_1 > score_2:
                pts_ECU += 3
                pts_SEN += 0
                wins_ECU += 1
                loses_SEN += 1
            elif score_1 < score_2:
                pts_ECU += 0
                pts_SEN += 3
                wins_SEN += 1
                loses_ECU += 1
            else:
                pts_ECU += 1
                pts_SEN += 1
                draws_ECU += 1
                draws_SEN += 1

    df_A = pd.DataFrame(
            {
                'teams':[NLD,ECU,SEN,QAT],
                'matchs':[match_NLD,match_ECU,match_SEN,match_QAT],
                'pts':[pts_NLD,pts_ECU,pts_SEN,pts_QAT],
                'W':[wins_NLD,wins_ECU,wins_SEN,wins_QAT],
                'D':[draws_NLD,draws_ECU,draws_SEN,draws_QAT],
                'L':[loses_NLD,loses_ECU,loses_SEN,loses_QAT],
                'gd':[gd_NLD,gd_ECU,gd_SEN,gd_QAT]
            }
            )

    df_A = df_A.set_index(['teams'])
    df_A = df_A.sort_values(by=['pts','gd'], ascending=False)

    st.table(df_A.style)

def Group_B():    
        st.header('Group B')
    #define
        match_ENG = 0
        match_WAL = 0
        match_USA = 0
        match_IRN = 0
        pts_ENG = 0
        pts_WAL = 0
        pts_USA = 0
        pts_IRN = 0
        wins_ENG = 0
        wins_WAL = 0
        wins_USA = 0
        wins_IRN = 0
        draws_ENG = 0
        draws_WAL = 0
        draws_USA = 0
        draws_IRN = 0
        loses_ENG = 0
        loses_WAL = 0
        loses_USA = 0
        loses_IRN = 0
        gd_ENG = 0
        gd_WAL = 0
        gd_USA = 0
        gd_IRN = 0

        if st.checkbox('🏴󠁧󠁢󠁥󠁮󠁧󠁿vs🇮🇷'):
            match_ENG += 1
            match_IRN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ENG, key=1, step=1)
            score_2=right_column.number_input(IRN, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🏴󠁧󠁢󠁥󠁮󠁧󠁿vs🇮🇷', value=result)

            gd_ENG += score_1-score_2
            gd_IRN += score_2-score_1

            if score_1 > score_2:
                pts_ENG += 3
                pts_IRN += 0
                wins_ENG += 1
                loses_IRN += 1
            elif score_1 < score_2:
                pts_ENG += 0
                pts_IRN += 3
                wins_IRN += 1
                loses_ENG += 1
            else:
                pts_ENG += 1
                pts_IRN += 1
                draws_ENG += 1
                draws_IRN += 1

        if st.checkbox('🇺🇸vs🏴󠁧󠁢󠁷󠁬󠁳󠁿'):
            match_USA += 1
            match_WAL += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(USA, key=1, step=1)
            score_2=right_column.number_input(WAL, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇺🇸vs🏴󠁧󠁢󠁷󠁬󠁳󠁿', value=result)

            gd_USA += score_1-score_2
            gd_WAL += score_2-score_1

            if score_1 > score_2:
                pts_USA += 3
                pts_WAL += 0
                wins_USA += 1
                loses_WAL += 1
            elif score_1 < score_2:
                pts_USA += 0
                pts_WAL += 3
                wins_WAL += 1
                loses_USA += 1
            else:
                pts_USA += 1
                pts_WAL += 1
                draws_USA += 1
                draws_WAL += 1

        if st.checkbox('🏴󠁧󠁢󠁷󠁬󠁳󠁿vs🇮🇷'):
            match_WAL += 1
            match_IRN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(WAL, key=2, step=1)
            score_2=right_column.number_input(IRN, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🏴󠁧󠁢󠁷󠁬󠁳󠁿vs🇮🇷', value=result)

            gd_WAL += score_1-score_2
            gd_IRN += score_2-score_1

            if score_1 > score_2:
                pts_WAL += 3
                pts_IRN += 0
                wins_WAL += 1
                loses_IRN += 1
            elif score_1 < score_2:
                pts_WAL += 0
                pts_IRN += 3
                wins_IRN += 1
                loses_WAL += 1
            else:
                pts_WAL += 1
                pts_IRN += 1
                draws_WAL += 1
                draws_IRN += 1

        if st.checkbox('🏴󠁧󠁢󠁥󠁮󠁧󠁿vs🇺🇸'):
            match_ENG += 1
            match_USA += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ENG, key=2, step=1)
            score_2=right_column.number_input(USA, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🏴󠁧󠁢󠁥󠁮󠁧󠁿vs🇺🇸', value=result)

            gd_ENG += score_1-score_2
            gd_USA += score_2-score_1

            if score_1 > score_2:
                pts_ENG += 3
                pts_USA += 0
                wins_ENG += 1
                loses_USA += 1
            elif score_1 < score_2:
                pts_ENG += 0
                pts_USA += 3
                wins_USA += 1
                loses_ENG += 1
            else:
                pts_ENG += 1
                pts_USA += 1
                draws_ENG += 1
                draws_USA += 1

        if st.checkbox('🏴󠁧󠁢󠁥󠁮󠁧󠁿vs🏴󠁧󠁢󠁷󠁬󠁳󠁿'):
            match_ENG += 1
            match_WAL += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ENG, key=0, step=1)
            score_2=right_column.number_input(WAL, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🏴󠁧󠁢󠁥󠁮󠁧󠁿vs🏴󠁧󠁢󠁷󠁬󠁳󠁿', value=result)

            gd_ENG += score_1-score_2
            gd_WAL += score_2-score_1

            if score_1 > score_2:
                pts_ENG += 3
                pts_WAL += 0
                wins_ENG += 1
                loses_WAL += 1
            elif score_1 < score_2:
                pts_ENG += 0
                pts_WAL += 3
                wins_WAL += 1
                loses_ENG += 1
            else:
                pts_ENG += 1
                pts_WAL += 1
                draws_ENG += 1
                draws_WAL += 1
        
        if st.checkbox('🇺🇸vs🇮🇷'):
            match_USA += 1
            match_IRN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(USA, key=0, step=1)
            score_2=right_column.number_input(IRN, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇺🇸vs🇮🇷', value=result)

            gd_USA += score_1-score_2
            gd_IRN += score_2-score_1

            if score_1 > score_2:
                pts_USA += 3
                pts_IRN += 0
                wins_USA += 1
                loses_IRN += 1
            elif score_1 < score_2:
                pts_USA += 0
                pts_IRN += 3
                wins_IRN += 1
                loses_USA += 1
            else:
                pts_USA += 1
                pts_IRN += 1
                draws_USA += 1
                draws_IRN += 1

        df_B = pd.DataFrame(
            {
                'teams':[ENG,USA,WAL,IRN],
                'matchs':[match_ENG,match_USA,match_WAL,match_IRN],
                'pts':[pts_ENG,pts_USA,pts_WAL,pts_IRN],
                'W':[wins_ENG,wins_USA,wins_WAL,wins_IRN],
                'D':[draws_ENG,draws_USA,draws_WAL,draws_IRN],
                'L':[loses_ENG,loses_USA,loses_WAL,loses_IRN],
                'gd':[gd_ENG,gd_USA,gd_WAL,gd_IRN]
            }
            )

        df_B = df_B.set_index(['teams'])
        df_B = df_B.sort_values(by=['pts','gd'], ascending=False)

        st.table(df_B.style)

def Group_C():
        st.header('Group C')
    #define
        match_MEX = 0
        match_POL = 0
        match_ARG = 0
        match_SAU = 0
        pts_MEX = 0
        pts_POL = 0
        pts_ARG = 0
        pts_SAU = 0
        wins_MEX = 0
        wins_POL = 0
        wins_ARG = 0
        wins_SAU = 0
        draws_MEX = 0
        draws_POL = 0
        draws_ARG = 0
        draws_SAU = 0
        loses_MEX = 0
        loses_POL = 0
        loses_ARG = 0
        loses_SAU = 0
        gd_MEX = 0
        gd_POL = 0
        gd_ARG = 0
        gd_SAU = 0

        if st.checkbox('🇦🇷vs🇸🇦'):
            match_ARG += 1
            match_SAU += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ARG, key=0, step=1)
            score_2=right_column.number_input(SAU, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇦🇷vs🇸🇦', value=result)

            gd_ARG += score_1-score_2
            gd_SAU += score_2-score_1

            if score_1 > score_2:
                pts_ARG += 3
                pts_SAU += 0
                wins_ARG += 1
                loses_SAU += 1
            elif score_1 < score_2:
                pts_ARG += 0
                pts_SAU += 3
                wins_SAU += 1
                loses_ARG += 1
            else:
                pts_ARG += 1
                pts_SAU += 1
                draws_ARG += 1
                draws_SAU += 1

        if st.checkbox('🇲🇽vs🇵🇱'):
            match_MEX += 1
            match_POL += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(MEX, key=0, step=1)
            score_2=right_column.number_input(POL, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇲🇽vs🇵🇱', value=result)

            gd_MEX += score_1-score_2
            gd_POL += score_2-score_1

            if score_1 > score_2:
                pts_MEX += 3
                pts_POL += 0
                wins_MEX += 1
                loses_POL += 1
            elif score_1 < score_2:
                pts_MEX += 0
                pts_POL += 3
                wins_POL += 1
                loses_MEX += 1
            else:
                pts_MEX += 1
                pts_POL += 1
                draws_MEX += 1
                draws_POL += 1

        if st.checkbox('🇵🇱vs🇸🇦'):
            match_POL += 1
            match_SAU += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(POL, key=2, step=1)
            score_2=right_column.number_input(SAU, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇵🇱vs🇸🇦', value=result)

            gd_POL += score_1-score_2
            gd_SAU += score_2-score_1

            if score_1 > score_2:
                pts_POL += 3
                pts_SAU += 0
                wins_POL += 1
                loses_SAU += 1
            elif score_1 < score_2:
                pts_POL += 0
                pts_SAU += 3
                wins_SAU += 1
                loses_POL += 1
            else:
                pts_POL += 1
                pts_SAU += 1
                draws_POL += 1
                draws_SAU += 1

        if st.checkbox('🇲🇽vs🇦🇷'):
            match_MEX += 1
            match_ARG += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(MEX, key=2, step=1)
            score_2=right_column.number_input(ARG, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇲🇽vs🇦🇷', value=result)

            gd_MEX += score_1-score_2
            gd_ARG += score_2-score_1

            if score_1 > score_2:
                pts_MEX += 3
                pts_ARG += 0
                wins_MEX += 1
                loses_ARG += 1
            elif score_1 < score_2:
                pts_MEX += 0
                pts_ARG += 3
                wins_ARG += 1
                loses_MEX += 1
            else:
                pts_MEX += 1
                pts_ARG += 1
                draws_MEX += 1
                draws_ARG += 1

        if st.checkbox('🇲🇽vs🇸🇦'):
            match_MEX += 1
            match_SAU += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(MEX, key=1, step=1)
            score_2=right_column.number_input(SAU, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇲🇽vs🇸🇦', value=result)

            gd_MEX += score_1-score_2
            gd_SAU += score_2-score_1

            if score_1 > score_2:
                pts_MEX += 3
                pts_SAU += 0
                wins_MEX += 1
                loses_SAU += 1
            elif score_1 < score_2:
                pts_MEX += 0
                pts_SAU += 3
                wins_SAU += 1
                loses_MEX += 1
            else:
                pts_MEX += 1
                pts_SAU += 1
                draws_MEX += 1
                draws_SAU += 1

        if st.checkbox('🇦🇷vs🇵🇱'):
            match_ARG += 1
            match_POL += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ARG, key=1, step=1)
            score_2=right_column.number_input(POL, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇦🇷vs🇵🇱', value=result)

            gd_ARG += score_1-score_2
            gd_POL += score_2-score_1

            if score_1 > score_2:
                pts_ARG += 3
                pts_POL += 0
                wins_ARG += 1
                loses_POL += 1
            elif score_1 < score_2:
                pts_ARG += 0
                pts_POL += 3
                wins_POL += 1
                loses_ARG += 1
            else:
                pts_ARG += 1
                pts_POL += 1
                draws_ARG += 1
                draws_POL += 1

        df_C = pd.DataFrame(
            {
                'teams':[MEX,ARG,POL,SAU],
                'matchs':[match_MEX,match_ARG,match_POL,match_SAU],
                'pts':[pts_MEX,pts_ARG,pts_POL,pts_SAU],
                'W':[wins_MEX,wins_ARG,wins_POL,wins_SAU],
                'D':[draws_MEX,draws_ARG,draws_POL,draws_SAU],
                'L':[loses_MEX,loses_ARG,loses_POL,loses_SAU],
                'gd':[gd_MEX,gd_ARG,gd_POL,gd_SAU]
            }
            )

        df_C = df_C.set_index(['teams'])
        df_C = df_C.sort_values(by=['pts','gd'], ascending=False)

        st.table(df_C.style)

def Group_D():       
        st.header('Group D')
    #define
        match_FRA = 0
        match_AUS = 0
        match_DNK = 0
        match_TUN = 0
        pts_FRA = 0
        pts_AUS = 0
        pts_DNK = 0
        pts_TUN = 0
        wins_FRA = 0
        wins_AUS = 0
        wins_DNK = 0
        wins_TUN = 0
        draws_FRA = 0
        draws_AUS = 0
        draws_DNK = 0
        draws_TUN = 0
        loses_FRA = 0
        loses_AUS = 0
        loses_DNK = 0
        loses_TUN = 0
        gd_FRA = 0
        gd_AUS = 0
        gd_DNK = 0
        gd_TUN = 0

        if st.checkbox('🇩🇰vs🇹🇳'):
            match_DNK += 1
            match_TUN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(DNK, key=0, step=1)
            score_2=right_column.number_input(TUN, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇩🇰vs🇹🇳', value=result)

            gd_DNK += score_1-score_2
            gd_TUN += score_2-score_1

            if score_1 > score_2:
                pts_DNK += 3
                pts_TUN += 0
                wins_DNK += 1
                loses_TUN += 1
            elif score_1 < score_2:
                pts_DNK += 0
                pts_TUN += 3
                wins_TUN += 1
                loses_DNK += 1
            else:
                pts_DNK += 1
                pts_TUN += 1
                draws_DNK += 1
                draws_TUN += 1

        if st.checkbox('🇫🇷vs🇦🇺'):
            match_FRA += 1
            match_AUS += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(FRA, key=0, step=1)
            score_2=right_column.number_input(AUS, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇫🇷vs🇦🇺', value=result)

            gd_FRA += score_1-score_2
            gd_AUS += score_2-score_1

            if score_1 > score_2:
                pts_FRA += 3
                pts_AUS += 0
                wins_FRA += 1
                loses_AUS += 1
            elif score_1 < score_2:
                pts_FRA += 0
                pts_AUS += 3
                wins_AUS += 1
                loses_FRA += 1
            else:
                pts_FRA += 1
                pts_AUS += 1
                draws_FRA += 1
                draws_AUS += 1

        if st.checkbox('🇦🇺vs🇹🇳'):
            match_AUS += 1
            match_TUN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(AUS, key=2, step=1)
            score_2=right_column.number_input(TUN, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇦🇺vs🇹🇳', value=result)

            gd_AUS += score_1-score_2
            gd_TUN += score_2-score_1

            if score_1 > score_2:
                pts_AUS += 3
                pts_TUN += 0
                wins_AUS += 1
                loses_TUN += 1
            elif score_1 < score_2:
                pts_AUS += 0
                pts_TUN += 3
                wins_TUN += 1
                loses_AUS += 1
            else:
                pts_AUS += 1
                pts_TUN += 1
                draws_AUS += 1
                draws_TUN += 1

        if st.checkbox('🇫🇷vs🇩🇰'):
            match_FRA += 1
            match_DNK += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(FRA, key=2, step=1)
            score_2=right_column.number_input(DNK, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇫🇷vs🇩🇰', value=result)

            gd_FRA += score_1-score_2
            gd_DNK += score_2-score_1

            if score_1 > score_2:
                pts_FRA += 3
                pts_DNK += 0
                wins_FRA += 1
                loses_DNK += 1
            elif score_1 < score_2:
                pts_FRA += 0
                pts_DNK += 3
                wins_DNK += 1
                loses_FRA += 1
            else:
                pts_FRA += 1
                pts_DNK += 1
                draws_FRA += 1
                draws_DNK += 1

        if st.checkbox('🇫🇷vs🇹🇳'):
            match_FRA += 1
            match_TUN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(FRA, key=1, step=1)
            score_2=right_column.number_input(TUN, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇫🇷vs🇹🇳', value=result)

            gd_FRA += score_1-score_2
            gd_TUN += score_2-score_1

            if score_1 > score_2:
                pts_FRA += 3
                pts_TUN += 0
                wins_FRA += 1
                loses_TUN += 1
            elif score_1 < score_2:
                pts_gd_FRA += 0
                pts_TUN += 3
                wins_TUN += 1
                loses_FRA += 1
            else:
                pts_FRA += 1
                pts_TUN += 1
                draws_FRA += 1
                draws_TUN += 1

        if st.checkbox('🇩🇰vs🇦🇺'):
            match_DNK += 1
            match_AUS += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(DNK, key=1, step=1)
            score_2=right_column.number_input(AUS, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇩🇰vs🇦🇺', value=result)

            gd_DNK += score_1-score_2
            gd_AUS += score_2-score_1

            if score_1 > score_2:
                pts_DNK += 3
                pts_AUS += 0
                wins_DNK += 1
                loses_AUS += 1
            elif score_1 < score_2:
                pts_DNK += 0
                pts_AUS += 3
                wins_AUS += 1
                loses_DNK += 1
            else:
                pts_DNK += 1
                pts_AUS += 1
                draws_DNK += 1
                draws_AUS += 1

        df_D = pd.DataFrame(
            {
                'teams':[FRA,DNK,AUS,TUN],
                'matchs':[match_FRA,match_DNK,match_AUS,match_TUN],
                'pts':[pts_gd_FRA,pts_DNK,pts_AUS,pts_TUN],
                'W':[wins_FRA,wins_DNK,wins_AUS,wins_TUN],
                'D':[draws_FRA,draws_DNK,draws_AUS,draws_TUN],
                'L':[loses_FRA,loses_DNK,loses_AUS,loses_TUN],
                'gd':[gd_FRA,gd_DNK,gd_AUS,gd_TUN]
            }
            )

        df_D = df_D.set_index(['teams'])
        df_D = df_D.sort_values(by=['pts','gd'], ascending=False)

        st.table(df_D.style)

def Group_E():    
        st.header('Group E')
    #define
        match_ESP = 0
        match_CRI = 0
        match_DEU = 0
        match_JPN = 0
        pts_ESP = 0
        pts_CRI = 0
        pts_DEU = 0
        pts_JPN = 0
        wins_ESP = 0
        wins_CRI = 0
        wins_DEU = 0
        wins_JPN = 0
        draws_ESP = 0
        draws_CRI = 0
        draws_DEU = 0
        draws_JPN = 0
        loses_ESP = 0
        loses_CRI = 0
        loses_DEU = 0
        loses_JPN = 0
        gd_ESP = 0
        gd_CRI = 0
        gd_DEU = 0
        gd_JPN = 0

        if st.checkbox('🇩🇪vs🇯🇵'):
            match_DEU += 1
            match_JPN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(DEU, key=0, step=1)
            score_2=right_column.number_input(JPN, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇩🇪vs🇯🇵', value=result)

            gd_DEU += score_1-score_2
            gd_JPN += score_2-score_1

            if score_1 > score_2:
                pts_DEU += 3
                pts_JPN += 0
                wins_DEU += 1
                loses_JPN += 1
            elif score_1 < score_2:
                pts_DEU += 0
                pts_JPN += 3
                wins_JPN += 1
                loses_DEU += 1
            else:
                pts_DEU += 1
                pts_JPN += 1
                draws_DEU += 1
                draws_JPN += 1

        if st.checkbox('🇪🇸vs🇨🇷'):
            match_ESP += 1
            match_CRI += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ESP, key=0, step=1)
            score_2=right_column.number_input(CRI, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇪🇸vs🇨🇷', value=result)

            gd_ESP += score_1-score_2
            gd_CRI += score_2-score_1

            if score_1 > score_2:
                pts_ESP += 3
                pts_CRI += 0
                wins_ESP += 1
                loses_CRI += 1
            elif score_1 < score_2:
                pts_ESP += 0
                pts_CRI += 3
                wins_CRI += 1
                loses_ESP += 1
            else:
                pts_ESP += 1
                pts_CRI += 1
                draws_ESP += 1
                draws_CRI += 1

        if st.checkbox('🇨🇷vs🇯🇵'):
            match_CRI += 1
            match_JPN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(CRI, key=2, step=1)
            score_2=right_column.number_input(JPN, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇨🇷vs🇯🇵', value=result)

            gd_CRI += score_1-score_2
            gd_JPN += score_2-score_1

            if score_1 > score_2:
                pts_CRI += 3
                pts_JPN += 0
                wins_CRI += 1
                loses_JPN += 1
            elif score_1 < score_2:
                pts_CRI += 0
                pts_JPN += 3
                wins_JPN += 1
                loses_CRI += 1
            else:
                pts_CRI += 1
                pts_JPN += 1
                draws_CRI += 1
                draws_JPN += 1

        if st.checkbox('🇪🇸vs🇩🇪'):
            match_ESP += 1
            match_DEU += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ESP, key=2, step=1)
            score_2=right_column.number_input(DEU, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇪🇸vs🇩🇪', value=result)

            gd_ESP += score_1-score_2
            gd_DEU += score_2-score_1

            if score_1 > score_2:
                pts_ESP += 3
                pts_DEU += 0
                wins_ESP += 1
                loses_DEU += 1
            elif score_1 < score_2:
                pts_ESP += 0
                pts_DEU += 3
                wins_DEU += 1
                loses_ESP += 1
            else:
                pts_ESP += 1
                pts_DEU += 1
                draws_ESP += 1
                draws_DEU += 1

        if st.checkbox('🇪🇸vs🇯🇵'):
            match_ESP += 1
            match_JPN += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(ESP, key=1, step=1)
            score_2=right_column.number_input(JPN, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇪🇸vs🇯🇵', value=result)

            gd_ESP += score_1-score_2
            gd_JPN += score_2-score_1

            if score_1 > score_2:
                pts_ESP += 3
                pts_JPN += 0
                wins_ESP += 1
                loses_JPN += 1
            elif score_1 < score_2:
                pts_ESP += 0
                pts_JPN += 3
                wins_JPN += 1
                loses_ESP += 1
            else:
                pts_ESP += 1
                pts_JPN += 1
                draws_ESP += 1
                draws_JPN += 1

        if st.checkbox('🇩🇪vs🇨🇷'):
            match_DEU += 1
            match_CRI += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(DEU, key=1, step=1)
            score_2=right_column.number_input(CRI, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇩🇪vs🇨🇷', value=result)

            gd_DEU += score_1-score_2
            gd_CRI += score_2-score_1

            if score_1 > score_2:
                pts_DEU += 3
                pts_CRI += 0
                wins_DEU += 1
                loses_CRI += 1
            elif score_1 < score_2:
                pts_DEU += 0
                pts_CRI += 3
                wins_CRI += 1
                loses_DEU += 1
            else:
                pts_DEU += 1
                pts_CRI += 1
                draws_DEU += 1
                draws_CRI += 1

        df_E = pd.DataFrame(
            {
                'teams':[ESP,DEU,CRI,JPN],
                'matchs':[match_ESP,match_DEU,match_CRI,match_JPN],
                'pts':[pts_ESP,pts_DEU,pts_CRI,pts_JPN],
                'W':[wins_ESP,wins_DEU,wins_CRI,wins_JPN],
                'D':[draws_ESP,draws_DEU,draws_CRI,draws_JPN],
                'L':[loses_ESP,loses_DEU,loses_CRI,loses_JPN],
                'gd':[gd_ESP,gd_DEU,gd_CRI,gd_JPN]
            }
            )

        df_E = df_E.set_index(['teams'])
        df_E = df_E.sort_values(by=['pts','gd'], ascending=False)

        st.table(df_E.style)

def Group_F():
        st.header('Group F')
    #define
        match_CAN = 0
        match_BEL = 0
        match_HRV = 0
        match_MAR = 0
        pts_CAN = 0
        pts_BEL = 0
        pts_HRV = 0
        pts_MAR = 0
        wins_CAN = 0
        wins_BEL = 0
        wins_HRV = 0
        wins_MAR = 0
        draws_CAN = 0
        draws_BEL = 0
        draws_HRV = 0
        draws_MAR = 0
        loses_CAN = 0
        loses_BEL = 0
        loses_HRV = 0
        loses_MAR = 0
        gd_CAN = 0
        gd_BEL = 0
        gd_HRV = 0
        gd_MAR = 0

        if st.checkbox('🇭🇷vs🇲🇦'):
            match_HRV += 1
            match_MAR += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(HRV, key=0, step=1)
            score_2=right_column.number_input(MAR, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇭🇷vs🇲🇦', value=result)

            gd_HRV += score_1-score_2
            gd_MAR += score_2-score_1

            if score_1 > score_2:
                pts_HRV += 3
                pts_MAR += 0
                wins_HRV += 1
                loses_MAR += 1
            elif score_1 < score_2:
                pts_HRV += 0
                pts_MAR += 3
                wins_MAR += 1
                loses_HRV += 1
            else:
                pts_HRV += 1
                pts_MAR += 1
                draws_HRV += 1
                draws_MAR += 1

        if st.checkbox('🇨🇦vs🇧🇪'):
            match_CAN += 1
            match_BEL += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(CAN, key=0, step=1)
            score_2=right_column.number_input(BEL, key=0, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇨🇦vs🇧🇪', value=result)

            gd_CAN += score_1-score_2
            gd_BEL += score_2-score_1

            if score_1 > score_2:
                pts_CAN += 3
                pts_BEL += 0
                wins_CAN += 1
                loses_BEL += 1
            elif score_1 < score_2:
                pts_CAN += 0
                pts_BEL += 3
                wins_BEL += 1
                loses_CAN += 1
            else:
                pts_CAN += 1
                pts_BEL += 1
                draws_CAN += 1
                draws_BEL += 1

        if st.checkbox('🇧🇪vs🇲🇦'):
            match_BEL += 1
            match_MAR += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(BEL, key=2, step=1)
            score_2=right_column.number_input(MAR, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇧🇪vs🇲🇦', value=result)

            gd_BEL += score_1-score_2
            gd_MAR += score_2-score_1

            if score_1 > score_2:
                pts_BEL += 3
                pts_MAR += 0
                wins_BEL += 1
                loses_MAR += 1
            elif score_1 < score_2:
                pts_BEL += 0
                pts_MAR += 3
                wins_MAR += 1
                loses_BEL += 1
            else:
                pts_BEL += 1
                pts_MAR += 1
                draws_BEL += 1
                draws_MAR += 1

        if st.checkbox('🇨🇦vs🇭🇷'):
            match_CAN += 1
            match_HRV += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(CAN, key=2, step=1)
            score_2=right_column.number_input(HRV, key=2, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇨🇦vs🇭🇷', value=result)

            gd_CAN += score_1-score_2
            gd_HRV += score_2-score_1

            if score_1 > score_2:
                pts_CAN += 3
                pts_HRV += 0
                wins_CAN += 1
                loses_HRV += 1
            elif score_1 < score_2:
                pts_CAN += 0
                pts_HRV += 3
                wins_HRV += 1
                loses_CAN += 1
            else:
                pts_CAN += 1
                pts_HRV += 1
                draws_CAN += 1
                draws_HRV += 1

        if st.checkbox('🇨🇦vs🇲🇦'):
            match_CAN += 1
            match_MAR += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(CAN, key=1, step=1)
            score_2=right_column.number_input(MAR, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇨🇦vs🇲🇦', value=result)

            gd_CAN += score_1-score_2
            gd_MAR += score_2-score_1

            if score_1 > score_2:
                pts_CAN += 3
                pts_MAR += 0
                wins_CAN += 1
                loses_MAR += 1
            elif score_1 < score_2:
                pts_CAN += 0
                pts_MAR += 3
                wins_MAR += 1
                loses_CAN += 1
            else:
                pts_CAN += 1
                pts_MAR += 1
                draws_CAN += 1
                draws_MAR += 1

        if st.checkbox('🇭🇷vs🇧🇪'):
            match_HRV += 1
            match_BEL += 1
            left_column, middle_column ,right_column = st.columns(3)
            score_1=middle_column.number_input(HRV, key=1, step=1)
            score_2=right_column.number_input(BEL, key=1, step=1)
            result = str(score_1) + '-' + str(score_2)

            left_column.metric(label='🇭🇷vs🇧🇪', value=result)

            gd_HRV += score_1-score_2
            gd_BEL += score_2-score_1

            if score_1 > score_2:
                pts_HRV += 3
                pts_BEL += 0
                wins_HRV += 1
                loses_BEL += 1
            elif score_1 < score_2:
                pts_HRV += 0
                pts_BEL += 3
                wins_BEL += 1
                loses_HRV += 1
            else:
                pts_HRV += 1
                pts_BEL += 1
                draws_HRV += 1
                draws_BEL += 1

        df_F = pd.DataFrame(
            {
                'teams':[CAN,HRV,BEL,MAR],
                'matchs':[match_CAN,match_HRV,match_BEL,match_MAR],
                'pts':[pts_CAN,pts_HRV,pts_BEL,pts_MAR],
                'W':[wins_CAN,wins_HRV,wins_BEL,wins_MAR],
                'D':[draws_CAN,draws_HRV,draws_BEL,draws_MAR],
                'L':[loses_CAN,loses_HRV,loses_BEL,loses_MAR],
                'gd':[gd_CAN,gd_HRV,gd_BEL,gd_MAR]
            }
            )

        df_F = df_F.set_index(['teams'])
        df_F = df_F.sort_values(by=['pts','gd'], ascending=False)

        st.table(df_F.style)

def Group_G():
    st.header('Group G')
#define
    match_BRA = 0
    match_SRB = 0
    match_CHE = 0
    match_CMR = 0
    pts_BRA = 0
    pts_SRB = 0
    pts_CHE = 0
    pts_CMR = 0
    wins_BRA = 0
    wins_SRB = 0
    wins_CHE = 0
    wins_CMR = 0
    draws_BRA = 0
    draws_SRB = 0
    draws_CHE = 0
    draws_CMR = 0
    loses_BRA = 0
    loses_SRB = 0
    loses_CHE = 0
    loses_CMR = 0
    gd_BRA = 0
    gd_SRB = 0
    gd_CHE = 0
    gd_CMR = 0

    if st.checkbox('🇨🇭vs🇨🇲'):
        match_CHE += 1
        match_CMR += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(CHE, key=0, step=1)
        score_2=right_column.number_input(CMR, key=0, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇨🇭vs🇨🇲', value=result)

        gd_CHE += score_1-score_2
        gd_CMR += score_2-score_1

        if score_1 > score_2:
            pts_CHE += 3
            pts_CMR += 0
            wins_CHE += 1
            loses_CMR += 1
        elif score_1 < score_2:
            pts_CHE += 0
            pts_CMR += 3
            wins_CMR += 1
            loses_CHE += 1
        else:
            pts_CHE += 1
            pts_CMR += 1
            draws_CHE += 1
            draws_CMR += 1

    if st.checkbox('🇧🇷vs🇷🇸'):
        match_BRA += 1
        match_SRB += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(BRA, key=0, step=1)
        score_2=right_column.number_input(SRB, key=0, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇧🇷vs🇷🇸', value=result)

        gd_BRA += score_1-score_2
        gd_SRB += score_2-score_1

        if score_1 > score_2:
            pts_BRA += 3
            pts_SRB += 0
            wins_BRA += 1
            loses_SRB += 1
        elif score_1 < score_2:
            pts_BRA += 0
            pts_SRB += 3
            wins_SRB += 1
            loses_BRA += 1
        else:
            pts_BRA += 1
            pts_SRB += 1
            draws_BRA += 1
            draws_SRB += 1

    if st.checkbox('🇷🇸vs🇨🇲'):
        match_SRB += 1
        match_CMR += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(SRB, key=2, step=1)
        score_2=right_column.number_input(CMR, key=2, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇷🇸vs🇨🇲', value=result)

        gd_SRB += score_1-score_2
        gd_CMR += score_2-score_1

        if score_1 > score_2:
            pts_SRB += 3
            pts_CMR += 0
            wins_SRB += 1
            loses_CMR += 1
        elif score_1 < score_2:
            pts_SRB += 0
            pts_CMR += 3
            wins_CMR += 1
            loses_SRB += 1
        else:
            pts_SRB += 1
            pts_CMR += 1
            draws_SRB += 1
            draws_CMR += 1

    if st.checkbox('🇧🇷vs🇨🇭'):
        match_BRA += 1
        match_CHE += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(BRA, key=2, step=1)
        score_2=right_column.number_input(CHE, key=2, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇧🇷vs🇨🇭', value=result)

        gd_BRA += score_1-score_2
        gd_CHE += score_2-score_1

        if score_1 > score_2:
            pts_BRA += 3
            pts_CHE += 0
            wins_BRA += 1
            loses_CHE += 1
        elif score_1 < score_2:
            pts_BRA += 0
            pts_CHE += 3
            wins_CHE += 1
            loses_BRA += 1
        else:
            pts_BRA += 1
            pts_CHE += 1
            draws_BRA += 1
            draws_CHE += 1

    if st.checkbox('🇧🇷vs🇨🇲'):
        match_BRA += 1
        match_CMR += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(BRA, key=1, step=1)
        score_2=right_column.number_input(CMR, key=1, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇧🇷vs🇨🇲', value=result)

        gd_BRA += score_1-score_2
        gd_CMR += score_2-score_1

        if score_1 > score_2:
            pts_BRA += 3
            pts_CMR += 0
            wins_BRA += 1
            loses_CMR += 1
        elif score_1 < score_2:
            pts_BRA += 0
            pts_CMR += 3
            wins_CMR += 1
            loses_BRA += 1
        else:
            pts_BRA += 1
            pts_CMR += 1
            draws_BRA += 1
            draws_CMR += 1

    if st.checkbox('🇨🇭vs🇷🇸'):
        match_CHE += 1
        match_SRB += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(CHE, key=1, step=1)
        score_2=right_column.number_input(SRB, key=1, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇨🇭vs🇷🇸', value=result)

        gd_CHE += score_1-score_2
        gd_SRB += score_2-score_1

        if score_1 > score_2:
            pts_CHE += 3
            pts_SRB += 0
            wins_CHE += 1
            loses_SRB += 1
        elif score_1 < score_2:
            pts_CHE += 0
            pts_SRB += 3
            wins_SRB += 1
            loses_CHE += 1
        else:
            pts_CHE += 1
            pts_SRB += 1
            draws_CHE += 1
            draws_SRB += 1

    df_G = pd.DataFrame(
        {
            'teams':[BRA,CHE,SRB,CMR],
            'matchs':[match_BRA,match_CHE,match_SRB,match_CMR],
            'pts':[pts_BRA,pts_CHE,pts_SRB,pts_CMR],
            'W':[wins_BRA,wins_CHE,wins_SRB,wins_CMR],
            'D':[draws_BRA,draws_CHE,draws_SRB,draws_CMR],
            'L':[loses_BRA,loses_CHE,loses_SRB,loses_CMR],
            'gd':[gd_BRA,gd_CHE,gd_SRB,gd_CMR]
        }
        )

    df_G = df_G.set_index(['teams'])
    df_G = df_G.sort_values(by=['pts','gd'], ascending=False)

    st.table(df_G.style)

def Group_H():    
    st.header('Group H')
#define
    match_PRT = 0
    match_GHA = 0
    match_URY = 0
    match_KOR = 0
    pts_PRT = 0
    pts_GHA = 0
    pts_URY = 0
    pts_KOR = 0
    wins_PRT = 0
    wins_GHA = 0
    wins_URY = 0
    wins_KOR = 0
    draws_PRT = 0
    draws_GHA = 0
    draws_URY = 0
    draws_KOR = 0
    loses_PRT = 0
    loses_GHA = 0
    loses_URY = 0
    loses_KOR = 0
    gd_PRT = 0
    gd_GHA = 0
    gd_URY = 0
    gd_KOR = 0

    if st.checkbox('🇺🇾vs🇰🇷'):
        match_URY += 1
        match_KOR += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(URY, key=0, step=1)
        score_2=right_column.number_input(KOR, key=0, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇺🇾vs🇰🇷', value=result)

        gd_URY += score_1-score_2
        gd_KOR += score_2-score_1

        if score_1 > score_2:
            pts_URY += 3
            pts_KOR += 0
            wins_URY += 1
            loses_KOR += 1
        elif score_1 < score_2:
            pts_URY += 0
            pts_KOR += 3
            wins_KOR += 1
            loses_URY += 1
        else:
            pts_URY += 1
            pts_KOR += 1
            draws_URY += 1
            draws_KOR += 1

    if st.checkbox('🇵🇹vs🇬🇭'):
        match_PRT += 1
        match_GHA += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(PRT, key=0, step=1)
        score_2=right_column.number_input(GHA, key=0, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇵🇹vs🇬🇭', value=result)

        gd_PRT += score_1-score_2
        gd_GHA += score_2-score_1

        if score_1 > score_2:
            pts_PRT += 3
            pts_GHA += 0
            wins_PRT += 1
            loses_GHA += 1
        elif score_1 < score_2:
            pts_PRT += 0
            pts_GHA += 3
            wins_GHA += 1
            loses_PRT += 1
        else:
            pts_PRT += 1
            pts_GHA += 1
            draws_PRT += 1
            draws_GHA += 1

    if st.checkbox('🇬🇭vs🇰🇷'):
        match_GHA += 1
        match_KOR += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(GHA, key=2, step=1)
        score_2=right_column.number_input(KOR, key=2, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇬🇭vs🇰🇷', value=result)

        gd_GHA += score_1-score_2
        gd_KOR += score_2-score_1

        if score_1 > score_2:
            pts_GHA += 3
            pts_KOR += 0
            wins_GHA += 1
            loses_KOR += 1
        elif score_1 < score_2:
            pts_GHA += 0
            pts_KOR += 3
            wins_KOR += 1
            loses_GHA += 1
        else:
            pts_GHA += 1
            pts_KOR += 1
            draws_GHA += 1
            draws_KOR += 1

    if st.checkbox('🇵🇹vs🇺🇾'):
        match_PRT += 1
        match_URY += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(PRT, key=2, step=1)
        score_2=right_column.number_input(URY, key=2, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇵🇹vs🇺🇾', value=result)

        gd_PRT += score_1-score_2
        gd_URY += score_2-score_1

        if score_1 > score_2:
            pts_PRT += 3
            pts_URY += 0
            wins_PRT += 1
            loses_URY += 1
        elif score_1 < score_2:
            pts_PRT += 0
            pts_URY += 3
            wins_URY += 1
            loses_PRT += 1
        else:
            pts_PRT += 1
            pts_URY += 1
            draws_PRT += 1
            draws_URY += 1

    if st.checkbox('🇵🇹vs🇰🇷'):
        match_PRT += 1
        match_KOR += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(PRT, key=1, step=1)
        score_2=right_column.number_input(KOR, key=1, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇵🇹vs🇰🇷', value=result)

        gd_PRT += score_1-score_2
        gd_KOR += score_2-score_1

        if score_1 > score_2:
            pts_PRT += 3
            pts_KOR += 0
            wins_PRT += 1
            loses_KOR += 1
        elif score_1 < score_2:
            pts_PRT += 0
            pts_KOR += 3
            wins_KOR += 1
            loses_PRT += 1
        else:
            pts_PRT += 1
            pts_KOR += 1
            draws_PRT += 1
            draws_KOR += 1

    if st.checkbox('🇺🇾vs🇬🇭'):
        match_URY += 1
        match_GHA += 1
        left_column, middle_column ,right_column = st.columns(3)
        score_1=middle_column.number_input(URY, key=1, step=1)
        score_2=right_column.number_input(GHA, key=1, step=1)
        result = str(score_1) + '-' + str(score_2)

        left_column.metric(label='🇺🇾vs🇬🇭', value=result)

        gd_URY += score_1-score_2
        gd_GHA += score_2-score_1

        if score_1 > score_2:
            pts_URY += 3
            pts_GHA += 0
            wins_URY += 1
            loses_GHA += 1
        elif score_1 < score_2:
            pts_URY += 0
            pts_GHA += 3
            wins_GHA += 1
            loses_URY += 1
        else:
            pts_URY += 1
            pts_GHA += 1
            draws_URY += 1
            draws_GHA += 1

    df_H = pd.DataFrame(
        {
            'teams':[PRT,URY,GHA,KOR],
            'matchs':[match_PRT,match_URY,match_GHA,match_KOR],
            'pts':[pts_PRT,pts_URY,pts_GHA,pts_KOR],
            'W':[wins_PRT,wins_URY,wins_GHA,wins_KOR],
            'D':[draws_PRT,draws_URY,draws_GHA,draws_KOR],
            'L':[loses_PRT,loses_URY,loses_GHA,loses_KOR],
            'gd':[gd_PRT,gd_URY,gd_GHA,gd_KOR]
        }
        )

    df_H = df_H.set_index(['teams'])
    df_H = df_H.sort_values(by=['pts','gd'], ascending=False)

    st.table(df_H.style)

def Round_of_16():
    st.header('Round of 16')
    A1 = 'A1'
    A2 = 'A2'
    B1 = 'B1'
    B2 = 'B2'
    C1 = 'C1'
    C2 = 'C2'
    D1 = 'D1'
    D2 = 'D2'   
    E1 = 'E1'
    E2 = 'E2'
    F1 = 'F1'
    F2 = 'F2'
    G1 = 'G1'
    G2 = 'G2'
    H1 = 'H1'
    H2 = 'H2'

    left_column, right_column = st.columns(2)
    left_column.write('A1:'+A1)
    left_column.write('A2:'+A2)
    left_column.write('B1:'+B1)
    left_column.write('B2:'+B2)
    left_column.write('C1:'+C1)
    left_column.write('C2:'+C2)
    left_column.write('D1:'+D1)
    left_column.write('D2:'+D2)
    right_column.write('E1:'+E1)
    right_column.write('E2:'+E2)
    right_column.write('F1:'+F1)
    right_column.write('F2:'+F2)
    right_column.write('G1:'+G1)
    right_column.write('G2:'+G2)
    right_column.write('H1:'+H1)
    right_column.write('H2:'+H2)



    st.header(A1 + '-' + B2)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(A1, key=0, step=1)
    score_2=right_column.number_input(B2, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= A1 + '-' + B2, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ A1)
    elif score_1 < score_2:
        st.subheader('winner: '+ B2)


    st.header(C1 + '-' + D2)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(C1, key=0, step=1)
    score_2=right_column.number_input(D2, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= C1 + '-' + D2, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ C1)
    elif score_1 < score_2:
        st.subheader('winner: '+ D2)

    st.header(D1 + '-' + C2)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(D1, key=0, step=1)
    score_2=right_column.number_input(C2, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= D1 + '-' + C2, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ D1)
    elif score_1 < score_2:
        st.subheader('winner: '+ C2)

    
    st.header(B1 + '-' + A2)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(B1, key=0, step=1)
    score_2=right_column.number_input(A2, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= B1 + '-' + A2, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ B1)
    elif score_1 < score_2:
        st.subheader('winner: '+ A2)

    
    st.header(E1 + '-' + F2)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(E1, key=0, step=1)
    score_2=right_column.number_input(F2, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= E1 + '-' + F2, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ E1)
    elif score_1 < score_2:
        st.subheader('winner: '+ F2)
    
    
    st.header(G1 + '-' + H2)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(G1, key=0, step=1)
    score_2=right_column.number_input(H2, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= G1 + '-' + H2, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ G1)
    elif score_1 < score_2:
        st.subheader('winner: '+ H2)
    
    st.header(F1 + '-' + E2)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(F1, key=0, step=1)
    score_2=right_column.number_input(E2, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= F1 + '-' + E2, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ F1)
    elif score_1 < score_2:
        st.subheader('winner: '+ E2)
    
    st.header(H1 + '-' + G2)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(H1, key=0, step=1)
    score_2=right_column.number_input(G2, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= H1 + '-' + G2, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ H1)
    elif score_1 < score_2:
        st.subheader('winner: '+ G2)

def Quater_finals():
    st.header('Quater-finals')
    A = 'A'#(A1-B2)
    B = 'B'#(C1-D2)
    C = 'C'#(D1-C2)
    D = 'D'#(B1-A2)
    E = 'E'#(E1-F2)
    F = 'F'#(G1-H2)
    G = 'G'#(F1-E2)
    H = 'H'#(H1-G2)

    st.write('Teams :')
    left_column, middle_column ,right_column = st.columns(3)
    left_column.write(A)
    left_column.write(B)
    left_column.write(C)
    middle_column.write(D)
    middle_column.write(E)
    middle_column.write(F)
    right_column.write(G)
    right_column.write(H)

    st.header(E + '-' + F)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(E, key=0, step=1)
    score_2=right_column.number_input(F, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= E + '-' + F, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ E)
    elif score_1 < score_2:
        st.subheader('winner: '+ F)
    
    st.header(A + '-' + B)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(A, key=0, step=1)
    score_2=right_column.number_input(B, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= A + '-' + B, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ A)
    elif score_1 < score_2:
        st.subheader('winner: '+ B)

    st.header(G + '-' + H)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(G, key=0, step=1)
    score_2=right_column.number_input(H, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= G + '-' + H, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ G)
    elif score_1 < score_2:
        st.subheader('winner: '+ H)
    
    st.header(C + '-' + D)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(C, key=0, step=1)
    score_2=right_column.number_input(D, key=0, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= C + '-' + D, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ C)
    elif score_1 < score_2:
        st.subheader('winner: '+ D)

def Semi_finals():
    st.header('Semi-finals')
    A = 'A'#(E-F)
    B = 'B'#(A-B)
    C = 'C'#(G-H)
    D = 'D'#(C-D)
    
    st.write('Teams :')
    left_column, right_column = st.columns(2)
    left_column.write(A)
    left_column.write(B)
    right_column.write(C)
    right_column.write(D)

    st.header(A + '-' + B)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(A, key= 1, step=1)
    score_2=right_column.number_input(B, key=1, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= A + '-' + B, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ A)
    elif score_1 < score_2:
        st.subheader('winner: '+ B)

    st.header(C + '-' + D)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(C, key=1, step=1)
    score_2=right_column.number_input(D, key=1, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= C + '-' + D, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ C)
    elif score_1 < score_2:
        st.subheader('winner: '+ D)

def Final():
    st.header('Final')
    A = 'A'#(A-B)
    B = 'B'#(C-D)

    st.header(A + '-' + B)
    left_column, middle_column ,right_column = st.columns(3)
    score_1=middle_column.number_input(A, key=2, step=1)
    score_2=right_column.number_input(B, key=2, step=1)
    result = str(score_1) + '-' + str(score_2)
    left_column.metric(label= A + '-' + B, value=result)
    if score_1 > score_2:
        st.subheader('winner: '+ A)
    elif score_1 < score_2:
        st.subheader('winner: '+ B)



#Group Stage
st.sidebar.header('Group Stage')
#Group A
if st.sidebar.checkbox('Group A'):
        Group_A()
        
#Group B
if st.sidebar.checkbox('Group B'):
        Group_B()
        
#Group C
if st.sidebar.checkbox('Group C'):
    Group_C()
    
#Group D
if st.sidebar.checkbox('Group D'):
    Group_D()
       
#Group E
if st.sidebar.checkbox('Group E'):
    Group_E()
        
#Group F
if st.sidebar.checkbox('Group F'):
    Group_F()
        
#Group G
if st.sidebar.checkbox('Group G'):
    Group_G()

#Group H
if st.sidebar.checkbox('Group H'):
    Group_H()
    
#All
if st.sidebar.checkbox('all groups'):
    Group_A()
    Group_B()
    Group_C()
    Group_D()
    Group_E()
    Group_F()
    Group_G()
    Group_H()

#Round of 16
st.sidebar.header('Round of 16')
if st.sidebar.checkbox('Round of 16'):
    Round_of_16()

#Quater-finals
st.sidebar.header('Quater-finals')
if st.sidebar.checkbox('Quater-finals'):
    Quater_finals()

#Semi-finals
st.sidebar.header('Semi-finals')
if st.sidebar.checkbox('Semi-finals'):
    Semi_finals()

#Final
st.sidebar.header('Final')
if st.sidebar.checkbox('Final'):
    Final()