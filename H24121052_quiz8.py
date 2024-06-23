import csv

def read_nba_standings(file_name):
    eastern_teams_gt_05 = []
    western_teams_home_lt_away = []
    eastern_teams_avg_point_diff = 0
    eastern_teams_count = 0
    wp=0
    ep=0

    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  

        #定義資料裡的欄位
        for row in reader:
            print(row)
            if row==[]:
                break
            conference = row[0]
            team = row[1]
            win_loss_pct = float(row[3])
            home_record = row[7]
            away_record = row[8]
            points_for = float(row[5])
            points_against = float(row[6])
            #print(conference)
            print(home_record)
            print(home_record[0])
            new=[]

            new.append(home_record.split("-"))
            print(new)
            new_rate=(int(new[0][0])/int(new[0][1]))

            new2=[]

            new2.append(away_record.split("-"))
            print(new2)
            new2_rate=(int(new2[0][0])/int(new2[0][1]))

        
            #東區勝率大於0.5
            #if conference == 'Eastern' and win_loss_pct > 0.5:
              #  eastern_teams_gt_05.append(team)
            #西區勝率大於0.5
            #if conference == 'Western' and calculate_win_rate(home_record) < calculate_win_rate(away_record):
              #  western_teams_home_lt_away.append(team)
            #計算東區勝率大於0.5的隊伍數以及分數差額(為計算平均差異)
            if conference == 'Eastern' and win_loss_pct > 0.5:
                eastern_teams_avg_point_diff += points_for - points_against
                eastern_teams_count += 1
            #東區主客比
            if conference == 'Eastern' :
                if new_rate - new2_rate <0:
                    eastern_teams_gt_05.append(team)
            #哪一區的球隊擁有較高的“平均得分減掉失分”)
            if conference == 'Eastern' :
                a=points_for-points_against
                ep+=a
            if conference == 'Western' :
                a=points_for-points_against
                wp+=a
        if ep>wp:
            western_teams_home_lt_away.append('Eastern')
        else:
            western_teams_home_lt_away.append('Western')




    return eastern_teams_gt_05, western_teams_home_lt_away, eastern_teams_avg_point_diff / eastern_teams_count

#計算勝率(檔案中的W-L欄位)
def calculate_win_rate(record):
    wins, losses = map(int, record.split('-'))
    total_games = wins + losses
    return wins / total_games


#輸出
file_name = 'pe8_data.csv'
eastern_teams_gt_05, western_teams_home_lt_away, avg_point_diff = read_nba_standings(file_name)

print("(1) (東區哪些球隊的主場勝率低於客場勝率:")
for team in eastern_teams_gt_05:
    print(team)

print("\n(2) 哪一區的球隊擁有較高的“平均得分減掉失分:")
for team in western_teams_home_lt_away:
    print(team)

#print("\n(3) Average difference between points scored and points allowed for teams in the Eastern Conference with a win-loss percentage greater than 0.5:")
#print(avg_point_diff)