# coding: utf-8

import sqlite3
import pandas as pd

data = pd.read_csv("pokemon.csv",encoding='utf-8')


def df2sqlite(dataframe, db_name = "Pokemon", tbl_name = "poke"):

	import sqlite3
	conn=sqlite3.connect(db_name)
	cur = conn.cursor()

	wildcards = ','.join(['?'] * len(dataframe.columns))
	data = [tuple(x) for x in dataframe.values]

	cur.execute("drop table if exists %s" % tbl_name)

	col_str = '"' + '","'.join(dataframe.columns) + '"'
	cur.execute("create table %s (%s)" % (tbl_name, col_str))

	cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)

	conn.commit()
	conn.close()

df2sqlite(data)
