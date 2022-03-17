#this is an example of a scraping program that goes to a football data site and grabs all of the passing (quarterback) data for the specified years and outputs a CSV for each year
#I referenced this blogpost initial conception before adapting to other webpages/content: https://stmorse.github.io/journal/pfr-scrape-python.html
import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://www.pro-football-reference.com'
years = (2018, 2019, 2020, 2021)
for year in years:
    maxp = 500

    #access passing page
    r = requests.get(url + '/years/' + str(year) + '/passing.htm')
    soup = BeautifulSoup(r.content, 'html.parser')

    passing_table = soup.find_all('table')[0]

    col=['name','pos','team','age','games_played','games_started','qb_rec','pass_cmp','pass_att','pass_cmp_perc','pass_yds','pass_td' ,'pass_td_perc','pass_int','pass_int_perc','pass_first_down','pass_long','pass_yds_per_att','pass_adj_yds_per_att',
    'pass_yds_per_cmp','pass_yds_per_g','pass_rating','qbr','pass_sacked','pass_sacked_perc','pass_net_yds_per_att','pass_adj_net_yds_per_att','comebacks','gwd']

    df=[]

    # first 2 rows are col headers
    for i,row in enumerate(passing_table.find_all('tr')[2:]):
        if i % 10 == 0: print(i, end=' ')
        if i >= maxp:
            print('\nComplete.')
            break

        try:
            dat = row.find('td', attrs={'data-stat': 'player'})
            name = dat.a.get_text()
            # grab this players stats
            team = row.find('td', attrs={'data-stat': 'team'}).get_text()
            age = row.find('td', attrs={'data-stat': 'age'}).get_text()
            pos = row.find('td', attrs={'data-stat': 'pos'}).get_text()
            games_played = row.find('td', attrs={'data-stat': 'g'}).get_text()
            games_started = row.find('td', attrs={'data-stat': 'gs'}).get_text()
            qb_rec = row.find('td', attrs={'data-stat': 'qb_rec'}).get_text()
            pass_cmp = row.find('td', attrs={'data-stat': 'pass_cmp'}).get_text()
            pass_att = row.find('td', attrs={'data-stat': 'pass_att'}).get_text()
            pass_cmp_perc = row.find('td', attrs={'data-stat': 'pass_cmp_perc'}).get_text()
            pass_yds = row.find('td', attrs={'data-stat': 'pass_yds'}).get_text()
            pass_td = row.find('td', attrs={'data-stat': 'pass_td'}).get_text()
            pass_td_perc = row.find('td', attrs={'data-stat': 'pass_td_perc'}).get_text()
            pass_int = row.find('td', attrs={'data-stat': 'pass_int'}).get_text()
            pass_int_perc = row.find('td', attrs={'data-stat': 'pass_int_perc'}).get_text()
            pass_first_down = row.find('td', attrs={'data-stat': 'pass_first_down'}).get_text()
            pass_long = row.find('td', attrs={'data-stat': 'pass_int'}).get_text()
            pass_yds_per_att = row.find('td', attrs={'data-stat': 'pass_yds_per_att'}).get_text()
            pass_adj_yds_per_att = row.find('td', attrs={'data-stat': 'pass_adj_yds_per_att'}).get_text()
            pass_yds_per_cmp = row.find('td', attrs={'data-stat': 'pass_yds_per_cmp'}).get_text()
            pass_yds_per_g = row.find('td', attrs={'data-stat': 'pass_yds_per_g'}).get_text()
            pass_rating = row.find('td', attrs={'data-stat': 'pass_rating'}).get_text()
            qbr = row.find('td', attrs={'data-stat': 'qbr'}).get_text()
            pass_sacked = row.find('td', attrs={'data-stat': 'pass_sacked'}).get_text()
            pass_sacked_perc = row.find('td', attrs={'data-stat': 'pass_sacked_perc'}).get_text()
            pass_net_yds_per_att = row.find('td', attrs={'data-stat': 'pass_net_yds_per_att'}).get_text()
            pass_adj_net_yds_per_att = row.find('td', attrs={'data-stat': 'pass_adj_net_yds_per_att'}).get_text()
            comebacks = row.find('td', attrs={'data-stat': 'comebacks'}).get_text()
            gwd = row.find('td', attrs={'data-stat': 'gwd'}).get_text()

            df.append([name,pos,team,age,games_played,games_started,qb_rec,pass_cmp,pass_att,pass_cmp_perc,pass_yds,pass_td ,pass_td_perc,pass_int,pass_int_perc,pass_first_down,pass_long,pass_yds_per_att,pass_adj_yds_per_att,
            pass_yds_per_cmp,pass_yds_per_g,pass_rating,qbr,pass_sacked,pass_sacked_perc,pass_net_yds_per_att,pass_adj_net_yds_per_att,comebacks,gwd])


        except:
            pass
    adv_pass_df = pd.DataFrame(df, columns=col)

    adv_pass_df.head()
    filename = "passing_%s.csv" % year
    adv_pass_df.to_csv(filename)
