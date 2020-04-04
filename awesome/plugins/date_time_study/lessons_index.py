from .lesson import *
#高数：high_math
#英语：english
#大物：Physical
#c++：c_design
#心理课：heart
#创业基础：Business
#离散数学：Li_san
#体育：sports
#商业模式设计：Occupational
#前面的索引代表课程提醒的某时刻，比如高数在早上8点开课，我要让机器人7.45提醒，那么索引就设置为7，目前最多同时支持两个班，
mon_switch_three = {7: high_math, 9: english, 15: Physical}
tue_switch_three = {7: history, 9: Li_San, 13: Occupational, 18: c_design}
web_switch_three = {7: high_math, 9: english, 13: Business, 15: sports}
thu_switch_three = {7: Li_San, 9: history, 13: Physical, 15: heart, 18: c_design}
fri_switch_three = {9: english_listening, 13: high_math}

mon_switch_six = {7: high_math, 13: Physical, 15: Business}
tue_switch_six = {7: high_math, 9: heart, 13: english}
web_switch_six = {7: high_math, 13: history}
thu_switch_six = {7: Li_San, 13: english, 15: english_listening}
fri_switch_six = {7: history, 9: Occupational, 13: high_math, 15: Physical, 18: c_design}
sat_switch_six = {18: c_design}