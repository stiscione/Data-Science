import csv
import sqlite3

conn = sqlite3.connect('')
cur = conn.cursor()
con = sqlite3.connect("FFdb.sqlite")
cur = con.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Rushing;
DROP TABLE IF EXISTS Passing;
DROP TABLE IF EXISTS Receiving;
DROP TABLE IF EXISTS Fantasy;
DROP TABLE IF EXISTS Advanced_passing_accuracy;
DROP TABLE IF EXISTS Advanced_passing_air_yards;
DROP TABLE IF EXISTS Advanced_passing_pressure;
DROP TABLE IF EXISTS Team_stats;
''')

cur.execute("CREATE TABLE Rushing (name, year, pos, team, age, games_played, games_started, rush_att, rush_yds, rush_td, rush_first_down, rush_long, rush_yds_per_att, rush_yds_per_g, fumbles);")
cur.execute("CREATE TABLE Receiving (name, year, pos, team, age, games_played, games_started, targets, rec, catch_pct, rec_yds, rec_yds_per_rec, rec_td, rec_first_down, rec_long, rec_yds_per_tgt, rec_per_g, rec_yds_per_g, fumbles);")
cur.execute("CREATE TABLE Passing (name, year, pos, team, age, games_played, games_started, qb_rec, pass_cmp, pass_att, pass_cmp_perc, pass_yds, pass_td , pass_td_perc, pass_int, pass_int_perc, pass_first_down, pass_long, pass_yds_per_att, pass_adj_yds_per_att, pass_yds_per_cmp, pass_yds_per_g, pass_rating, qbr, pass_sacked, pass_sacked_perc, pass_net_yds_per_att, pass_adj_net_yds_per_att, comebacks, gwd);")
cur.execute("CREATE TABLE Team_stats (team,year,player,points, total_yards,plays_offense,yds_per_play_offense,turnovers,fumbles_lost,first_down,pass_cmp,pass_att,pass_yds,pass_td,pass_int,pass_net_yds_per_att,pass_fd,rush_att,rush_yds,rush_td,rush_yds_per_att, rush_fd, penalties, penalties_yds, pen_fd, drives, score_pct,turnover_pct,start_avg,time_avg,plays_per_drive, yds_per_drive, points_avg);")
cur.execute("CREATE TABLE Fantasy (name, year, pos, age, fantasy_points, fantasy_points_ppr, draftkings_points, fanduel_points, vbd, fantasy_rank_pos, fantasy_rank_overall);")

year_range = ['2018', '2019', '2020', '2021']

for data_year in year_range:
    path = 'C:\\Users\\stisc\\OneDrive\\Documents\\Data Science\\Fantasy Football\\Data\\rushing_'+str(data_year)+'.csv'
    year = data_year
    with open(path,'r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['name'], year, i['pos'], i['team'], i['age'], i['games_played'], i['games_started'], i['rush_att'], i['rush_yds'], i['rush_td'], i['rush_first_down'], i['rush_long'], i['rush_yds_per_att'], i['rush_yds_per_g'], i['fumbles']) for i in dr]
    cur.executemany("INSERT INTO Rushing (name, year, pos, team, age, games_played, games_started, rush_att, rush_yds, rush_td, rush_first_down, rush_long, rush_yds_per_att, rush_yds_per_g, fumbles) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

for data_year in year_range:
    path = 'C:\\Users\\stisc\\OneDrive\\Documents\\Data Science\\Fantasy Football\\Data\\receiving_'+str(data_year)+'.csv'
    year = data_year
    with open(path,'r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['name'], year, i['pos'], i['team'], i['age'], i['games_played'], i['games_started'], i['targets'], i['rec'], i['catch_pct'], i['rec_yds'], i['rec_yds_per_rec'], i['rec_td'], i['rec_first_down'], i['rec_long'], i['rec_yds_per_tgt'], i['rec_per_g'], i['rec_yds_per_g'], i['fumbles']) for i in dr]
    cur.executemany("INSERT INTO Receiving (name, year, pos, team, age, games_played, games_started, targets, rec, catch_pct, rec_yds, rec_yds_per_rec, rec_td, rec_first_down, rec_long, rec_yds_per_tgt, rec_per_g, rec_yds_per_g, fumbles) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

for data_year in year_range:
    path = 'C:\\Users\\stisc\\OneDrive\\Documents\\Data Science\\Fantasy Football\\Data\\passing_'+str(data_year)+'.csv'
    year = data_year
    with open(path,'r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['name'], year, i['pos'], i['team'], i['age'], i['games_played'], i['games_started'], i['qb_rec'], i['pass_cmp'], i['pass_att'], i['pass_cmp_perc'], i['pass_yds'], i['pass_td'], i['pass_td_perc'], i['pass_int'], i['pass_int_perc'], i['pass_first_down'], i['pass_long'], i['pass_yds_per_att'], i['pass_adj_yds_per_att'], i['pass_yds_per_cmp'], i['pass_yds_per_g'], i['pass_rating'], i['qbr'], i['pass_sacked'], i['pass_sacked_perc'], i['pass_net_yds_per_att'], i['pass_adj_net_yds_per_att'], i['comebacks'], i['gwd']) for i in dr]
    cur.executemany("INSERT INTO Passing (name, year, pos, team, age, games_played, games_started, qb_rec, pass_cmp, pass_att, pass_cmp_perc, pass_yds, pass_td , pass_td_perc, pass_int, pass_int_perc, pass_first_down, pass_long, pass_yds_per_att, pass_adj_yds_per_att, pass_yds_per_cmp, pass_yds_per_g, pass_rating, qbr, pass_sacked, pass_sacked_perc, pass_net_yds_per_att, pass_adj_net_yds_per_att, comebacks, gwd) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

for data_year in year_range:
    path = 'C:\\Users\\stisc\\OneDrive\\Documents\\Data Science\\Fantasy Football\\Data\\fantasy_'+str(data_year)+'.csv'
    year = data_year
    with open(path,'r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['name'], year, i['pos'], i['age'], i['fantasy_points'], i['fantasy_points_ppr'], i['draftkings_points'], i['fanduel_points'], i['vbd'], i['fantasy_rank_pos'], i['fantasy_rank_overall']) for i in dr]
    cur.executemany("INSERT INTO Fantasy (name, year, pos, age, fantasy_points, fantasy_points_ppr, draftkings_points, fanduel_points, vbd, fantasy_rank_pos, fantasy_rank_overall) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

path = 'C:\\Users\\stisc\\OneDrive\\Documents\\Data Science\\Fantasy Football\\Data\\team_stats.csv'
with open(path,'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['team'], i['year'], i['player'], i['points'], i['total_yards'], i['plays_offense'], i['yds_per_play_offense'], i['turnovers'], i['fumbles_lost'], i['first_down'], i['pass_cmp'], i['pass_att'], i['pass_yds'], i['pass_td'], i['pass_int'], i['pass_net_yds_per_att'], i['pass_fd'], i['rush_att'], i['rush_yds'], i['rush_td'], i['rush_yds_per_att'], i['rush_fd'], i['penalties'], i['penalties_yds'], i['pen_fd'], i['drives'], i['score_pct'],i['turnover_pct'], i['start_avg'],i['time_avg'], i['plays_per_drive'], i['yds_per_drive'], i['points_avg']) for i in dr]
cur.executemany("INSERT INTO Team_stats (team, year, player, points, total_yards, plays_offense, yds_per_play_offense, turnovers, fumbles_lost, first_down, pass_cmp, pass_att, pass_yds, pass_td, pass_int, pass_net_yds_per_att, pass_fd, rush_att, rush_yds, rush_td, rush_yds_per_att, rush_fd, penalties, penalties_yds, pen_fd, drives, score_pct, turnover_pct, start_avg, time_avg, plays_per_drive, yds_per_drive, points_avg) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

con.commit()
con.close()
