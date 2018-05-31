#!/usr/bin/env python3
import psycopg2
data_base = "news"
conn = psycopg2.connect(database="news", user="vagrant", password="vagrant")
if conn:
    print("connected successfully!")
else:
    print("Error in connecting the database")
cur = conn.cursor()


def popular_articles():
    cur.execute("select * from art_view limit 3;")
    a = cur.fetchall()
    print("\n")
    print("Most popular articles of all the time are:")
    for i in range(0, len(a), 1):
        print("\"" + a[i][0] + "\" - " + str(a[i][1]) + " views")


def popular_authors():
    cur.execute("select name,count from author_view2 limit 3;")
    b = cur.fetchall()
    print("\n")
    print("Most popular authors of all the time are:")
    for j in range(0, len(b), 1):
        print("\"" + b[j][0] + "\" - " + str(b[j][1]) + "veiws")


def error_percentage():
    cur.execute("select * from error_percent where error_cent>1")
    c = cur.fetchall()
    print("\n")
    print("The day with maximum number of errors is:")
    for i in range(0, len(c), 1):
        print str(c[i][0]) + " - "+str(round(c[i][1], 2))+"% errors"
popular_articles()
popular_authors()
error_percentage()
cur.close()
conn.close()
