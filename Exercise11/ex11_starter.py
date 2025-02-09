Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)

character_count = len(Belgium)
print(character_count)

print("-" * 81)

print(Belgium.replace(",",":"))

Belgium_list = ['Belgium', '10445852','Brussels','737966','Europe','1830','Euro','Catholicism','Dutch','French','German']
total_popu = int(Belgium_list[1]) + int(Belgium_list[3])
print(total_popu)