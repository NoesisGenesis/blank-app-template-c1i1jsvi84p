import streamlit as st

st.title('Employee Cost Savings Calculator')

# Slider for employee hourly wage
hourly_wage = st.slider('Employee Hourly Wage ($)', min_value=10, max_value=100, value=25)

# Slider for percentage of work that can be saved
work_saved = st.slider('Percentage of Work Saved (%)', min_value=0, max_value=100, value=50)

# Number of employees
num_employees = st.number_input('Number of Employees', min_value=1, value=3)

# Slider for hours worked per day
hours_per_day = st.slider('Hours Worked per Day', min_value=1, max_value=8, value=8)

# Calculation of cost savings
days_per_week = 5
weeks_per_year = 52
hours_per_week = hours_per_day * days_per_week
total_hours_saved_per_year = hours_per_week * weeks_per_year * (work_saved / 100) * num_employees
annual_savings = total_hours_saved_per_year * hourly_wage

st.write(f'With {work_saved}% of work saved, you will save approximately ${annual_savings:,.2f} per year.')

# Additional breakdown
st.write(f'Total hours saved per year: {total_hours_saved_per_year:.0f} hours')
st.write(f'Total savings per employee per year: ${total_hours_saved_per_year * hourly_wage / num_employees:,.2f}')
