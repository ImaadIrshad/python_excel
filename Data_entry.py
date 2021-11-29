import PySimpleGUI as sg
import datetime
import pandas as pd


dt = datetime.datetime.now()

sg.theme('Black')

EXCEL_FILE = 'Data_entry.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
	[sg.Text('Please fill out the following fields:')],
	[sg.Text('Crypto Name', size=(15,1)), sg.InputText(key='Name')],
	[sg.Text('Date', size=(15,1)), sg.InputText(dt.strftime("%d-%m-%y %H:%M:%S"), key='Date')],
	[sg.Text('Invested?', size=(15,1)), sg.Combo(['Yes', 'No'], key='Invested?')],
	[sg.Text('Entry Price', size=(15,1)), sg.InputText(key='Entry Price')],
	[sg.Text('Marketcap', size=(15,1)), sg.InputText(key='Marketcap')],
	[sg.Text('Community Number', size=(15,1)), sg.InputText(key='Community Number')],
	[sg.Text('Purpose', size=(15,1)), sg.InputText(key='Purpose')],
	[sg.Text('Uniquity', size=(15,1)), sg.InputText(key='Uniquity')],
	[sg.Text('Consensus Algorithm', size=(15,1)), sg.InputText(key='Consensus Algorithm')],
	[sg.Text('News and Trends', size=(15,1)), sg.InputText(key='News and Trends')],

	[sg.Submit(), sg.Button('Clear'), sg.Exit()],
]

window = sg.Window('Simple Crypto Aid', layout)

def clear_input():
	for key in values: 
		window[key]('')
	return None

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Exit':
		break
	if event == 'Clear':
			clear_input()
	if event == 'Submit':
		df = df.append(values, ignore_index=True)
		df.to_excel(EXCEL_FILE, index=False)
		sg.popup('Data saved!')
		clear_input()
window.close()