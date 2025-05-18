import openpyxl, pprint
print("ワークブックを開いています。。。。")
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
county_data = {}

print("行を読み込んでいます。。。。")
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the state exists in the county_data dictionary.
    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})
    county_data[state][county]['tracts'] += 1
    county_data[state][county]['pop'] += int(pop)
print("結果を書き込み中。。。。")
result_file = open('census2010.data', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print("完了") 


#　面白い、あの形のデータを辞書式で取り込むのは面白いアイデアだ